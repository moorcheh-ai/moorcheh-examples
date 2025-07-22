# --- Welcome to the Demo of the Moorcheh Chatbot ---
# --- We will be using Moorcheh, LlamaIndex, and Firecrawl to create a chatbot

# --- Please run the following installation commands on your terminal ---
!pip install llama-index-vector-stores-moorcheh
!pip install pandas
!pip install llama-index-readers-file
!pip install firecrawl-py


# --- Import Necessary Packages ---
import os
import csv
import sys
import pandas as pd
import time
import logging
from llama_index.vector_stores.moorcheh import MoorchehVectorStore
from llama_index.core import SimpleDirectoryReader, Settings
from firecrawl import FirecrawlApp

# --- Preparation Variables ---
MOORCHEH_API_KEY = userdata.get("MOORCHEH_API_KEY")
FIRECRAWL_API_KEY = userdata.get("FIRECRAWL_API_KEY")
firecrawl_app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

namespace_name="firecrawl_llama_moorcheh"
documents_folder="./documents"
SCRAPE_URLS = [ "https://console.moorcheh.ai/docs", "https://www.moorcheh.ai/about"]
namespace_type="text" # or vector
query_csv_path = "queries.csv" # Path to your CSV file with queries
output_csv_path = "answers.csv" # Where to save the results
top_k = 5

# --- Scrape and Chunk ---
from typing import List

def scrape_and_chunk(urls: List[str], min_len: int = 20) -> List[dict]:
    chunks = []
    last_idx = 0
    for url in urls:
        result = firecrawl_app.scrape_url(url)
        content = result.markdown
        for i, sentence in enumerate(content.split(".")):
            sentence = sentence.strip()
            if len(sentence) > min_len:
                chunks.append({
                    "id": f"{namespace_name}-{last_idx + i}", # Use namespace_name instead of NAMESPACE
                    "text": sentence,
                    "metadata": {"source": url}
                })
        last_idx += len(chunks)
    return chunks

logging.info("Scraping content...")
documents_fc = scrape_and_chunk(SCRAPE_URLS)

# --- Prepare Documents ---
documents = SimpleDirectoryReader(documents_folder).load_data()
documents = [doc for doc in documents if hasattr(doc, 'text') and isinstance(doc.text, str) and doc.text.strip()]
start_idx = len(documents_fc)
output = [{"id": f"chunk_{start_idx + idx}", "text": doc.text_resource.text} for idx, doc in enumerate(documents)]
output += documents_fc

# --- Set chunk size and overlap ---
Settings.chunk_size = 5000
Settings.chunk_overlap = 20

# --- Initialize the Moorcheh Vector Store ---
__all__ = ["MoorchehVectorStore"]

vector_store = MoorchehVectorStore(
    api_key=MOORCHEH_API_KEY,
    namespace=namespace_name,
    namespace_type=namespace_type,
    vector_dimension=None,
    add_sparse_vector=False,
    batch_size=100,
)

# --- Upload Documents ---
# Batch Upload the pdf
batch_size = 5
for start in range(1, len(documents), batch_size):
    vector_store._client.upload_documents(
        namespace_name=namespace_name,
        documents=documents[start:start + batch_size]
    )

# --- Generate Response ---

#loop_handling for prompts
def loop_handling(prompt):
  user_input = input(prompt).lower()
  if user_input == "y":
    return True
  elif user_input == "n":
    return False
  else:
    print("Invalid input. Please enter 'y' or 'n'.")
    return loop_handling(prompt)

#continues asking queries by user input unless user specifics "n" or "N"
loop = loop_handling("Do you want to enter a query? (y/n): ")

while loop == True:
  inputted_query = input("Please enter your query: ")
  response = vector_store.get_generative_answer(query = inputted_query, ai_model = "anthropic.claude-3-7-sonnet-20250219-v1:0", llm=None)
  print(response)
  loop = loop_handling("Do you want to enter a query? (y/n): ")

print("Exiting Query tool. Goodbye!")
