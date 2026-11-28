# Week 1 — Technology Stack

Only technologies **actually used** in Week 1 are listed as "used". The broader
project stack (from PDF §16) is listed separately as **planned** so nothing is
over‑claimed.

## 1. Used in Week 1 (verified in the repo)

| Technology | Version (verified) | Where | Purpose |
|------------|--------------------|-------|---------|
| Python | 3.11 target (`ruff target-version = py311`; CI `python-version: "3.11"`) | whole week‑1 | Scripting + tooling runtime |
| pytest | `>=8.0,<9.0` (`requirements-dev.txt`) | `tests/` | Unit tests for the validator |
| Ruff | `>=0.6,<1.0` (0.17.6 observed in `.ruff_cache`) | whole week‑1 | Lint + import sorting (`select = E,F,I`, line‑length 100) |
| GitHub Actions | `actions/checkout@v4`, `actions/setup-python@v5` | `.github/workflows/week-1-ci.yml` | CI on push/PR |
| CSV (stdlib `csv`) | Python 3.11 stdlib | validator + register | Read/validate the 17‑column register |
| Git / GitHub | — | repository | Version control, individual `main` workflow |

**Config evidence:** `pyproject.toml` sets pytest `testpaths=["tests"]` and Ruff
`line-length=100`, `target-version="py311"`, `lint.select=["E","F","I"]`.
`requirements.txt` is currently empty (no runtime deps yet — correct for Week 1).

## 2. Dependency policy

- Dev‑only dependencies (pytest, ruff) are pinned with version ranges in
  `requirements-dev.txt`. No runtime/ML dependencies are installed in Week 1 —
  consistent with "no RAG/agent code yet".
- Keep the project on **Python 3.11** unless the internship specifies otherwise.

## 3. Planned stack (PDF §16 — NOT installed in Week 1)

| Layer | Planned choice |
|-------|----------------|
| API | FastAPI + Pydantic v2 + Uvicorn |
| Agent orchestration | LangGraph + LangChain |
| LLM | Gemini or Groq‑hosted model (verify model IDs/limits before use) |
| Embeddings | BAAI/bge‑m3 |
| Reranker | BAAI/bge‑reranker‑v2‑m3 |
| Vector store | ChromaDB (FAISS alternative) |
| Lexical search | rank‑bm25 |
| PDF / OCR | PyMuPDF, pdfplumber, Tesseract 5, OpenCV |
| Computer vision | PyTorch, timm, torchvision, Grad‑CAM |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Evaluation | RAGAS, pytest, scikit‑learn, Locust |
| Observability | structured JSON logs; LangSmith or Langfuse (optional) |
| UI / deploy | Streamlit, Docker, docker‑compose, GitHub Actions |

These arrive in later phases (Ingestion/OCR → Cards → Indexing → RAG → Vision → API/UI),
not Week 1.
