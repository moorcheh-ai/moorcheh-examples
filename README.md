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
| `upcoming` | Other examples such as healthcare, legal are in progress     |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/moorcheh-ai/moorcheh_examples.git
cd moorcheh_examples
```

### 2. Set Up Environment

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your Moorcheh API key:

```bash
export MOORCHEH_API_KEY="your_api_key_here"
```

### 3. Run an Example

```bash
cd finance
python demo.py
```

>  Most examples are designed to work in both local environments and Google Colab.

---

## Benchmarking

Check out our [benchmarking github]((https://github.com/moorcheh-ai/moorcheh-benchmarks)) and the [discussion post](https://github.com/moorcheh-ai/moorcheh-benchmarks/discussions/3) on how Moorcheh compares with other vector databases across metrics like relevance, context completeness, and response depth.

---
