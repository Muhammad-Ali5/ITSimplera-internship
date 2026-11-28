# Day 6 — Rice Tier 1 Source Collection

**Date:** 2026-11-28 (Asia/Karachi)
**Scope:** Official rice diseases **R1–R6** (from the internship PDF, §3.1)
**Owner:** I1 (Research & Knowledge) · solo intern
**Status:** Partial — metadata collected; **no PDFs downloaded in this environment** (see Environment note)

> **Environment note (honesty):** This collection ran in a cloud sandbox whose
> shell network reaches only package registries, and the desktop bridge to the
> local project (`E:\Interships\ITSamplera solutions`) was **offline**. So I
> could **not** download institutional PDFs or compute their SHA‑256 here.
> Where a page allowed automated reading I verified it; where it did not
> (IRRI) I have said so plainly. Use `scripts/fetch_and_hash.py` on your own
> machine to download + hash the rice PDFs and populate `SHA256SUMS.csv`.

## Official rice diseases (exact IDs from the PDF)

| ID | Disease | Candidate causal agent | Type |
|----|---------|------------------------|------|
| R1 | Rice Blast | *Magnaporthe oryzae* (syn. *Pyricularia oryzae*) | Fungus |
| R2 | Bacterial Leaf Blight | *Xanthomonas oryzae* pv. *oryzae* | Bacterium |
| R3 | Sheath Blight | *Rhizoctonia solani* AG1‑IA | Fungus |
| R4 | Brown Spot | *Bipolaris oryzae* | Fungus |
| R5 | False Smut | *Ustilaginoidea virens* | Fungus |
| R6 | Rice Tungro | RTBV + RTSV | **Virus** (no fungicide/bactericide cure) |

## Sources collected (Tier 1)

| source_id | Source | Publisher | URL | Covers | Verify status |
|-----------|--------|-----------|-----|--------|---------------|
| W2S-001 | Rice Diseases fact sheets (Rice Knowledge Bank) | IRRI | knowledgebank.irri.org/…/pest-management/diseases | R1–R6 | **pending** — fetch blocked |
| W2S-002 | Diagnosis of Common Diseases of Rice (Elazegui & Islam, 2003) | IRRI | …/images/docs/diagnostic-of-common-diseases-of-rice.pdf | R1–R6 | **pending** — not downloaded |
| W2S-003 | PARC crop research programmes | PARC | parc.gov.pk | R1–R6 (locate docs) | **pending** |

Full bibliographic rows (all 17 register columns) are in
`week2_source_register_additions.csv`.

## What was actually checked

- **IRRI Rice Knowledge Bank & the IRRI diagnostic PDF** — listed in the
  internship PDF (§5.4 and §21.1) as the primary rice T1 sources. Automated
  fetch returned *robots unreachable* for the IRRI host, so I could **not**
  confirm the live page content or download the PDF here. They remain
  **pending**: open them manually, confirm each fact sheet, and capture the
  per‑disease URLs.
- **PARC** — recorded as the Pakistan institutional entry point; the specific
  rice‑disease publications still need locating on the live site.
- **FAO rice** — no single rice‑specific FAO document was verified this session;
  FAO wheat and FAO pesticide references are logged under Day 7 instead.

## Downloads & SHA‑256 evidence

**None in this environment.** `SHA256SUMS.csv` has a header and **zero document
rows** — this is the honest state, not an omission. To produce real hashes:

```bash
python scripts/fetch_and_hash.py   # run on your machine, network open
```

The script downloads the IRRI diagnostic PDF (and others you approve), writes
`sources/rice/pdfs/…`, and appends `filename, relative_path, sha256,
file_size_bytes, downloaded_at`.

## Access & licence status

All three rice sources are **institutional**; licence/reuse terms are **not yet
confirmed**. Treat “free to read” ≠ “free to reuse/ingest” until each site’s
terms are checked (internship PDF §5.2, §6).

## Outstanding for Day 6

- [ ] Manually open IRRI pages; capture per‑disease fact‑sheet URLs (R1–R6).
- [ ] Download the IRRI diagnostic PDF + hash it (helper script).
- [ ] Locate a PARC (or Punjab/Sindh Agriculture) rice‑disease document, ideally
      Pakistan field evidence for R1 (blast) and R2 (BLB).
- [ ] Confirm reuse rights for each before ingestion.
