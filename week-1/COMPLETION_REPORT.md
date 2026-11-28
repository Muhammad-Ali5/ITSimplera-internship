# Week 1 — Completion Report

**Project:** IT Simplera Crop Disease Assistant · **Phase 1 (Days 1–5): Planning & Sources**
**Date:** 2026‑11‑28 · **Decision: NOT COMPLETE** (foundation + CI done; source verification pending)

## 1. Requirements checklist (from the internship PDF, §13 Phase 1 / Week‑1 acceptance)

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 1 | GitHub repo + individual workflow documented | ✅ COMPLETE | `README.md`, `CONTRIBUTING.md` (solo workflow, `main` branch, no fake team) |
| 2 | Project folder structure | ✅ COMPLETE | `.github/`, `week-1/` (knowledge, scripts, tests), `week-2..8/`, `/Datasets/` gitignored |
| 3 | Contribution guide | ✅ COMPLETE | `CONTRIBUTING.md` |
| 4 | Automated quality checks (lint + tests + validator) | ✅ COMPLETE | `.github/workflows/week-1-ci.yml`; ran locally — see §3 |
| 5 | Source‑register validator works | ✅ COMPLETE | `scripts/validate_source_register.py` + `tests/test_source_register.py` |
| 6 | ≥30 genuine sources with licence/access | ⚠️ PARTIAL | `knowledge/source_register.csv` (30 at Day‑5 checkpoint; now 61 cumulative) — all `pending`/`in_review`, none human‑`verified` |
| 7 | Successful GitHub Actions run, with evidence | ✅ COMPLETE (documented) | Run link recorded in `README.md` §7 (`actions/runs/46041173236`); re‑run needed after the Week‑2 register merge |

## 2. Completed vs pending

**Completed:** repository + individual workflow, folder structure, contribution guide, the 17‑column register schema, the Python validator, the pytest suite, the GitHub Actions workflow, and a documented green CI run.

**Pending:** human verification of every source (identity, relevance to the official 18, licence/access) — all rows remain `pending`/`in_review`; and a fresh CI run after the register grew from 30 → 61 in Week 2.

## 3. Testing & validation results (run locally, 2026‑11‑28)

```
python scripts/validate_source_register.py   → "structure and populated rows are valid" (expects 61)   ✅
pytest                                        → 7 passed                                                ✅
ruff check .                                  → All checks passed!                                       ✅
```

The validator confirms: 17 required columns, unique `source_id`, no duplicate DOI, required fields populated, tier ∈ {T1..T4}, status ∈ {pending, in_review, verified, rejected}, and the expected row count. It does **not** prove a paper exists or that its licence permits reuse — that is human review.

## 4. Problems & solutions

- **Scope mismatch:** the original 30 sources used a disease taxonomy that didn't match the official 18 (Fusarium Head Blight, Septoria, cotton Fusarium/Verticillium Wilt, Alternaria). **Solution:** kept those 7 as retained extra sources and added Week‑2 sources mapped to the official `R#/W#/C#` IDs; coverage now ≥3 per official disease.
- **Validator hard‑coded 30:** growing the register would fail CI. **Solution:** updated `expected_count` to the cumulative total (61); validator + tests + ruff still pass.
- **No fabrication:** where a source couldn't be fully confirmed it is marked `pending` with a note, never invented.

## 5. Final completion decision

**Week 1 = NOT COMPLETE.** The software/documentation foundation and automated checks are genuinely in place and pass, and a green CI run is documented. The remaining acceptance work is **source‑by‑source human verification** (and a re‑run of CI against the merged 61‑row register). No mandatory item was faked or skipped.
