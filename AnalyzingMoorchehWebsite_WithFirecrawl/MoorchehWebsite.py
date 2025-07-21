# --- Welcome to the Demo of the Moorcheh Client ---
# --- We will be using Moorcheh and Firecrawl to answer queries about the Moorcheh Website ---

# --- Please run the following installation commands on your terminal ---
'''
!pip install firecrawl-py
!pip install moorcheh-sdk
'''

# --- Import Necessary Packages ---

import os
import csv
import time
import logging
from typing import List
import pandas as pd
from firecrawl import FirecrawlApp
from moorcheh_sdk import MoorchehClient


# --- Logging ---
logging.basicConfig(level=logging.INFO)


# --- API Keys ---
FIRECRAWL_API_KEY = os.environ["FIRECRAWL_API_KEY"]
MOORCHEH_API_KEY = os.environ["MOORCHEH_API_KEY"]

if not FIRECRAWL_API_KEY or not MOORCHEH_API_KEY:
    raise EnvironmentError("Missing FIRECRAWL_API_KEY or MOORCHEH_API_KEY")


# --- Initialize Clients ---
firecrawl_app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
moorcheh_client = MoorchehClient(api_key=MOORCHEH_API_KEY)


# --- Config ---
NAMESPACE = "moorcheh_website"
NAMESPACE_TYPE = "text"
VECTOR_DIM = None
QUERY_CSV = "queries.csv"
OUTPUT_CSV = "answers.csv"
SCRAPE_URLS = ["https://www.moorcheh.ai/about"]
AI_MODEL = "anthropic.claude-3-7-sonnet-20250219-v1:0"


# --- Scrape and Chunk ---
def scrape_and_chunk(urls: List[str], min_len: int = 20) -> List[dict]:
    chunks = []
    for url in urls:
        result = firecrawl_app.scrape_url(url)
        content = result.markdown  
        for i, sentence in enumerate(content.split(".")):
            sentence = sentence.strip()
            if len(sentence) > min_len:
                chunks.append({
                    "id": f"{NAMESPACE}-{i}",
                    "text": sentence,
                    "metadata": {"source": url}
                })
    return chunks


# --- Upload in Batches  ---
def upload_in_batches(client, namespace_name, documents, batch_size=100):
    total = len(documents)
    for i in range(0, total, batch_size):
        batch = documents[i:i+batch_size]
        logging.info(f"Uploading batch {i//batch_size + 1}: {len(batch)} documents")
        client.upload_documents(namespace_name=namespace_name, documents=batch)
        time.sleep(0.2)


logging.info("Scraping content...")
documents = scrape_and_chunk(SCRAPE_URLS)


# --- Upload to Moorcheh ---
logging.info(f"Creating namespace '{NAMESPACE}' and uploading {len(documents)} chunks...")

moorcheh_client.create_namespace(namespace_name=NAMESPACE, type=NAMESPACE_TYPE, vector_dimension=VECTOR_DIM)
upload_in_batches(
    client=moorcheh_client,
    namespace_name=NAMESPACE,
    documents=documents,
    batch_size=100
)


# --- Run Queries ---
if not os.path.exists(QUERY_CSV):
    raise FileNotFoundError(f"Missing: {QUERY_CSV}")

queries_df = pd.read_csv(QUERY_CSV)

with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["passage_id", "query", "generated_answers"])
    writer.writeheader()

    for idx, row in queries_df.iterrows():
        query = row["query"]
        logging.info(f"Query {idx + 1}: {query}")
        try:
            response = moorcheh_client.get_generative_answer(
                namespace=NAMESPACE,
                query=query,
                ai_model=AI_MODEL
            )
            writer.writerow({
                "passage_id": idx,
                "query": query,
                "generated_answers": response.get("answer", "No answer.")
            })
            time.sleep(0.5)
        except Exception as e:
            logging.error(f"Error for query '{query}': {e}")
            writer.writerow({
                "passage_id": idx,
                "query": query,
                "generated_answers": f"ERROR: {e}"
            })

