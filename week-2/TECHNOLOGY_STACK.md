# Week 2 — Technology Stack

Only what Week 2 **actually used** is listed as "used". The ingestion/RAG stack the
Week‑2 sources are *collected for* is listed separately as **planned** (PDF §16).

## 1. Used in Week 2 (verified)

| Technology | Version | Where | Purpose |
|------------|---------|-------|---------|
| Python | 3.11 target | `week-2/scripts/`, `week-2/datasets/`, `week-2/fetch_and_hash.py` | All Week‑2 scripts |
| Python stdlib `csv` | 3.11 | `check_coverage.py`, inventory | Read register / write coverage matrix |
| Python stdlib `re` | 3.11 | `check_coverage.py` | Map disease names + IDs to the official 18 |
| Python stdlib `hashlib` | 3.11 | `inspect_datasets.py`, `fetch_and_hash.py` | SHA‑256 / duplicate detection |
| Python stdlib `urllib` | 3.11 | `fetch_and_hash.py` | Download permitted documents (run locally) |
| Ruff | `>=0.6,<1.0` | week‑2 scripts | Lint (passes) |
| pytest | `>=8.0,<9.0` | shared (week‑1 suite) | Tests |
| GitHub Actions | checkout@v4, setup-python@v5 | `.github/workflows/week-2-ci.yml` | CI: validator + coverage gate + ruff |
| Git / GitHub (anonymous read) | — | repo | Inspect + sync the repository |

**No third‑party runtime libraries** were added in Week 2 — every script is pure
Python standard library. This keeps the collection tooling dependency‑free and easy to
run on the developer's machine.

> Note: during research, publisher/DOI metadata was confirmed via web search and
> academic indexes (Crossref/AGRIS/PubMed Central/publisher pages). Those are research
> actions, not project dependencies.

## 2. Planned ingestion / RAG stack (PDF §16 — NOT used in Week 2)

These are the technologies the collected sources will feed into in later phases:

| Layer | Planned choice | Phase |
|-------|----------------|-------|
| PDF / OCR | PyMuPDF, pdfplumber, Tesseract 5, OpenCV | 3 (Extraction & OCR) |
| Knowledge cards | JSON schema + validator | 4 |
| Embeddings / vector store | BAAI/bge‑m3 · ChromaDB (FAISS alt) | 5 |
| Lexical search | rank‑bm25 | 5 |
| Reranker | BAAI/bge‑reranker‑v2‑m3 | 6 |
| Agent / LLM | LangGraph + LangChain · Gemini or Groq | 6 |
| API / UI | FastAPI + Pydantic v2 + Uvicorn · Streamlit · Docker | 7/9 |
| Database | SQLite (dev) / PostgreSQL (prod) | 6+ |
| Evaluation | RAGAS, scikit‑learn, Locust | 8 |

## 3. Dependency policy for Week 2

- Keep scripts **standard‑library only** so they run anywhere with Python 3.11.
- Pin any future ingestion libraries in `week-1/requirements.txt` (currently empty) or
  a dedicated `requirements.txt` when Phase 3 begins.
- Verify LLM/model IDs, limits and costs before adopting them (PDF §16 note).
