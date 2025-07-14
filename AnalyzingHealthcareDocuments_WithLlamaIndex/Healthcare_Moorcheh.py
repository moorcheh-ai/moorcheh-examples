# --- Welcome to the Demo of the Moorcheh Vector Store ---
# --- We will be using Moorcheh and LlamaIndex to search through Healthcare Documents

# --- Please run the following installation commands on your terminal ---
'''
!pip install llama-index-vector-stores-moorcheh
!pip install llama-index-embeddings-openai
!pip install pandas
!pip install llama-index-readers-file
!pip install llama-index llama-index-llms-openai
'''

# --- Import the Necessary Packages ---
import logging
import sys
import os
import csv
import pandas as pd
import time

from llama_index.vector_stores.moorcheh import MoorchehVectorStore
from IPython.display import Markdown, display
from typing import Any, Callable, Dict, List, Optional, cast
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    Settings,
)
from llama_index.core.base.embeddings.base_sparse import BaseSparseEmbedding
from llama_index.core.bridge.pydantic import PrivateAttr
from llama_index.core.schema import BaseNode, MetadataMode, TextNode
from llama_index.core.vector_stores.types import (
    BasePydanticVectorStore,
    MetadataFilters,
    VectorStoreQuery,
    VectorStoreQueryMode,
    VectorStoreQueryResult,
)
from llama_index.core.vector_stores.utils import (
    DEFAULT_TEXT_KEY,
    legacy_metadata_dict_to_node,
    metadata_dict_to_node,
    node_to_metadata_dict,
)
from llama_index.core.vector_stores.types import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
    FilterCondition,
)
from llama_index.llms.openai import OpenAI

# --- Logging Setup ---
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))



# --- Initialization Setup ---
MOORCHEH_API_KEY = os.environ["MOORCHEH_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Optional: Create LLM object for LLMs integrated with LlamaIndex
llm = OpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)

namespace_name="llamaindex_moorcheh6"
documents_folder="./documents"
namespace_type="text" # or vector
query_csv_path = "queries.csv" # Path to your CSV file with queries
output_csv_path = "answers.csv" # Where to save the results
top_k = 5

if "MOORCHEH_API_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable MOORCHEH_API_KEY is not set")
if "OPENAI_API_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable OPENAI_API_KEY is not set")
print(OPENAI_API_KEY)
# --- Load Documents ---
documents = SimpleDirectoryReader(documents_folder).load_data()

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

# --- Create a Vector Store Index using the Vector Store and given Documents ---
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)


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
