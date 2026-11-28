# Week 2 Audit Report

**Audit date:** 2026-11-28  
**Scope:** Agricultural source collection, disease coverage, access/rights, official regulatory evidence and CI.  
**Explicit exclusion:** Machine-learning models, image classification, image datasets and image diagnosis.

## Findings

| Area | Finding | Status |
|---|---|---|
| Crop/disease scope | Rice, wheat, cotton; 18 disease IDs | Confirmed from project brief |
| Initial source register | 61 rows before deep audit | Count checked |
| Deep-audit additions | 12 additional records appended in this branch | In review; not all fully verified |
| Disease coverage | Existing report says >=3 metadata-associated sources for all 18 diseases | Metadata check only; rerun after reconciliation |
| Pakistan evidence | Direct Pakistan sources found for cotton disease gaps, wheat loose smut, wheat powdery mildew prevalence and rice sheath blight/BLB research | Multiple leads verified; card-level review required |
| Source rights | Some records are open access, others have unclear or publisher-restricted terms | Per-source review required |
| DPP registered/banned lists | Official pages identified; actual downloadable lists not archived | Pending |
| SHA-256 manifest | No approved document-download records yet | Correctly empty |
| Staging register | 23 W2S rows require row-by-row review | Pending |
| Image/ML scope | Removed from Week 2 scope | Excluded by project decision |
| CI | Earlier Week 2 branch checks passed; this deep-verification branch needs fresh CI | Pending |

## Evidence quality rules

1. A paper counts for a disease only when its actual title, abstract or full text supports that disease.
2. A homepage or index page is a discovery lead, not a disease-specific evidence source.
3. A Pakistan affiliation does not automatically make a study Pakistan field evidence.
4. A research trial from another country cannot establish a Pakistan pesticide recommendation.
5. Open access does not always mean unrestricted reuse; record the exact licence.
6. Old sources may support taxonomy, symptoms or disease biology, but management advice must prioritize current sources.
7. Chemical products and doses require current DPP registration and the exact official label.
8. No unsupported details should be silently filled in. Missing author names, year, pages or rights remain review items.

## Verified high-value findings

- Punjab Agriculture Department publishes 2026 crop pest alerts, including rice bacterial leaf blight, brown leaf spot, sheath blight and wheat rust.
- Punjab Agriculture Department states that crop reports are issued weekly and fortnightly.
- APS confirms Chohan and Abid's Pakistan cotton boll-rot first report, DOI 10.1094/PDIS-02-18-0314-PDN, with field observations in southern Punjab.
- Pakistan Journal of Phytopathology confirms Ghazanfar et al. (2023) on rice sheath blight, including its laboratory-based biocontrol/plant-extract tests.
- PubMed confirms the 2024 rice sheath-blight study by Sunera et al., with Pakistan affiliations.
- AARI/Punjab-hosted journal records confirm a Pakistan loose-smut trial conducted at AARI Faisalabad.
- PubMed confirms the 2026 nationwide Pakistan wheat disease assessment. It is a broad wheat-health assessment and must not be misrepresented as disease-specific proof for every disease in the register.

## Remaining evidence and risks

- Reconcile the 23 staged W2S records.
- Verify the full text and source rights for each record marked in_review or pending.
- Capture the actual linked DPP registered and banned list files, not just their landing pages.
- Add file names, access dates and SHA-256 values after lawful downloads.
- Re-run the disease coverage report after staging reconciliation.
- Obtain current local extension guidance for loose smut and powdery mildew management.
- Complete independent human review before treating any record as verified.

## Verdict

**Research expansion: completed for this review. Evidence acceptance: partial.**  
Week 2 must not be marked fully complete until the remaining evidence blockers are resolved. Image/ML dataset inventory is explicitly excluded and is not a blocker.
