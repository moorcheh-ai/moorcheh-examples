# AI Analyst: Semantic Finance Search with Moorcheh

This example showcases how to build a **Retrieval-Augmented Generation (RAG)** pipeline for financial reports and earnings transcripts using **Moorcheh** as the vector store and **Langchain** for document ingestion and querying.

The pipeline enables semantic search and AI-powered answering over company earnings, financial trends, and stock market insights — all in a single API call using Moorcheh.

## 🎥 Demo Video

Watch the full demo here:  
🔗 [AI Analyst: Finance RAG Demo](https://www.youtube.com/watch?v=s0IBq8rnuqM)

## 📌 Key Features

- Uses **Moorcheh's API** for embedding, storage, and retrieval  
- Focused on financial documents for question answering  
- Clean ingestion pipeline and reproducible queries  
- Demonstrates RAG using only **one API call** 

## 🗂️ Included in this example

- `finance_pipeline.ipynb` – Notebook version of the pipeline  
- `finance_pipeline.py` – Script version for production use  
- `queries.txt` – Sample financial queries  
- `README.md` – This file

## 🛠️ Requirements

Make sure you have:
- Python 3.9+
- A Moorcheh API key (sign up at [moorcheh.ai](https://www.moorcheh.ai))

## 🚀 Running the Pipeline

You can either run the pipeline as a Jupyter notebook or a Python script:

**Notebook:**
```bash
jupyter notebook finance_pipeline.ipynb
