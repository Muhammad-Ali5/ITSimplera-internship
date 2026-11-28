# Week 2 Progress

**Updated:** 2026‑11‑28 · **Honest status: PARTIAL — not complete.**

## Completion status at a glance

| Day | Target | Done | Not done |
|-----|--------|------|----------|
| 6 Rice T1 | Collect + verify + download + hash R1–R6 | Metadata for 3 T1 sources; disease IDs confirmed | IRRI fetch blocked; **no downloads/hashes**; PARC docs not located |
| 7 Wheat/Cotton/DPP | T1 wheat+cotton; capture DPP lists | 7 wheat/cotton T1 (3 Pakistan pages verified live) | **DPP registered/banned lists NOT captured**; no downloads/hashes |
| 8 T2 gaps | ≥1 paper per priority gap | 10 T2 papers; all official gaps have ≥1 source; 6 DOIs confirmed | some DOIs/citations still to confirm; W1/W3 thin |

## Completed tasks (with evidence)

- Extracted the **exact 18 diseases + IDs** from the internship PDF (§3.1–3.3).
- Logged **23 new sources** into `week2_source_register_additions.csv` (correct
  17‑column schema; no duplicate `source_id`; no duplicate DOI; all 18 IDs referenced).
- **Verified live** (content retrieved this session):
  - CCRI Reports page + Annual Report 2023‑2024 link (W2S‑009)
  - CCRI Cotton Pathology page (W2S‑010)
  - Sindh Agriculture “Diseases of Cotton & their control” (W2S‑011)
  - CIMMYT “Bunt and Smut Diseases of Wheat”, incl. Loose Smut chapter + ISBN (W2S‑006)
- **DOI + abstract retrieved** for 6 Tier‑2 papers (W2S‑015, 016, 019, 020, 021; plus Mapuranga PM review as cross‑reference).
- Wrote Day 6/7/8 reports, README, this progress file, `SHA256SUMS.csv`
  (header‑only, honest), and `scripts/fetch_and_hash.py`.

## Pending tasks (must be done on your machine / manually)

1. **DPP pesticide lists** — capture the current **registered** list and the
   **banned** list from `plantprotection.gov.pk`; save a dated snapshot under
   `sources/dpp/`. *Blocker for the chemical‑safety gate.* ← highest priority
2. **Downloads + SHA‑256** — run `scripts/fetch_and_hash.py` (IRRI diagnostic
   PDF, CCRI AR 2023‑24, FAOLEX Rules, DPP list).
3. **Open & confirm** IRRI pages (R1–R6 fact sheets) and CIMMYT handles 10883/1115, 10883/3219.
4. **Confirm citations/DOIs** for AGRIS‑only / DOI‑unshown rows: W2S‑014 (C4),
   W2S‑017 (C6), W2S‑022, W2S‑023.
5. **Strengthen thin diseases:** dedicated Pakistan papers for **W1 Leaf Rust**
   and **W3 Stem Rust**; a Pakistan cotton‑anthracnose and cotton‑Myrothecium
   source would help too.
6. **Merge** additions into the canonical register (renumber `W2S-` → `SRC-###`,
   dedup‑check DOIs) — this is yours to do since I couldn’t read the register.

## Evidence links (key)

- Internship PDF (source of truth): `IT_Simplera_Crop_Disease_Assistant_Enhanced.pdf`
- CCRI reports: https://ccri.gov.pk/reports.html
- CCRI pathology: https://ccri.gov.pk/pathology.html
- Sindh Agriculture cotton diseases: https://agri.sindh.gov.pk/diseases-of-cotton-their-control
- CIMMYT repository (Bunt & Smut): https://repository.cimmyt.org/
- Register additions: `week2_source_register_additions.csv`

## Honest completion statement

Week 2 is **not complete.** Files exist and the research is genuine, but
**(a)** no documents were downloaded or hashed in this environment, **(b)** the
DPP pesticide lists — the most safety‑critical item — are not yet captured, and
**(c)** merging into the canonical register and the Week‑1 scope reconciliation
still require your action on the actual repo.
