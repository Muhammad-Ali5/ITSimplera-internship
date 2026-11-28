# Week 2 - Agricultural Source Collection and Verification

**Phase:** Days 6-10  
**Project:** IT Simplera Crop Disease Assistant  
**Scope decision:** Text-based agricultural knowledge only. Machine-learning models, image classification, image datasets and image diagnosis are excluded from this project scope.

## Goal

Collect and verify lawful, authoritative agricultural sources for rice, wheat and cotton; register source metadata; check disease coverage; identify Pakistan-specific evidence; and document official pesticide-regulatory references.

## Scope

- Crops: rice, wheat and cotton.
- Disease scope: six diseases per crop, 18 total, using the IDs in the project brief.
- Core approach: curated sources, PDF/HTML ingestion, OCR where needed, Regex normalization, hybrid text retrieval and LangGraph in later phases.
- No image classifier, no ML training, no image dataset inventory, and no image diagnosis endpoint.
- The Week 2 Day 9 image-dataset task in the original brief is formally excluded by the project's revised text-only scope. It is not a pending task.

## Week 2 files

| File | Purpose |
|---|---|
| `../week-1/knowledge/source_register.csv` | Canonical cumulative source register |
| `reports/disease_source_coverage.csv` | Disease-to-source metadata coverage report |
| `scripts/check_coverage.py` | Checks crop-aware metadata coverage against 18 disease IDs |
| `source_collection_log.csv` | Records source discovery and access status |
| `week2_source_register_additions.csv` | Staging list requiring row-by-row reconciliation |
| `dpp_snapshot_log.csv` | Tracks actual official DPP pesticide-list evidence capture |
| `SHA256SUMS.csv` | Manifest for documents actually downloaded |
| `fetch_and_hash.py` | Downloads only explicitly approved URLs and records hashes |
| `RESEARCH_VERIFICATION_REPORT.md` | Research findings, verified citations, gaps and limitations |

## Verified repository work

- The pre-audit canonical register contained 61 source records and the coverage checker reported at least three metadata associations for all 18 diseases.
- Twelve additional research records have been appended in the deep-verification branch. Their status remains `in_review` until full bibliographic, scientific and rights checks are completed.
- Directly inspected sources include IRRI rice disease material, CIMMYT wheat field-identification material, CCRI cotton pathology information, Pakistan Journal of Phytopathology papers, Punjab Agriculture Department alerts, APS Plant Disease reports, PubMed records and AARI-hosted research.
- Ruff passed on the earlier Week 2 implementation branch. Final branch CI must still be checked.
- The coverage checker is a metadata test, not proof of scientific correctness, source quality or licence permission.

## Remaining evidence for sign-off

1. Reconcile all 23 W2S staging records: merge only when title, authors, publication, DOI/URL, crop/disease relevance and access terms are supported; otherwise correct or reject.
2. Capture the actual current DPP registered and banned pesticide files, with exact linked URL, file name, capture date and SHA-256. A landing-page visit is not a snapshot.
3. Review each source's licence/access condition and distinguish open access, free-to-read, repository download and permission-restricted content.
4. Confirm at least one Pakistan-specific source per crop and at least three genuinely relevant sources per disease. Do not count a broad homepage or a disease-agnostic paper as disease evidence.
5. Obtain current Pakistan extension guidance for wheat loose-smut and powdery-mildew management. Historical studies can support biology or prevalence, not current pesticide advice.
6. Download and hash only documents whose access and use terms have been checked.
7. Obtain human review of taxonomy, disease mapping, bibliography and rights.
8. Run the coverage checker, Ruff and GitHub Actions on this branch.

## Chemical safety boundary

No pesticide product or dose is approved by this research phase. Chemical recommendations require a current official Pakistan registration check and the exact current product label for the crop and target disease/pest. Never infer, convert or calculate a dose. Viral diseases must not be described as curable with fungicides or bactericides.

## Run locally

From the repository root:

```powershell
python week-2/scripts/check_coverage.py
python -m ruff check week-1 week-2
```

## Acceptance decision

Week 2 is **research-expanded but not yet fully evidence-accepted**. It becomes complete when the staging records are reconciled, the actual DPP snapshots are captured, the lawful-access evidence is reviewed, the source coverage is scientifically checked, and CI passes. The image dataset inventory is not part of the revised scope.
