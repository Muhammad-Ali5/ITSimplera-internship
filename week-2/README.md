# Week 2 — Source Collection & Audit (Days 6–10)

IT Simplera Crop Disease Assistant · rice · wheat · cotton · 18 official diseases
**Updated:** 2026‑11‑28 · **Status:** register targets met; safety/evidence items blocked on your machine (**NOT COMPLETE**)

**Objective (PDF §13 Phase 2):** collect, verify, organise and document authoritative
knowledge for all 18 diseases; Day‑10 target ≥60 registered sources, ≥3 per disease,
≥1 Pakistan source per crop.

## Week 2 documentation

- [COMPLETION_REPORT.md](COMPLETION_REPORT.md) — requirements checklist, evidence, decision
- [ARCHITECTURE.md](ARCHITECTURE.md) — collection/verification pipeline + planned RAG feed
- [TECHNOLOGY_STACK.md](TECHNOLOGY_STACK.md) — tools used vs planned
- [AUDIT_REPORT.md](AUDIT_REPORT.md) — requirements → evidence → status
- [reports/disease_source_coverage.csv](reports/disease_source_coverage.csv) — coverage matrix
- [datasets/DATASET_INVENTORY_REPORT.md](datasets/DATASET_INVENTORY_REPORT.md) — Day 9 dataset inventory

## What changed in this completion pass

- Canonical register merged to **61 sources** (`week-1/knowledge/source_register.csv`) — the 30 originals preserved; 31 genuine Week‑2 sources added and mapped to the official IDs **R1–R6, W1–W6, C1–C6**.
- Verification deepened by web search: **18 rows `in_review`** (DOI/journal/metadata confirmed this session), 43 `pending`, 0 human‑`verified` yet.
- Validator updated to expect 61; **validator + pytest (7) + ruff all pass locally**.
- New: `COMPLETION_REPORT.md`, `ARCHITECTURE.md`, `TECHNOLOGY_STACK.md`, `AUDIT_REPORT.md`, `reports/disease_source_coverage.csv` (all 18 ≥3), `scripts/check_coverage.py`, `datasets/inspect_datasets.py`, `datasets/DATASET_INVENTORY_REPORT.md`, `hashes/SHA256SUMS.csv`, and `.github/workflows/week-2-ci.yml`.

## Day‑10 targets (proven by `scripts/check_coverage.py`)

| Target | Result |
|--------|--------|
| ≥60 unique sources | **61** ✅ |
| ≥3 sources per official disease | all 18, range **3–8** ✅ |
| ≥1 Pakistan source per crop | rice 9 · wheat 9 · cotton 11 ✅ |
| Register validator passes | ✅ (local) |

## Still blocked on your machine (why Week 2 isn't "complete")

1. **DPP registered + banned pesticide snapshots** — URLs recorded (`GEN‑001/002`, `dpp_snapshot_log.csv`); site unreachable here, no dated snapshot yet. **Top priority (chemical‑safety gate).**
2. **Document downloads + SHA‑256** — run `fetch_and_hash.py`; `hashes/SHA256SUMS.csv` is header‑only until then.
3. **Dataset image counts** — `/Datasets/` is gitignored + bridge offline; run `datasets/inspect_datasets.py` to fill real counts (none invented).
4. **Human verification** — all 61 rows are `pending`/`in_review`; open each DOI/URL and promote to `verified`.
5. **Green GitHub Actions run** — can't push/verify from here.

## Folder map (Week 2)

```
week-2/
├── README.md  ·  AUDIT_REPORT.md
├── DAY6_RICE_COLLECTION.md · DAY7_WHEAT_COTTON_DPP.md · DAY8_T2_RESEARCH.md · WEEK2_PROGRESS.md
├── week2_source_register_additions.csv   (now superseded by the merged canonical register)
├── source_collection_log.csv · dpp_snapshot_log.csv
├── scripts/check_coverage.py             (Week-2 CI coverage gate)
├── datasets/  dataset_inventory.csv · inspect_datasets.py · DATASET_INVENTORY_REPORT.md
├── COMPLETION_REPORT.md · ARCHITECTURE.md · TECHNOLOGY_STACK.md · AUDIT_REPORT.md
├── reports/   disease_source_coverage.csv
├── hashes/    SHA256SUMS.csv              (header only until fetch_and_hash.py runs)
└── fetch_and_hash.py
```

## Non‑negotiables honoured
No invented papers, authors, DOIs, licences, hashes or image counts. 0 sources marked `verified`. Viral diseases (R6, C1) flagged "no fungicide/bactericide cure". No pesticide names/doses invented. Week‑1 rows preserved; Week‑3+ untouched; the four datasets untouched.
