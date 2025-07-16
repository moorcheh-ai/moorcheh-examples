# Moorcheh Examples

This repository showcases real-world examples of how to build Retrieval-Augmented Generation (RAG) pipelines using [Moorcheh](https://github.com/mjfekri/moorcheh-python-sdk) — a powerful semantic vector store designed for high-performance document retrieval and contextual AI applications.

---

## What’s Inside

Each folder contains a full example pipeline, complete with:

- Preloaded datasets  & queries 
- Code to upload and index documents into Moorcheh
- Semantic queries and retrieval logic
- Output analysis and results

---

## Use Cases

| Folder       | Description                                                                            |
|--------------|----------------------------------------------------------------------------------------|
| `finance`    | Semantic search over quarterly earnings reports and transcripts from major tech firms |
| `healthcare` | Semantic search over clinical and scientific documents related to diseases  |
| `legal` | Semantic search over legal documents and reports  |
| `upcoming` | Other examples such as education, geographical are in progress     |

You can watch all our example demos here:  
🔗 [Moorcheh YouTube Channel](https://www.youtube.com/@moorchehai/videos)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/moorcheh-ai/moorcheh_examples.git
cd moorcheh_examples
```

### 2. Set Up Environment

Set your OPENAI API Key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Set your Moorcheh API key:

```bash
export MOORCHEH_API_KEY="your_api_key_here"
```

### 3. Run an Example

Before running the demo, make sure to upload your own document set (PDFs, text files, or markdown) into the designated folder—usually ./documents/—and your queries in CSV format (with a query column) into ./queries/.

```bash
cd AnalyzingFinancialDocuments_WithLangChain
python demo.py
```

>  Most examples are designed to work in both local environments and Google Colab. Within each folder, you will also find videos about each topic to guide you through the process as well. 

---

## Benchmarking

Check out our [benchmarking github]((https://github.com/moorcheh-ai/moorcheh-benchmarks)) and the [discussion post](https://github.com/moorcheh-ai/moorcheh-benchmarks/discussions/3) on how Moorcheh compares with other vector databases across metrics like relevance, context completeness, and response depth.

---
