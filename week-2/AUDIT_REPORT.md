# Week 2 Audit Report

**Audit date:** 2026-11-28  
**Scope:** Dataset inventory, source coverage, download/hash utility, regulatory evidence and CI.

## Findings

| Area | Finding | Status |
|---|---|---|
| Disease coverage | 61 register records; coverage script reports >=3 associated records for all 18 diseases | Passed metadata check |
| Coverage meaning | Mapping is based on disease and crop text in CSV records | Human review required |
| Pakistan source check | Uses Pakistan/institution/location markers in metadata | Human review required |
| Dataset inventory | Four local dataset folders are listed | Actual counts pending |
| Dataset inspection | Utility uses full-file SHA-256 for exact duplicates and writes a separate report | Ready for local run |
| Dataset licence | Original publisher terms have not been fully reviewed | Pending |
| DPP registered/banned lists | Landing pages are logged; dated copies of actual linked lists are absent | Pending |
| SHA-256 manifest | No downloaded-document rows are present | Correctly empty |
| Download helper | Output paths now resolve under `week-2/`; download list is intentionally empty until approvals | Ready after approval |
| GitHub Actions | Week 2 CI passed on PR #2 after Ruff exclusions and the unused import fix | Passed on PR branch; merge to main pending |

## Issues corrected in this review

1. Clarified that coverage is a metadata association check, not scientific validation.
2. Made disease-name mapping crop-aware for the shared term "bacterial blight".
3. Improved dataset duplicate detection to hash complete files rather than only the first 64 KiB.
4. Renamed the inventory metrics to avoid claiming image corruption when only file-read errors are detected.
5. Corrected the download helper's output directory and manifest path.
6. Made the download list empty by default so no source is downloaded before its access terms are checked.

## Remaining evidence and risks

- Review every source citation, title, author list, disease relevance and licence.
- Run the dataset inspection utility on the actual local folders and manually review the measured report.
- Check dataset licences before using images for training or redistribution.
- Capture dated copies of the actual DPP registered and banned pesticide lists.
- Reconcile the 23-row staging CSV with the cumulative 61-row register.
- Confirm GitHub Actions after the workflow exclusion is corrected.

## Verdict

**Repository preparation: complete for this phase. Evidence acceptance: still partial.**

No source, licence, dataset count, pesticide status, or file hash should be described as verified without its corresponding evidence.
