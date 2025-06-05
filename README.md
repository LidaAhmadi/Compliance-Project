# Compliance NLP Project

## Overview

This project explores how natural language processing (NLP) and rule-based techniques can be applied to support compliance and risk review workflows. The goal is to transform large-scale unstructured regulatory text into structured, searchable insights that enable faster decision-making.

## Goals

- Build a prototype pipeline to:
  - Fetch and clean legal and regulatory text data (e.g., court rulings)
  - Apply NLP methods such as NER, embeddings, clustering, and semantic search
  - Evaluate potential use cases for compliance review and automation

## Tech Stack
- **Languages**: Python
- **Libraries**: `pandas`, `re`, `scikit-learn`, `sentence-transformers`, `faiss`, `matplotlib`, `spacy`
- **Tools**: JupyterLab, Git, GitHub
- **Concepts**: Semantic Search, Embeddings, Information Extraction, Clustering, Risk Labeling

## Project Structure

compliance-nlp/
│
├── data/ # Raw and processed text data
├── notebooks/ # Step-by-step development in Jupyter
├── src/ # Modular Python code
│ ├── cleaning.py # Text normalization and cleaning functions
│ ├── embedding.py # Embedding generation
│ ├── search.py # FAISS-based semantic search
│ └── labeling.py # Risk scoring and rule-based classification
├── README.md # Project documentation
└── requirements.txt # Environment setup


## Progress & Roadmap

| Phase                              | Status     |
|-----------------------------------|------------|
| Data fetching (CourtListener)   | Completed  |
| Text cleaning and standardization | In progress |
| Semantic search with SBERT + FAISS | Upcoming |
| Risk labeling (LLM/rule-based)  | Upcoming   |
| Evaluation + Reporting          | Upcoming   |

## Sample Use Case

> Retrieve relevant rulings and risk indicators for a given legal clause (e.g., IRC 482).  
> Return top-matching documents with semantic similarity and assign risk tags based on heuristics or language cues.

## Future Work

- Add LLM prompting and comparison with rule-based methods
- Evaluate outputs using IR metrics (Precision@k, NDCG)
- Build simple Streamlit app for demo interface
- Explore model versioning and MLOps integration




