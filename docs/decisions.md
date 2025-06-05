# Technical Decisions and Justifications

## 1. Tokenization and Preprocessing

### Decision
I used built-in tokenization provided by:
- `TfidfVectorizer` (scikit-learn) for word-level retrieval
- `sentence-transformers` (planned) for semantic embeddings

### Rationale
- Both libraries include reliable tokenization and normalization steps (lowercasing, stopword removal, etc.).
- I considered adding custom tokenization, but it wasn't blocking quality or usability at this stage.
- This let me focus on higher-impact steps like embedding, retrieval, and evaluation.

### Interview-Ready Talking Point
> "I used proven, off-the-shelf tokenizers to balance speed and quality, ensuring I could focus on building a usable retrieval pipeline."

---

## 2. Search Strategy (TF-IDF First)

### Decision
I started with **TF-IDF** for baseline retrieval.

### Rationale
- It’s lightweight, interpretable, and fast to implement.
- Provides a good baseline to compare against more advanced methods like Sentence-BERT.
- Helps explain trade-offs between **word-based vs. semantic retrieval** in interviews.

### Interview-Ready Talking Point
> "Starting with TF-IDF gave me a fast baseline to test the retrieval pipeline before introducing heavier semantic models."

---

More decisions will be added as the project evolves.
