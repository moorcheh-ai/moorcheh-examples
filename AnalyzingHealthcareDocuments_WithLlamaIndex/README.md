# AI Diagnostic: Semantic Healthcare Search with Moorcheh

This example showcases how to build a **Retrieval-Augmented Generation (RAG)** pipeline using **Moorcheh** to perform semantic search and AI-powered answering over healthcare reports and articles.

----

## Demo Video

Watch the full walkthrough on YouTube:  
🔗 [Healthcare RAG Demo](https://www.youtube.com/watch?v=9J9RLbm6I5s)

## Key Features

- Uses **Moorcheh's API** for embedding, storage, and retrieval
- Integrated with **LlamaIndex** for document parsing
- Focused on medical documents for question answering
- Clean ingestion pipeline and reproducible queries

## Included in this example

- `healthcare_pipeline.ipynb`: Notebook version of the pipeline
- `healthcare_pipeline.py`: Script version for production use
- `queries.txt`: Sample medical queries
- `README.md`: This file

## Requirements

Make sure you have:
- Python 3.9+
- A Moorcheh API key (sign up at [moorcheh.ai](https://www.moorcheh.ai))

## Running the Pipeline

You can either run the pipeline as a Jupyter notebook or a python script:

**Notebook:**
```bash
jupyter notebook healthcare_pipeline.ipynb 
