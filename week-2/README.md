# IT Simplera Crop Disease Assistant — Week 2

**Phase:** Collection (Days 6–10)  
**Contributor:** Individual / solo workflow  
**Scope:** Week 2 only. This folder does not change Week 1 or Weeks 3–8.

## What Week 2 means

Week 1 prepared the repository and the source-register tools. Week 2 is about collecting the actual evidence and recording the datasets that may later support the assistant.

A link in a spreadsheet is not the same as a downloaded source. A downloaded source is not automatically reusable. We record the URL, access date, licence/access conditions and SHA-256 hash, and we do not mark a file downloaded or verified until we have checked it.

## Official Day 6–10 tasks

| Day | Internship brief task | Evidence to keep | Completion rule |
|---|---|---|---|
| 6 | Download rice T1 PDFs/HTML; record hashes and access dates | Rice source collection log and SHA-256 manifest | Rice source links checked; files actually downloaded where lawful |
| 7 | Collect wheat/cotton T1 sources; capture DPP lists | Wheat/cotton source log and dated DPP snapshots | DPP snapshots dated and documented |
| 8 | Collect T2 papers and close research gaps | Added source-register rows and gap notes | At least one source found for each priority gap |
| 9 | Create dataset inventory | Dataset inventory CSV and inspection notes | Licence, classes, counts and field/lab origin recorded |
| 10 | Reach 60 registered sources and review phase | Updated Week 1 canonical source register and coverage report | At least 60 sources; at least 3 per disease; at least 1 Pakistan-specific source per crop; no unlicensed content |

The source register remains the canonical file at `../week-1/knowledge/source_register.csv`. Do not create a second competing register.

## Week 2 files

- `source_collection_log.csv`: official source pages and files to collect, with honest download/hash status.
- `dpp_snapshot_log.csv`: dated record of official DPP registered/banned pesticide list snapshots.
- `dataset_inventory.csv`: inventory of the four dataset groups visible in the user's VS Code screenshot. Counts and licence fields are intentionally pending until local inspection.
- `SHA256SUMS.csv`: file hash manifest. Add entries only after downloading the actual files.
- `WEEK2_PROGRESS.md`: daily checklist and explanations.

## How to calculate a SHA-256 hash (Windows PowerShell)

After downloading a source file into `week-2/sources/`, run:

```powershell
Get-FileHash .\week-2\sources\your-file.pdf -Algorithm SHA256
```

Copy the returned hash into `SHA256SUMS.csv`. A hash identifies the exact file bytes; it does not prove the scientific quality or licence of the source.

## Important research rules

1. Use the official source page or publisher/repository record, not a random re-upload.
2. Confirm title, authors, publisher, year and the actual crop/disease relevance.
3. Record the exact licence or access terms. “Free to read” does not automatically mean “free to redistribute”.
4. Do not upload copyrighted PDFs to GitHub unless the licence permits redistribution. Keep lawful local copies and commit metadata/hashes when redistribution is not allowed.
5. Do not invent source metadata, page numbers, file hashes, dataset counts, image origins or licences.
6. Prefer recent sources for management advice. Older material can support background biology but must be flagged.
7. Chemical recommendations require current official registration and label checks. Do not use this collection log as a pesticide recommendation.
8. Dataset folders are not proof of a dataset's licence. Inspect the dataset's own README, metadata and source page.

## Initial authoritative starting points

- IRRI rice disease fact sheets: https://www.knowledgebank.irri.org/training/fact-sheets/pest-management/diseases
- IRRI diagnostic guide: https://www.knowledgebank.irri.org/images/docs/diagnostic-of-common-diseases-of-rice.pdf
- CIMMYT wheat field-identification guide: https://repository.cimmyt.org/entities/publication/98c26921-80bc-4003-8c26-419fc1bf557c
- CCRI Plant Pathology: https://ccri.gov.pk/pathology.html
- CCRI Annual Progress Report 2023–24: https://ccri.gov.pk/Annual%20Report%202023-2024.pdf
- Pakistan DPP registered pesticide list: https://plantprotection.gov.pk/services/pesticide-registration/list-of-registered-pesticides-in-pakistan/
- Pakistan DPP banned pesticide list: https://plantprotection.gov.pk/services/pesticide-registration/list-of-banned-pesticides-in-pakistan/
- Punjab Agriculture Department crop forecasts: https://agripunjab.punjab.gov.pk/pw_forecast

These are starting points. Each individual publication/download and its access terms still need to be checked.

## Week 2 status

Week 2 is **in progress**. This folder is a tracking scaffold, not a claim that all Day 6–10 acceptance checks are already complete. See [WEEK2_PROGRESS.md](WEEK2_PROGRESS.md).
