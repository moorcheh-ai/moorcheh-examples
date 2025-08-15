!pip install langchain-moorcheh
!pip install langchain-community pypdf

from langchain_moorcheh import MoorchehVectorStore
from moorcheh_sdk import MoorchehClient

import logging
import os
import uuid
import asyncio
from typing import Any, List, Optional, Literal, Tuple, Type, TypeVar, Sequence
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

MOORCHEH_API_KEY = os.environ.get('MOORCHEH_API_KEY')
namespace = "your_namespace_name"
namespace_type = "text" # or vector
store = MoorchehVectorStore(
            api_key=MOORCHEH_API_KEY,
            namespace=namespace,
            namespace_type=namespace_type
        )

pdf_path = "your-pdf-path.pdf" #input your-pdf-path here
top_k = 5

loader = PyPDFLoader(pdf_path)
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=120)
chunks = splitter.split_documents(pages)

documents = []
doc_id = []

for i, chunk in enumerate(chunks):
    text = chunk.page_content.strip()
    doc_id.append(f"chunk_{i}")
    documents.append(Document(page_content=text, metadata={"topic": "LLMs"}))

store.add_documents(documents=documents, ids=doc_id)

query = "Give me a brief history on the research of Large Language Models."
answer = store.generative_answer(query, ai_model = "anthropic.claude-3-7-sonnet-20250219-v1:0")
print(answer)
