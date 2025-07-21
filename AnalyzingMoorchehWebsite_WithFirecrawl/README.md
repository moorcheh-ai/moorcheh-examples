# AI Hub: Semantic Website Search with Moorcheh

This example demonstrates how to build a **Retrieval-Augmented Generation (RAG)** pipeline to search and answer questions over websites using **firecrawl** and **moorcheh**.

## Key Features

- Uses **firecrawl** for web scraping
- Uses **Moorcheh's API** for embedding, storage, and retrieval  
- Clean ingestion and simple pipeline 
  
## Files Included

- `moorchehwebsite.ipynb` – Notebook version of the pipeline
- `moorchehwebsite.py` –  Python Script version 
- `queries.txt` – Example legal queries
- `README.md` – This file

## Requirements

- Python 3.9+
- Moorcheh API Key (get one at [moorcheh.ai](https://www.moorcheh.ai))
- Firecrawl API Key

## Running the Pipeline

You can either run the pipeline as a Jupyter notebook or a Python script:

**Notebook:**
```bash
jupyter notebook moorchehwebsite.py 
