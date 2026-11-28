# Week 2 - Dataset Preparation and Disease Coverage

**Phase:** Days 6-10  
**Project:** IT Simplera Crop Disease Assistant  
**Status:** Core repository work complete; local evidence and human verification remain open.

## Goal

Organize the available crop datasets, map research records to the 18 official diseases, and prepare simple tools for coverage, dataset inventory, and file integrity checks.

## Scope

- Crops: rice, wheat, and cotton.
- Official disease scope: six diseases per crop, 18 total.
- Research register: the cumulative Week 1 register is the single source of truth.
- Minimum coverage target: at least three associated source records per disease.
- Dataset folders: four local folders listed in the inventory.

## Week 2 files

| File | Purpose |
|---|---|
| `datasets/dataset_inventory.csv` | Master list of the four local datasets and their verification status |
| `datasets/DATASET_INVENTORY_REPORT.md` | Dataset inspection findings and limitations |
| `datasets/inspect_datasets.py` | Read-only local image inventory utility |
| `reports/disease_source_coverage.csv` | Generated disease-to-source coverage report |
| `scripts/check_coverage.py` | Checks source-register coverage metadata |
| `source_collection_log.csv` | Records source collection and access status |
| `week2_source_register_additions.csv` | Staging list retained for reconciliation |
| `dpp_snapshot_log.csv` | Tracks official pesticide-list evidence capture |
| `SHA256SUMS.csv` | Manifest for documents actually downloaded |
| `fetch_and_hash.py` | Downloads only explicitly approved URLs and records hashes |

## Current verified results

- The cumulative register has 61 populated records.
- The coverage script reports at least three associated records for each of the 18 official disease IDs.
- The local Ruff check passed after the import and regular-expression style fixes.
- Week 2 GitHub Actions previously failed because Ruff also scanned legacy files under `week-1/New folder/`. The workflow exclusion is being corrected separately.

The coverage script checks the metadata in the register. It does not prove that a paper's contents support each disease association, that source details are accurate, or that reuse is permitted.

## Still requiring local or human evidence

1. Run the dataset inventory utility against the actual local `Datasets` directory and review the measured CSV.
2. Check the original publisher/source and licence for each dataset before using its images.
3. Capture dated copies of the actual registered and banned pesticide lists linked by Pakistan's Department of Plant Protection.
4. Download only documents whose access and use terms have been checked; then generate their SHA-256 entries.
5. Reconcile the 23-row staging additions with the cumulative register without inventing or duplicating records.
6. Have a human verify bibliographic details and whether each source genuinely supports its disease mapping.

Do not move, rename, overwrite, or delete the original dataset folders. Do not treat an old pesticide snapshot as proof of current registration.

## Run locally

From the repository root:

```powershell
python week-2/scripts/check_coverage.py
python -m ruff check week-1 week-2
python week-2/datasets/inspect_datasets.py "E:\\Interships\\ITSamplera solutions\\Datasets"
```

The dataset utility writes `week-2/datasets/dataset_inventory_measured.csv`. Review it before updating the master inventory.

To generate hashes, first add only approved document URLs to `DOWNLOADS` in `week-2/fetch_and_hash.py`, then run:

```powershell
python week-2/fetch_and_hash.py
```

## Safety boundary

Week 2 prepares research and dataset evidence. It does not implement a classifier, RAG pipeline, AI agent, diagnosis, or pesticide recommendation engine. Any future chemical guidance must be checked against current official registration and product labels.
