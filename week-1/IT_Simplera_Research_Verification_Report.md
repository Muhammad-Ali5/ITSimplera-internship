# IT Simplera Crop Disease Assistant — Research Verification Report

**Deliverable:** Week-1 research source set (30 publications)
**Crops:** Rice, Wheat, Cotton (18 diseases, 6 per crop)
**Research date:** 2026-11-27
**Prepared by:** AI-assisted literature research — **requires human verification before use**
**Companion file:** `IT_Simplera_Week1_30_Research_Sources.csv`

---

## 1. Honesty & method statement

Every record was located through live searches of academic databases and publisher sites (PubMed Central, Crossref/DOAJ, Frontiers, MDPI, Springer, Wiley, Elsevier, APS, AGRIS). Titles, journals, years and DOIs/URLs were read from the returned records.

- **No paper, author, DOI, year, licence or page number was invented.** Where a field could not be confirmed from the retrieved record it is written as `Not verified` or flagged in `notes` — rather than guessed.
- **`verification_status` = `pending` for all 30 rows.** No human has yet independently opened each DOI to confirm it resolves to the stated article. A reviewer should click every `url_or_doi` before the set is treated as final.
- **Known items still needing a human check** (see §6): one inferred DOI (Azzam & Chancellor 2002, APS pattern), several `Not verified` author lists, and all licences marked "confirm".

## 2. Totals

| Metric | Value |
|---|---:|
| Publications researched / delivered | 30 |
| Rice | 10 |
| Wheat | 10 |
| Cotton | 10 |
| Peer-reviewed (Tier 2) | 28 |
| Official technical guides (Tier 1) | 2 |
| Open-access (CC BY / CC BY-NC, stated) | 22 |
| Subscription / licence unconfirmed | 8 |
| Explicitly Pakistan-focused studies | 6 |
| Pakistan-relevant (South-Asia / CIMMYT / PK co-authors) | +3 |

## 3. Papers by crop and disease (coverage matrix)

All 18 required diseases have at least one source.

| Crop | Disease | Source IDs | # |
|---|---|---|---:|
| Rice | Rice Blast | RICE-001, RICE-002 | 2 |
| Rice | Bacterial Leaf Blight | RICE-003 | 1 |
| Rice | Sheath Blight | RICE-004, RICE-005 | 2 |
| Rice | Brown Spot | RICE-006, RICE-007 | 2 |
| Rice | False Smut | RICE-008 | 1 |
| Rice | Rice Tungro | RICE-009, RICE-010 | 2 |
| Wheat | Wheat Rust (Stripe/Yellow) | WHEAT-001, WHEAT-002, WHEAT-003 | 3 |
| Wheat | Powdery Mildew | WHEAT-004, WHEAT-005 | 2 |
| Wheat | Fusarium Head Blight | WHEAT-006 | 1 |
| Wheat | Spot Blotch | WHEAT-007, WHEAT-008 | 2 |
| Wheat | Septoria Leaf Blotch | WHEAT-009 | 1 |
| Wheat | Loose Smut | WHEAT-010 | 1 |
| Cotton | Cotton Leaf Curl Disease | COTTON-001, COTTON-002 | 2 |
| Cotton | Bacterial Blight | COTTON-003 | 1 |
| Cotton | Fusarium Wilt | COTTON-004, COTTON-005 | 2 |
| Cotton | Verticillium Wilt | COTTON-006, COTTON-007 | 2 |
| Cotton | Root Rot (charcoal rot) | COTTON-008, COTTON-009 | 2 |
| Cotton | Alternaria Leaf Spot | COTTON-010 | 1 |

## 4. Pakistan-specific publications

