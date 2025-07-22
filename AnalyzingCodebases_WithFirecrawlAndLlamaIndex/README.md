# CodeRAGen: Coding with Moorcheh

This example demonstrates how to build a **Retrieval-Augmented Generation (RAG)** pipeline to search and answer questions about code — specifically the **Moorcheh SDK** — using **Moorcheh** as the vector database and **LlamaIndex** & **firecrawl** for document+website ingestion and querying.

## Key Features

- Uses **Moorcheh's API** for embedding, storage, and retrieval
- Uses **Firecrawl's API** for website ingestion
- Uses **LlamaIndex** for document ingestion
- Can dynamically enter queries based on user input
  
## Files Included

- `InteractiveMoorchehChatbot.ipynb` – Notebook version of the pipeline
- `InteractiveMoorchehChatbot.py` –  Python Script version 
- `README.md` – This file

## Requirements

- Python 3.9+
- Moorcheh API Key (get one at [moorcheh.ai](https://www.moorcheh.ai))

## Running the Pipeline

You can either run the pipeline as a Jupyter notebook or a Python script:

**Notebook:**
```bash
jupyter notebook InteractiveMoorchehChatbot.ipynb
