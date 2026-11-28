# Week 1 Architecture

## Scope
Week 1 implements the research-evidence and quality-control foundation. The crop-disease assistant, retrieval pipeline, agents, image model, API, and UI are future work, not Week 1 implementations.

## Implemented components

| Component | Responsibility | Status |
|---|---|---|
| `knowledge/source_register.csv` | Canonical 17-column research source ledger | Implemented |
| `scripts/validate_source_register.py` | Checks schema, required values, unique IDs/DOIs, tiers, statuses, and expected total | Implemented |
| `tests/test_source_register.py` | Unit tests for validation rules | Implemented |
| `../.github/workflows/week-1-ci.yml` | Runs register validation, pytest, and Ruff | Implemented |

## Data flow

```mermaid
flowchart LR
 A[Research source identified] --> B[source_register.csv]
 B --> C[Python validator]
 C --> D[pytest]
 D --> E[Ruff]
 E --> F[GitHub Actions]
 F --> G[Structurally valid register]
```

A green validation result confirms data structure and configured checks only. It does not prove that a publication exists, that its metadata is accurate, or that its licence permits reuse. Those require human verification.

## Planned full system

The internship's later architecture includes source ingestion/OCR, disease knowledge cards, hybrid retrieval, evidence checks, a chemical-safety gate, agent orchestration, and an interface. These are not claimed as implemented in Week 1.
