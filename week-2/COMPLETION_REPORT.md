# Week 2 — Completion Report

**Project:** IT Simplera Crop Disease Assistant · **Phase 2 (Days 6–10): Source Collection**
**Date:** 2026‑11‑28 · **Decision: NOT COMPLETE** (register targets met; safety/evidence items blocked on the local machine)

## 1. Requirements checklist (from the internship PDF, §13 Phase 2 / Day‑10 acceptance)

| Day / target | Requirement | Status | Evidence |
|--------------|-------------|--------|----------|
| 6 | Rice T1 collection | ⚠️ PARTIAL | `RICE‑011/012/013` (IRRI×2, PARC); IRRI unreachable to automated fetch, not downloaded |
| 7 | Wheat T1 collection | ⚠️ PARTIAL | `WHEAT‑011/012/013` (CIMMYT×2, FAO) |
| 7 | Cotton T1 collection | ⚠️ PARTIAL | `COTTON‑011/012/013` (CCRI pathology/AR, Sindh Agri) |
| 7 | DPP registered + banned snapshots | ⛔ BLOCKED | list URLs recorded (`GEN‑001/002`, `dpp_snapshot_log.csv`); site blocks automated access; no dated snapshot |
| 8 | T2 research (gap fill) | ⚠️ PARTIAL | leaf/stem rust, loose smut, powdery mildew, boll rot, anthracnose, Myrothecium, cotton root rot — DOIs/records |
| 9 | Dataset inventory | ⚠️ PARTIAL | `datasets/dataset_inventory.csv` (4 datasets, counts pending) + `inspect_datasets.py` + `DATASET_INVENTORY_REPORT.md` |
| 10 | ≥60 sources in register | ✅ COMPLETE | merged register = **61** (validator passes) |
| 10 | ≥3 sources per official disease | ✅ COMPLETE | `reports/disease_source_coverage.csv` — all 18 (range 4–8) |
| 10 | ≥1 Pakistan source per crop | ✅ COMPLETE | rice 13 · wheat 15 · cotton 18 Pakistan‑relevant |
| 10 | SHA‑256 for downloads | ⛔ BLOCKED | nothing downloadable in this environment (HTTP 403) → `fetch_and_hash.py` runs locally |
| 10 | Validator passes | ✅ COMPLETE | ran locally (61) |

## 2. Completed vs pending

**Completed:** register grown to 61 sources mapped to the official `R#/W#/C#` IDs; coverage ≥3/disease; Pakistan coverage per crop; coverage checker + Week‑2 CI; dataset inventory structure + local measuring script; deeper web verification (18 rows `in_review`).

**Pending / blocked (need the local machine or a push):** DPP snapshots; document downloads + hashes; dataset image counts; human verification (`pending`/`in_review` → `verified`); a fresh green Actions run.

## 3. Evidence (numbers)

- **Total unique sources:** 61 (`source_id` unique; dup‑DOI check passes)
- **By ID:** rice 13 · wheat 24 · cotton 19 · cross‑cutting (GEN) 5
- **By tier:** 16 T1 · 45 T2
- **Per official disease:** all 18 ≥3 (range 4–8) — see `reports/disease_source_coverage.csv`
- **Verification:** 18 `in_review` · 43 `pending` · **0 human‑`verified`**
- **Downloads:** 0 · **Hashes:** 0 · **Dataset image counts:** not measured (not invented)

## 4. Testing & validation results (run locally, 2026‑11‑28)

```
week-1: python scripts/validate_source_register.py   → valid (expects 61)   ✅
week-1: pytest                                        → 7 passed             ✅
week-2: python scripts/check_coverage.py              → 61 sources; all 18 ≥3; PK per crop OK   ✅
ruff check week-2/scripts week-2/datasets             → All checks passed!   ✅
```

## 5. Problems & solutions

- **DPP + downloads blocked:** the sandbox proxy returns HTTP 403 for institutional sites and the DPP site blocks automated access (tested, not assumed). **Solution:** recorded exact URLs + provided `fetch_and_hash.py` and `dpp_snapshot_log.csv` to complete on the local machine; nothing faked.
- **Datasets not in repo:** `/Datasets/` is gitignored and the bridge was offline. **Solution:** `inspect_datasets.py` computes real counts locally; inventory left `pending`, counts never invented.
- **Duplicate DOI caught:** the merge guard rejected a powdery‑mildew paper already present as `WHEAT‑004`; it was dropped.

## 6. Final completion decision

**Week 2 = NOT COMPLETE.** The register‑level Day‑10 acceptance criteria (≥60 sources, ≥3/disease, Pakistan per crop, validator green) are genuinely met and proven. DPP snapshots, downloads + hashes, dataset counts, human verification, and a live CI run remain — all require the local machine or a push.
