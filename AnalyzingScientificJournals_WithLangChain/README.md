# AI Research Assistant: Semantic Search over Scientific Journals with Moorcheh

This example demonstrates how to build a **Retrieval-Augmented Generation (RAG)** pipeline tailored for academic and scientific literature using **Moorcheh** as the vector store and **LangChain** for document ingestion and querying.

Designed for researchers, this pipeline enables intelligent search and summarization across journal articles — making it easier to extract insights from publications.

## Key Features

- Leverages **Moorcheh’s API** for embedding, indexing, and retrieval  
- Ingests scientific PDFs, abstracts, and metadata for full-document search  
- Provides semantic answers to research questions across multiple papers  
- Uses a **single API call** to perform search and AI-generated summarization  

## What’s Included

- `journal_pipeline.ipynb` – Interactive notebook to run and explore the pipeline  
- `journal_pipeline.py` – Script version for production workflows  
- `README.md` – This documentation  

## 🔧 Requirements

- Python 3.9+
- A Moorcheh API key (get one at [moorcheh.ai](https://www.moorcheh.ai))  
- Install the integration package:
  ```bash
  pip install langchain-moorcheh

## Running the Pipeline

You can either run the pipeline as a Jupyter notebook or a Python script:

**Notebook:**
```bash
jupyter notebook journal_pipeline.ipynb

