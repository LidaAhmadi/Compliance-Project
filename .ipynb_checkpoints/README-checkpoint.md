# Compliance NLP Project

This project explores retrieval and classification techniques for legal compliance using real-world rulings from the [CourtListener API](https://www.courtlistener.com/).

## Dataset

We query legal opinions that mention **"tax"** or **"fraud"** using their REST API.  
Only rulings with usable full text are saved to `data/raw/`.

Script: `notebooks/01_fetch_opinions.ipynb`  
Config: `config.py` (holds API key, search term, number of pages, etc.)

## To Extend

To fetch more data, increase `MAX_PAGES` in `config.py` and re-run the notebook.