| Source ID | Why it is Pakistan-relevant |
|---|---|
| RICE-002 | Magnaporthe oryzae characterisation in **Punjab**; fungicide/botanical screening |
| RICE-007 | Brown-spot IDM review, **Univ. of Agriculture Faisalabad** |
| WHEAT-001 | Stripe-rust genetics/breeding review, **AARI Faisalabad** |
| WHEAT-002 | Climate + stripe rust, **UAF + NIAB** (with CIMMYT) |
| COTTON-001 | CLCuV resistance review, **NIAB-C / PIEAS + PARC** |
| COTTON-002 | CLCuD begomovirus resurgence, **Vehari, Punjab** |

Additional Pakistan/South-Asia relevance: WHEAT-007 (CIMMYT, warm-humid South Asia incl. Pakistan), RICE-008/RICE-010 (reviews with regional co-authors). **Treatment recommendations from non-Pakistani studies must not be assumed to apply in Pakistan** — confirm against local registrations.

## 5. Open-access vs restricted / licence-unconfirmed

**Open access (licence stated in CSV):** RICE-003, RICE-005, RICE-006, RICE-007, RICE-008, RICE-010, WHEAT-001, WHEAT-002, WHEAT-004, WHEAT-005, WHEAT-006, WHEAT-007, WHEAT-008, WHEAT-009, COTTON-001, COTTON-002, COTTON-003, COTTON-005, COTTON-006, COTTON-007, COTTON-008, COTTON-009 (22).

**Restricted / licence to confirm:** RICE-001 (CC BY but confirm), RICE-002 (IJAB — not confirmed), RICE-004 (Planta — subscription likely), RICE-009 (APS — publisher-restricted), WHEAT-003 (confirm), WHEAT-010 (extension — reuse terms), COTTON-004 (Euphytica — subscription), COTTON-010 (extension — reuse terms).

> **Licence caution:** free-to-read ≠ free-to-reuse. Do **not** ingest full text into the assistant's RAG store or redistribute it until each licence is confirmed. Abstracts are not substitutes for full papers.

## 6. Publications / fields needing human verification

1. **RICE-009 (Azzam & Chancellor 2002):** citation confirmed across multiple indexes and the APS article page; the DOI is written in APS standard format — **open it to confirm it resolves**.
2. **Author lists marked `Not verified`:** RICE-004, RICE-005, RICE-010, WHEAT-003, WHEAT-010, COTTON-002, COTTON-009 — complete from the publisher page.
3. **RICE-002 year/volume:** one index listed 2025; the publisher volume (IJAB 22(6)) corresponds to **2019** — confirm the authoritative year.
4. **WHEAT-002 year:** MDPI lists "Plants 2026, 15(7), 1073" (volume 15) — confirm 2025 vs 2026 early-access.
5. **All licences marked "confirm" / "Not confirmed".**
6. **COTTON-002 article number** (Sci. Rep. 2017) — confirm exact article ID.

## 7. Research gaps & recommendations

- **Loose Smut (wheat) and Alternaria Leaf Spot (cotton)** have few recent peer-reviewed *reviews*; both are currently covered by **official extension guides** (Tier 1). Recommend sourcing a Pakistani (AARI / PARC / provincial agriculture dept.) leaflet for each to replace the US extension guides.
- **Bacterial Leaf Blight (rice)**, **FHB**, **Septoria**, **Bacterial Blight (cotton)** each have a single source; adding one Pakistan-focused study per disease would strengthen local applicability.
- **Chemical control:** no spray schedules, doses or intervals were copied from these papers into the dataset. Any chemical recommendation in the assistant **must** come from current official Pakistani registrations and product labels, clearly separated from experimental results.

## 8. Scientific safety flags (built into the data)

- **Rice Tungro (RICE-009, RICE-010)** and **Cotton Leaf Curl Disease (COTTON-001, COTTON-002)** are **viral** — the `notes` field explicitly states they **cannot be cured with fungicides or bactericides**; management is vector control (green leafhopper / whitefly) plus resistant varieties.
- Experimental fungicide/botanical results (e.g., RICE-002, COTTON-008) are flagged as experimental, **not** approved recommendations.
