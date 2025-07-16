# AI LegalSight: Semantic Legal Search with Moorcheh

This example demonstrates how to build a **Retrieval-Augmented Generation (RAG)** pipeline to search and answer questions over legal documents — specifically the **Canadian Copyright Act (R.S.C., 1985, c. C-42)** — using **Moorcheh** as the vector database and **LlamaIndex** for document ingestion and querying.

The goal is to showcase how Moorcheh can power legal information retrieval using semantic understanding, all with a single API call.

## Demo Video

Watch the full walkthrough on YouTube:  
🔗 [AI LegalSight: Legal RAG Demo](https://www.youtube.com/watch?v=ikOHQKmaNeU&t=2s)

## Key Features

- Uses **Moorcheh's API** for embedding, storage, and retrieval  
- Fully integrated with **LlamaIndex**  
- Focused on legal documents for question answering  
- Clean ingestion pipeline and reproducible queries  
- Demonstrates RAG using only **one API key** (Moorcheh)
- 
## Files Included

- `legal_pipeline.ipynb` – Notebook version of the pipeline
- `legal_pipeline.py` –  Python Script version 
- `queries.txt` – Example legal queries
- `README.md` – This file

## Requirements

- Python 3.9+
- Moorcheh API Key (get one at [moorcheh.ai](https://www.moorcheh.ai))

## Running the Pipeline

You can either run the pipeline as a Jupyter notebook or a Python script:

**Notebook:**
```bash
jupyter notebook legal_pipeline.ipynb
