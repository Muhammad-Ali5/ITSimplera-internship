# Day 9 — Dataset Inventory Report

**Date:** 2026‑11‑28 · **Status:** PARTIAL — structure recorded; **image counts NOT measured remotely** (see below)

## Honest limitation (read first)

The four datasets live under `/Datasets/`, which is **gitignored** (confirmed in
`.gitignore`) and therefore **not in the GitHub repository**. The desktop bridge
to `E:\Interships\ITSamplera solutions` was **offline** when these files were
prepared. So the actual **image counts, per‑class counts, train/val/test splits,
corrupt files and duplicates could not be measured** here.

Per the project rules, **no image or class counts were invented.** Every count in
`dataset_inventory.csv` is left blank/`pending`. To fill them with real numbers,
run the provided script on your machine:

```bash
python week-2/datasets/inspect_datasets.py "E:\Interships\ITSamplera solutions\Datasets"
```

It writes `dataset_inventory_measured.csv` with real totals, per‑class counts,
formats, likely duplicates and unreadable files. Copy those into
`dataset_inventory.csv` and set `verification_status` to `verified`.

## The four datasets (from folder names + your screenshot notes)

| ID | Folder | Crop | What is known | What to check locally |
|----|--------|------|---------------|-----------------------|
| DS‑001 | Cotton Leaf Disease Dataset with Severity Levels | cotton | Folder **and** a ZIP variant were visible in VS Code | Don't double‑count the ZIP + extracted copy; find README/source + licence |
| DS‑002 | long‑diseases | unknown | Name doesn't reveal crop/classes | Inspect contents + any metadata to identify crop and classes |
| DS‑003 | rice ninja | rice | Has `train/valid/test` + `LICENSE.md`, `meta.json`, `README.md`; platform **Dataset Ninja** (`cdn.datasetninja.com/rice-disease`) | Read `LICENSE.md` for exact reuse terms; count per class |
| DS‑004 | rice_leaf_diseases | rice | Class folders include **Bacterial leaf blight, Brown spot, Leaf smut** | Confirm original source + licence; map classes to official IDs |

## Mapping datasets to the official 18 diseases (important)

Datasets must **not** silently redefine the official disease list. Two mismatches
to resolve before any future image work:

- **DS‑004 "Leaf smut"** is **not** an official rice disease. Official rice is
  R1 Blast, R2 Bacterial Leaf Blight, R3 Sheath Blight, R4 Brown Spot,
  **R5 False Smut**, R6 Tungro. Confirm whether "Leaf smut" maps to R5 or is a
  different class to exclude.
- DS‑001/003/004 cover only a **subset** of the 18 diseases (mostly a few rice
  and cotton classes). There is **no dataset** for most wheat diseases or for
  several cotton diseases. This is fine — the primary system is **knowledge/RAG
  based**, not image‑based.

## Image classification is conditional (do not train now)

The internship brief and `week-1/README.md` state image diagnosis is **optional
later work, only for classes with enough licensed and validated images.** No
classifier was trained (correctly). Recommendation: treat these datasets as
**candidate** material only; decide on image work **after** (a) licences in each
`LICENSE.md`/source page are confirmed, and (b) `inspect_datasets.py` shows which
classes have enough clean, non‑duplicate, correctly‑labelled images.

## Outstanding for Day 9

- [ ] Run `inspect_datasets.py` → fill real counts in `dataset_inventory.csv`.
- [ ] Read each dataset's `LICENSE.md`/source page; record exact licence + evidence.
- [ ] Resolve the DS‑004 "Leaf smut" → official‑disease mapping.
- [ ] Confirm DS‑002 crop/classes; de‑dup the DS‑001 ZIP vs extracted copy.
