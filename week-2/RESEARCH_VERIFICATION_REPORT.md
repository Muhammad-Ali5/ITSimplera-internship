# Week 2 Deep Source Verification

Audit date: 2026-11-28

## Verdict

Week 2 is **partially complete, not fully evidence-complete**. The 61-row canonical source register and disease coverage checker demonstrate metadata coverage, not source accuracy, licence permission, or scientific support. Four additional sources with directly inspected institutional/repository evidence have been added to the canonical register as W2V-001 through W2V-004 on this branch.

## Evidence verified in this review

| Source | What was checked | What it supports | Limits |
|---|---|---|---|
| IRRI, *Rice diseases: Biology and selected management practices* (2018) | Online contents and disease categories | Rice blast, bacterial blight, sheath blight, brown spot, false smut and tungro are represented in this IRRI resource | Verify individual chapter sections and reuse terms before extraction |
| CIMMYT, *Wheat Diseases and Pests: A Guide for Field Identification*, 2nd edition (2012) | Full PDF and contents | Wheat rusts, loose smut, powdery mildew and spot blotch identification | Distinct from the 1986 guide already registered; older management advice is not current Pakistan pesticide guidance |
| Khan et al. (2019), *Northern Himalayan region of Pakistan with cold and wet climate favors a high prevalence of wheat powdery mildew* | CIMMYT repository record and abstract | Pakistan field-survey evidence for wheat powdery mildew prevalence | Prevalence study, not a current management prescription |
| CCRI Multan Plant Pathology Section | Official page content | Pakistan-specific discussion of cotton bacterial blight, root rot, boll rot and anthracnose | Some chemical advice is historical; verify management independently |

## Priority research gaps

| Gap in project brief | Finding | Status |
|---|---|---|
| Cotton bacterial blight | CCRI pathology page directly discusses it | Pakistan institutional source found |
| Cotton root rot | CCRI pathology page directly discusses it | Pakistan institutional source found |
| Cotton boll rot | CCRI pathology page directly discusses it | Pakistan institutional source found |
| Cotton anthracnose | CCRI pathology page directly discusses it | Pakistan institutional source found |
| Wheat loose smut | CIMMYT 2012 field guide includes loose smut | Identification source found; seek current Pakistan management source |
| Wheat powdery mildew management in Pakistan | Khan et al. (2019) field survey plus CIMMYT guide | Pakistan prevalence evidence found; current local management recommendation still missing |

## Important bibliographic correction

The existing register contains a separate CIMMYT guide dated 1986. The PDF inspected during this review is the **second edition from 2012**, edited by Duveiller, Singh, Mezzalama, Singh and Dababat. Both records should remain distinct.

## Staging reconciliation

The staging file contains 23 records, W2S-001 through W2S-023. None of those IDs occurs in the 61-row canonical register fetched at the start of this review. The 23 records have not been blindly merged because some contain incomplete authorship, uncertain reuse rights, generic landing pages, or disease mappings that still need review. Four separately inspected sources were added as W2V-001 through W2V-004.

## DPP pesticide evidence

The official DPP registered-pesticide page was found and states that its registered product list includes Form-01, Form-16 and Form-17, plus a separately notified Form-16 list. The official banned-pesticide page was also found. The DPP download index lists Agricultural Pesticide Rules, the Ordinance, registration forms and SRO records.

The actual linked registered and banned list files were **not downloaded or archived in this review**. Attempts to open the official pages timed out. Therefore, do not mark the DPP snapshots complete. The 2026 secondary article describing a 30 January 2025 spreadsheet is not a substitute for a direct dated DPP capture. Before any chemical advice, check the current DPP list, the exact crop/pest use, the product registration validity, and the current product label.

## Dataset inventory scope

The project brief lists dataset inventory on Day 9, but image classification is a conditional module separate from text RAG. No local dataset folder measurements or dataset licence checks were performed here. If the project lead defers vision, document that decision and mark the image dataset inventory as deferred. Otherwise, inventory only approved dataset locations and verify each original publisher's licence. Do not infer that local folders are approved or legally reusable.

## Remaining acceptance checklist

- [ ] Reconcile the 23 W2S staging rows one by one: merge after review, revise, or reject.
- [ ] Capture actual DPP registered and banned list files with exact URL, filename, capture date and SHA-256.
- [ ] Verify crop/pest-specific registration and current label before any chemical guidance.
- [ ] Open individual IRRI disease chapters and record exact chapter/section references and reuse terms.
- [ ] Obtain a current Pakistan extension source for wheat loose-smut management and wheat powdery-mildew management.
- [ ] Decide whether the Day 9 image dataset inventory is in scope; record project-lead deferral if vision is postponed.
- [ ] Download only materials whose access terms are checked, then generate SHA-256 entries.
- [ ] Obtain human review of disease mapping, taxonomy, bibliographic details and rights.
- [ ] Run coverage, Ruff and GitHub Actions on this branch and review the pull request.

## Safety

No pesticide product or dose is approved by this report. Viral disease advice must follow the brief's rule that fungicides and bactericides are not cures for viral diseases. Publicly viewable content is not automatically licensed for bulk ingestion, redistribution or model training.

## Sources inspected

- IRRI: https://rice-diseases.irri.org/contents
- CIMMYT 2012 wheat guide: https://repository.cimmyt.org/server/api/core/bitstreams/60c2d78f-c921-45a5-b368-962b902ff60d/content
- Khan et al. (2019) repository record: https://repository.cimmyt.org/entities/publication/dd006716-0865-4db6-946f-96c6a6c4b5b5
- CCRI Multan: https://ccri.gov.pk/pathology.html
- Punjab Agriculture pest alerts: https://agripunjab.gov.pk/pw_alerts
- Punjab Agriculture pest forecasts: https://www.agripunjab.gov.pk/pw_forecast
- DPP registered pesticides: https://plantprotection.gov.pk/services/pesticide-registration/list-of-registered-pesticides-in-pakistan/
- DPP banned pesticides: https://plantprotection.gov.pk/services/pesticide-registration/list-of-banned-pesticides-in-pakistan/
- DPP pesticide registration downloads: https://plantprotection.gov.pk/downloads/pesticide-registration/
- Pakistan Agricultural Pesticides Rules (consolidated): https://tipp.gov.pk/ur-pk/site/display/49
