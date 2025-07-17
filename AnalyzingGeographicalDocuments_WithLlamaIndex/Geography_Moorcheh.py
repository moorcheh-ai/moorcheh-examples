# --- Welcome to the Demo of the Moorcheh Vector Store ---
# --- We will be using Moorcheh and LlamaIndex to search through Healthcare Documents

# --- Please run the following installation commands on your terminal ---
'''
!pip install llama-index-vector-stores-moorcheh
!pip install pandas
!pip install llama-index-readers-file
'''

import os
import csv 
import sys
import logging
import pandas as pd 
import time 
from llama_index.vector_stores.moorcheh import MoorchehVectorStore 
from llama_index.core import SimpleDirectoryReader, Settings

# --- Logging Setup ---
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# --- Initialization Setup ---
MOORCHEH_API_KEY = os.environ["MOORCHEH_API_KEY"]

if "MOORCHEH_API_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable MOORCHEH_API_KEY is not set")
  

namespace_name="llamaindex_moorcheh3136"
documents_folder="./documents"
namespace_type="text" # or vector
query_csv_path = "queries.csv" # Path to your CSV file with queries
output_csv_path = "answers.csv" # Where to save the results
top_k = 5


# --- Load Documents ---
documents = SimpleDirectoryReader(documents_folder).load_data()
documents = [doc for doc in documents if hasattr(doc, 'text') and isinstance(doc.text, str) and doc.text.strip()]
output = [{"id": f"chunk_{idx}", "text": doc.text_resource.text} for idx, doc in enumerate(documents)]
print(output)
# --- Set chunk size and overlap ---
Settings.chunk_size = 1024
Settings.chunk_overlap = 20


# --- Initialize the Moorcheh Vector Store ---
__all__ = ["MoorchehVectorStore"]

# Creates a Moorcheh Vector Store with the following parameters
# For text-based namespaces, set namespace_type to "text" and vector_dimension to None
# For vector-based namespaces, set namespace_type to "vector" and vector_dimension to the dimension of your uploaded vectors
vector_store = MoorchehVectorStore(
    api_key=MOORCHEH_API_KEY,
    namespace=namespace_name,
    namespace_type=namespace_type,
    vector_dimension=None,
    add_sparse_vector=False,
    batch_size=100,
)

'''
# --- Create a Vector Store Index using the Vector Store and given Documents ---
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)
'''
vector_store._client.upload_documents(namespace_name=namespace_name, documents=output)


# --- Generate Response ---
# --- Set Logging to DEBUG for more Detailed Outputs ---

queries_df = pd.read_csv(query_csv_path) 

with open(output_csv_path, "w", newline="") as f: 
    writer = csv.DictWriter(f, fieldnames=["passage_id", "query", "generated_answers"]) 
    writer.writeheader() 

    for idx, q in enumerate(queries_df["query"]): 
        print(f"Processing: {q}") 
        try:
            response = vector_store.get_generative_answer(query = q, ai_model = "anthropic.claude-3-7-sonnet-20250219-v1:0", llm=None)
            time.sleep(0.5)
            writer.writerow({ 
                "passage_id": idx, 
                "query": q,
                "generated_answers": response 
            })
        except Exception as e: 
            print(f"Error for query '{q}':", e) 
