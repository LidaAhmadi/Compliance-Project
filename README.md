
#  Compliance NLP Project

This project builds a prototype search tool that retrieves real-world legal rulings related to tax and fraud.  
The goal is to help compliance analysts, auditors, or legal researchers find relevant court rulings  
that inform risk assessments and audits.

---

##  Dataset

We sourced legal opinions using the [CourtListener API](https://www.courtlistener.com/), a public legal database.

- Queried rulings that mention **"tax"** or **"fraud"**
- Filtered for documents with usable full text
- Saved results as `.txt` files in `data/raw/`

Scripts:
- Data fetch: `notebooks/01_fetch_opinions.ipynb`
- Config: `config.py` (stores API key, search query, output paths, etc.)

---

##  To Extend

To fetch more rulings:
1. Increase `MAX_PAGES` in `config.py`
2. Re-run the fetch notebook to save additional `.txt` files

Coming next:
- Text cleaning and preprocessing
- Embedding and retrieval via Sentence-BERT or TF-IDF
- Optional: risk labeling and summarization
