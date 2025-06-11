# Overview

This project applies natural language processing (NLP), semantic search, and rule-based techniques to support real-world compliance and risk review workflows.

Inspired by challenges encountered in my professional role at the IRS, it transforms large-scale unstructured legal and regulatory texts into structured, searchable insights for faster, more informed decision-making. Built independently using public data, the project demonstrates practical methods for identifying relevant cases, surfacing risk signals, and supporting auditable analysis pipelines.

# Goals

Build a prototype pipeline to:

- Fetch and clean legal and regulatory text data (e.g., court rulings)  
- Apply NLP methods such as NER, embeddings, semantic search, and rule-based labeling  
- Evaluate retrieval quality using IR metrics such as Precision@k and NDCG  
- Evaluate potential use cases for compliance review and automation

# Tech Stack

- **Languages**: Python  
- **Libraries**: `pandas`, `re`, `scikit-learn`, `sentence-transformers`, `faiss`, `matplotlib`, `spacy`  
- **Tools**: JupyterLab, Git, GitHub  
- **Concepts**: Semantic Search, Embeddings, Information Extraction, Risk Labeling, Evaluation Metrics

# Data Source

The data used in this project comes from [CourtListener](https://www.courtlistener.com/), an open-access repository of legal opinions maintained by the Free Law Project. CourtListener provides bulk downloads and APIs containing court rulings from U.S. federal and state courts, including appellate decisions with full-text legal opinions.

# Project Structure
```
compliance-nlp/
│
├── data/                                # Raw and processed text data
│   ├── raw/                             # Unprocessed fetched files (raw txt)
│   └── clean/                           # Cleaned and normalized texts
│
├── notebooks/                           # Jupyter notebooks for exploration and prototyping
│   ├── 01_fetch_opinions.ipynb          # Fetch and store rulings from CourtListener's API 
│   ├── 02_load_and_clean_rulings.ipynb  # Clean and normalize text for further processing
│   ├── 03_semantic_search.ipynb         # Perform similarity search using embeddings + FAISS
│   └── 04_label_and_review.ipynb        # Risk labeling via rule-based or semantic classification
├── src/                                 # Modular Python code
│
├── README.md                            # Project documentation
├── config.py                            # Configuration 
├── requirements.txt                     # Environment setup
└── .gitignore                           # Files and folders to exclude from Git
```
# Progress & Roadmap

| Phase                                              | Status     |
|---------------------------------------------------|------------|
| Data fetching (CourtListener)                     | Completed |
| Text cleaning and standardization                 | Completed |
| Semantic search with SBERT + FAISS                | Completed|
| Risk labeling (rule-based and LLM-assisted)       | Upcoming |
| Evaluation (Precision@k, NDCG) + Output Reporting | Upcoming |

# Sample Use Case

Retrieve relevant rulings and risk indicators for a given legal clause.  
Return top-matching documents with semantic similarity and assign risk tags based on heuristics or language cues.

# Understanding Ruling Structure

The court rulings retrieved from CourtListener follow a semi-structured format. Each ruling typically includes:

- **Metadata**: Case name, date, court, docket number, and legal representatives  
- **Procedural Context**: Explanation of how the case arrived at the court (e.g., appeals, motions)  
- **Decision and Order**: The court’s final ruling and legal reasoning  
- **Legal Citations**: References to relevant statutes and past cases

# Example Cleaned Ruling (Preview)

> **Pantanilla v Yuson (2025 NY Slip Op 02597)**  
> Decided on April 30, 2025  
> Appellate Division, Second Department  
> In an action to recover damages for unjust enrichment, the plaintiff alleged an agreement to purchase a business and partial payments made. The defendant rescinded the agreement without refunding the payments. A default judgment was entered in favor of the plaintiff for $40,000. The court affirmed the judgment.

# Future Work

- Add LLM-based prompting and comparison with rule-based methods  
- Evaluate outputs using IR metrics (Precision@k, NDCG)  
- Build simple Streamlit app for demo interface  
- Explore model versioning and MLOps integration

---

> *This project is conducted in a personal capacity using only public data. It does not reflect the views or data of the IRS.*
