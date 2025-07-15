# --- Welcome to the Demo of the Moorcheh Vector Store ---
# --- We will be using Moorcheh and LlamaIndex to search through Financial Documents

# --- Please run the following installation commands on your terminal ---

'''
pip install moorcheh-sdk langchain_community pypdf pandas
'''

import os
import csv
import pandas as pd
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import time
from sentence_transformers import SentenceTransformer  # Optional: Can be used for embedding
from moorcheh_sdk import MoorchehClient


MOORCHEH_API_KEY = userdata.get("MOORCHEH_API_KEY")

namespace_name="new_namepsaces"
client = MoorchehClient(api_key=MOORCHEH_API_KEY)
client.create_namespace(namespace_name=namespace_name, type="text")

pdf_path = "CombinedDoc.pdf"
query_csv_path = "queries.csv" # Path to your CSV file with queries
output_csv_path = "answers.csv" # Where to save the results
top_k = 5


loader = PyPDFLoader(pdf_path)
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=120)
chunks = splitter.split_documents(pages)


documents = []
for i, chunk in enumerate(chunks):
    text = chunk.page_content.strip()
    documents.append({"id": f"chunk_{i}",
                      "text": text})

client.upload_documents(namespace_name=namespace_name, documents=documents)


queries_df = pd.read_csv(query_csv_path) # Load your questions from a CSV file

with open(output_csv_path, "w", newline="") as f: # Open the results CSV file
    writer = csv.DictWriter(f, fieldnames=["passage_id", "query", "generated_answers"]) # Set up CSV columns
    writer.writeheader() # Write the column headers

    for idx, q in enumerate(queries_df["query"]): # Go through each question
        print(f"Processing: {q}") # Show which question is being processed
        try:
            response = client.get_generative_answer(query = q,
                                               ai_model = "anthropic.claude-3-7-sonnet-20250219-v1:0",
                                               namespace=namespace_name).get("answer", "")
            time.sleep(0.5)
            writer.writerow({ # Write the results to the CSV
                "passage_id": idx, # Unique ID for this answer
                "query": q, # The original question
                "generated_answers": response # The AI-generated answer
            })
        except Exception as e: # If something goes wrong
            print(f"Error for query '{q}':", e) # Print the error
