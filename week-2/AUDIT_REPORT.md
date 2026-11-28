# Week 2 — Audit Report

**Date:** 2026‑11‑28 · **Auditor:** AI‑assisted, against the real repo at commit `388570d`
**Statuses:** COMPLETE · PARTIAL · MISSING · NEEDS VERIFICATION · BLOCKED

## What already existed in `week-2/` (before this pass)

Real work was already present and was **read, not assumed**:
`DAY6_RICE_COLLECTION.md`, `DAY7_WHEAT_COTTON_DPP.md`, `DAY8_T2_RESEARCH.md`,
`README.md`, `WEEK2_PROGRESS.md`, `SHA256SUMS.csv`, `week2_source_register_additions.csv`,
`dataset_inventory.csv`, `dpp_snapshot_log.csv`, `source_collection_log.csv`,
`fetch_and_hash.py`. The `source_collection_log.csv` held 8 genuine T1 leads you
recorded (IRRI, CIMMYT field guide, CCRI pathology, CCRI AR, DPP registered/banned,
Punjab forecasting) — these were folded into the merged register.

## Requirement → evidence → status

| Day | Requirement | Evidence | Status |
|-----|-------------|----------|--------|
| 6 | Rice T1 collection documented | `DAY6_RICE_COLLECTION.md`; register `RICE‑011/012/013` (IRRI×2, PARC) | **PARTIAL** |
| 7 | Wheat T1 collection | register `WHEAT‑011/012/013` (CIMMYT×2, FAO) | **PARTIAL** |
| 7 | Cotton T1 collection | register `COTTON‑011/012/013` (CCRI pathology, CCRI AR, Sindh Agri) | **PARTIAL** |
| 7 | DPP registered + banned pesticide snapshots | `dpp_snapshot_log.csv` + register `GEN‑001/002` have the exact list URLs; **no snapshot captured** | **BLOCKED** |
| 8 | T2 research papers (gap fill) | register adds leaf rust, stem rust, loose smut, powdery mildew, boll rot, anthracnose, Myrothecium, cotton root rot (PK) — with DOIs/records | **PARTIAL** |
| 9 | Dataset inventory | `datasets/dataset_inventory.csv` (4 datasets, counts `pending`) + `inspect_datasets.py` + `DATASET_INVENTORY_REPORT.md` | **PARTIAL** |
| 10 | ≥60 sources in register | merged register = **61 rows** (validator passes at 61) | **COMPLETE** |
| 10 | ≥3 sources per official disease | `reports/disease_source_coverage.csv` — **all 18 ≥3** | **COMPLETE** |
| 10 | ≥1 Pakistan source per crop | rice 9, wheat 9, cotton 11 Pakistan‑specific | **COMPLETE** |
| 10 | SHA‑256 records for downloads | `hashes/SHA256SUMS.csv` header only — **nothing downloaded here** | **BLOCKED** |
| 10 | Validator passes | ran locally ✅ (61 rows) | **COMPLETE** |

## Why the PARTIAL / BLOCKED items are not COMPLETE

- **Days 6–8 PARTIAL:** sources are registered with real URLs/DOIs, but most are `pending`/`in_review` — not human‑verified — and **no institutional PDFs were downloaded** (this sandbox's network reaches only package registries; the bridge to `E:\` was offline). Downloads + hashes must run on your machine (`fetch_and_hash.py`).
- **DPP BLOCKED:** `plantprotection.gov.pk` could not be fetched here. The exact registered/banned list URLs are recorded, but a **dated snapshot does not yet exist**. This is the top safety item.
- **Day 9 PARTIAL:** `/Datasets/` is gitignored and the bridge was offline, so **image counts could not be measured** and were **not invented**. `inspect_datasets.py` fills them locally.
- **SHA‑256 BLOCKED:** depends on downloads, which depend on your machine.

## Day‑10 numbers (from the delivered register)

- **Total sources:** 61 unique (`source_id` unique; dup‑DOI check passes).
- **Per official disease:** all 18 have ≥3 (range 4–8). See coverage CSV.
- **Pakistan‑relevant (by crop):** rice 13 · wheat 15 · cotton 18.
- **Tiers:** 16 T1 · 45 T2; 7 non‑official‑scope sources retained from Week 1.
- **Verification:** 18 `in_review` (DOI/journal/metadata confirmed via web search this session) · 43 `pending` · **0 `verified`** (no human sign‑off yet).

## Week 2 — audit verdict

The **register‑level Day‑10 targets are genuinely met** (61 sources, ≥3/disease, Pakistan per crop) and the validator proves it. **But Week 2 is not fully complete**: DPP snapshots, document downloads + hashes, and dataset image counts are all **blocked on your machine**, and no source is human‑verified yet.
