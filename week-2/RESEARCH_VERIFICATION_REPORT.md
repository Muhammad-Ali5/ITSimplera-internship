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


---

# Research update: Pakistan-specific papers and text-only scope (2026-11-28)

This addendum records additional sources inspected after the initial report. It does not upgrade every record to fully verified: full-text review, rights and scientific relevance still need to be checked where stated.

## Additional directly checked records

| Source | Direct evidence observed | Relevance / limitation |
|---|---|---|
| Ahsan et al. (2021), Pakistan rice bacterial leaf blight survey, DOI 10.17582/journal.pjar/2021/34.4.693.699 | Search result metadata and abstract-level record | Pakistan field survey; verify full text and exact bibliographic details before ingestion |
| Ghazanfar et al. (2023), rice sheath blight, DOI 10.33866/phytopathol.035.02.0975 | Pakistan Journal of Phytopathology article page and PDF; authors, pages 387-395, abstract and lab methods visible | Pakistan study; results are primarily in-vitro biocontrol/plant-extract evidence, not a field-validated farmer prescription |
| Sunera et al. (2024), rice sheath blight, DOI 10.1016/j.micpath.2024.107084 | PubMed record, authors, affiliations, abstract and DOI | Pakistan affiliations; full text/access rights must be reviewed |
| Chohan & Abid (2019), cotton boll rot, DOI 10.1094/PDIS-02-18-0314-PDN | APS publisher full text and publication record | Open access first report from southern Punjab; pathogen identification and pathogenicity tests. Strong Pakistan-specific pathogen evidence |
| Husnain et al. (2017), wheat loose smut, AARI Faisalabad | Punjab-hosted journal page/PDF, authors, abstract and trial period | Pakistan trial at AARI (2012-14); historical fungicide data must not be reused as current product advice |
| Plex Sulá et al. (2026), nationwide wheat disease assessment, DOI 10.1094/PHYTO-11-25-0365-R | PubMed record, full authors, publication date, DOI, abstract and CC BY 4.0 status | Nationwide expert-elicitation assessment; useful national risk context, but do not map it to individual disease cards without disease-specific evidence |
| Punjab Agriculture Department 2026 pest alerts | Official alerts page lists rice bacterial leaf blight, brown leaf spot, sheath blight, wheat rust and other crop alerts | Current official extension discovery index; open and archive each disease-specific alert PDF before extracting advice |
| Punjab Agriculture Department pest forecasts | Official page says crop reports are issued weekly and fortnightly | A live discovery point for current crop alerts; each underlying report needs its own source record and date |

## Additional sources added to the canonical register

The branch now contains W2V-001 through W2V-012 in addition to the four records described in the original report. Their verification status is deliberately `in_review`. In particular:
- W2V-005 to W2V-012 add Pakistan rice, wheat and cotton research leads.
- W2V-010 is a nationwide wheat assessment published in November 2026. Its broad findings must not be treated as direct evidence for every wheat disease.
- W2V-012 has author metadata intentionally marked for completion, so it is not ready for final ingestion.
- All entries need final source-rights review.

## Official Punjab sources to capture individually

- 2026 Pest Alerts: https://agripunjab.gov.pk/pw_alerts
- Forecasting of Pests and Crop Diseases: https://www.agripunjab.gov.pk/pw_forecast

The alert index itself is not a substitute for each linked bulletin. Record each bulletin's exact title, date, crop, disease, PDF/HTML URL, pages used and access terms.

## Revised scope: no image or ML work

The original IT Simplera brief labels image classification as optional, while its core architecture is curated knowledge, OCR, Regex, hybrid RAG and LangGraph. The project scope is now explicitly text-only:
- no machine-learning model;
- no image classification;
- no image dataset inventory;
- no image diagnosis endpoint.

The former Week 2 image inventory report, CSV and inspection script have been removed from this branch. This is a scope decision, not an outstanding acceptance task.

## Current honest completion state

Research discovery and source-register expansion are complete for this work session. Week 2 evidence acceptance remains blocked by:
1. 23 staged W2S rows not yet reconciled;
2. actual DPP registered/banned list files not yet captured and hashed;
3. incomplete per-source rights and full-text checks;
4. final disease-by-disease source validation;
5. final coverage, Ruff and GitHub Actions run on this updated branch.

Do not mark Week 2 fully complete until these are resolved. No pesticide recommendation or dose is approved.
