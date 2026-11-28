# Week 2 — Source Collection (Days 6–8)

IT Simplera Crop Disease Assistant · rice · wheat · cotton · 18 diseases
**Prepared:** 2026‑11‑28 · **Status:** partial & honestly flagged (not “complete”)

## What Week 2 covers

| Day | Focus | Deliverable report |
|-----|-------|--------------------|
| 6 | Rice Tier‑1 institutional sources (R1–R6) | `DAY6_RICE_COLLECTION.md` |
| 7 | Wheat/Cotton Tier‑1 + DPP pesticide lists (W1–W6, C1–C6) | `DAY7_WHEAT_COTTON_DPP.md` |
| 8 | Tier‑2 peer‑reviewed papers to fill gaps | `DAY8_T2_RESEARCH.md` |

## ⚠️ Read this first — two things that shape everything here

**1. This was built without access to your real project.** The desktop bridge to
`E:\Interships\ITSamplera solutions` was offline and the GitHub repo add was
blocked. So this folder could **not**: read your Week‑1 `source_register.csv`,
read the existing `week-2/` folder, download institutional PDFs, or compute
real SHA‑256 hashes. Everything here is built to be **merged in by you** after a
quick check. Nothing is faked; gaps are labelled.

**2. Scope mismatch with Week 1.** The official internship PDF defines the 18
diseases with IDs **R1–R6, W1–W6, C1–C6**. Your Week‑1 register was built on a
*different* list (it used Fusarium Head Blight, Septoria, cotton Fusarium Wilt,
Verticillium Wilt, Alternaria Leaf Spot — **none are in the official 18**, and it
was missing Leaf Rust, Stem Rust, Boll Rot, Anthracnose, Myrothecium Leaf Spot).
**Week 2 uses the official IDs.** You will likely want to reconcile Week 1 later
(that touches Week‑1 files, so it is out of scope for this folder).

## Official 18 diseases (canonical, from the PDF)

- **Rice:** R1 Rice Blast · R2 Bacterial Leaf Blight · R3 Sheath Blight · R4 Brown Spot · R5 False Smut · R6 Rice Tungro *(virus)*
- **Wheat:** W1 Leaf Rust · W2 Stripe Rust · W3 Stem Rust · W4 Powdery Mildew · W5 Spot Blotch · W6 Loose Smut
- **Cotton:** C1 CLCuD *(virus)* · C2 Bacterial Blight · C3 Root Rot · C4 Boll Rot · C5 Anthracnose · C6 Myrothecium Leaf Spot

## Folder layout (this deliverable)

```
week-2/
├── README.md                              (this file)
├── DAY6_RICE_COLLECTION.md
├── DAY7_WHEAT_COTTON_DPP.md
├── DAY8_T2_RESEARCH.md
├── WEEK2_PROGRESS.md
├── SHA256SUMS.csv                         (header only — 0 downloads here, by design)
├── week2_source_register_additions.csv    (23 new sources, register schema; MERGE into your canonical register)
├── scripts/
│   └── fetch_and_hash.py                  (run on YOUR machine to download + hash)
└── sources/                               (created by the helper script when you run it)
    ├── rice/{pdfs,html}/
    ├── wheat/{pdfs,html}/
    ├── cotton/{pdfs,html}/
    └── dpp/
```

## The source register

`week2_source_register_additions.csv` uses the **exact** required columns:

```
source_id,title,authors,publisher,year,type,tier,url_or_doi,licence,crops,diseases,pages_used,language,access_date,verified_by,verification_status,notes
```

- **23 rows** — 13 Tier‑1 institutional + 10 Tier‑2 papers.
- `source_id` uses a **`W2S-` prefix** so it cannot collide with your Week‑1 IDs
  (which this environment could not read). **Renumber to your `SRC-###` scheme
  when merging**, after a duplicate‑DOI check.
- `verification_status`: `in_review` (9) = publisher/DOI metadata + abstract
  retrieved this session; `pending` (14) = page unreachable here or index‑only.
  `verified_by` = “AI‑assisted research; requires human review” for **all** rows.
- All 18 official disease IDs are referenced.

### To merge (suggested)
1. Open your canonical `week-1/knowledge/source_register.csv`.
2. For each `W2S-` row, check its `url_or_doi` isn’t already present (no dup DOIs).
3. Renumber `W2S-00n` → your next `SRC-###`.
4. Append; keep `verification_status` as given until a human verifies.

## How to reproduce the collection work

- **Verify pages / metadata:** open each `url_or_doi` in the additions CSV.
- **Download + hash documents:** `python scripts/fetch_and_hash.py` on a machine
  with open network. It writes `sources/.../` and fills `SHA256SUMS.csv` with
  real `sha256` + sizes. Add the DPP list URL to the script once you locate it.

## Progress & outstanding
See `WEEK2_PROGRESS.md`. Headline outstanding item: **capture the DPP registered
and banned pesticide lists** — the chemical‑safety gate depends on it and it
could not be fetched here.

## Non‑negotiables honoured
No invented papers, authors, DOIs, licences or hashes. No source marked
`verified`. Viral diseases (R6, C1) flagged “no fungicide/bactericide cure”. No
pesticide names/doses invented. Week‑1 and later‑week files untouched.
