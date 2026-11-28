# Week 1 — Audit Report

**Date:** 2026‑11‑28 · **Auditor:** AI‑assisted, against the real repo at commit `388570d`
**Method:** cloned `Muhammad-Ali5/ITSimplera-internship`, read actual files, ran the checks locally.
**Statuses:** COMPLETE · PARTIAL · MISSING · NEEDS VERIFICATION · BLOCKED

> A task is never COMPLETE just because a file exists. "COMPLETE" below means the
> file exists **and** its content was read and (where runnable) executed here.

## Requirement → evidence → status

| # | Requirement (Week 1) | Evidence found | Status |
|---|----------------------|----------------|--------|
| 1 | GitHub repo + individual workflow documented | `week-1/README.md` (§ workflow), `week-1/CONTRIBUTING.md` ("maintained by one intern; use `main`"). No fake team. | **COMPLETE** |
| 2 | Project folder structure | `.github/`, `week-1/`…`week-8/`, `/Datasets/` gitignored, `.gitignore` sound | **COMPLETE** |
| 3 | Contribution/development guide | `week-1/CONTRIBUTING.md` — env setup, checks, source rules, commit conventions, safety rules | **COMPLETE** |
| 4 | Automated quality checks | `.github/workflows/week-1-ci.yml` runs on push/PR, Python 3.11, installs `requirements-dev.txt`, validates register, `pytest`, `ruff`. Ran locally: validator ✅, **pytest 7 passed**, **ruff all checks passed** | **COMPLETE (local)** |
| 5 | Source‑register validator works | `week-1/scripts/validate_source_register.py` (columns, dup `source_id`, dup DOI, tier/status enums, count). Ran locally ✅ | **COMPLETE** |
| 6 | ≥30 genuine sources with licence/access | `week-1/knowledge/source_register.csv` = **30 rows**, all 17 columns incl. `licence`, `verification_status` | **PARTIAL** |
| 7 | Required GitHub Actions run succeeds, with evidence | CI workflow exists; a successful run is **documented** in `week-1/README.md` §7 (`actions/runs/46041173236`). Not independently re‑fetched here (no auth); a re‑run is needed after the 61‑row merge | **COMPLETE (documented) · re‑run pending** |

## Why #6 is PARTIAL (not COMPLETE)

- All **30 rows are `verification_status: pending`** — none independently human‑verified. The brief treats pending sources as not fully verified. To close: open each `url_or_doi`, confirm identity/relevance/licence, set `verified`.
- **Scope mismatch (important):** the 30 rows use an **old disease taxonomy** that does not match the official 18. 7 rows are for diseases **outside** the official list — `WHEAT-006` (Fusarium Head Blight), `WHEAT-009` (Septoria), `COTTON-004/005` (Fusarium Wilt), `COTTON-006/007` (Verticillium Wilt), `COTTON-010` (Alternaria). They are **retained** (not deleted — they're genuine sources) but don't count toward official‑disease coverage. See `week-2/AUDIT_REPORT.md` for the reconciled register.

## Fixes applied in this pass (delivered, not pushed)

- Merged register to **61 rows** (Week‑2 sources added; the 30 originals preserved byte‑for‑byte). The validator's expected count was updated 30 → **61**; validator + pytest + ruff still pass locally.
- No Week‑1 file was deleted. The only Week‑1 edit is the validator's `expected_count` (30→61) so CI stays green against the grown register.

## Week 1 — audit verdict

Foundation is **solid and real** (structure, workflow docs, validator, tests, CI config all present and runnable). Two things keep Week 1 short of fully signed‑off: **(a)** every source is still `pending` human verification, and **(b)** no successful GitHub Actions run could be observed from here. Neither is fabricated‑away.
