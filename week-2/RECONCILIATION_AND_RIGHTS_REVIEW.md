# Week 2 Staging Reconciliation and Rights Review

Audit date: 2026-11-28  
Scope: text-only crop disease knowledge (rice, wheat, cotton; 18 disease IDs). No ML/image work.

## Result

All 23 staged rows W2S-001 through W2S-023 have now received an explicit disposition in `staging_reconciliation.csv`. This closes the administrative reconciliation task: no row is left without a decision. It does **not** mean every candidate is approved for ingestion. Duplicates are mapped to canonical records; weak/incomplete items are retained only as leads or rejected from disease coverage.

- Merge duplicates: W2S-004 → W2V-002; W2S-010 → W2V-004; W2S-014 → W2V-008; W2S-019 → W2V-003.
- Do not count general indexes, policy sources or global references as disease-specific Pakistan evidence.
- Preserve the distinction between open access, free-to-read and permission to reuse.
- Do not copy full copyrighted publications into the knowledge base unless licence/permission allows it.

## DPP evidence review

### Registered products

The official DPP page says the national register is divided across Form-1, Form-16 and Form-17. The official page itself could not be opened to capture its linked spreadsheet during this audit. A secondary report dated 28 November 2026 states it downloaded a spreadsheet titled “Registered Product List Form-1, 16, 17”, dated 30 January 2025, and counted 2,061 rows (141/950/970 across the three tabs). This is secondary corroboration, not a substitute for our own official-file capture. It also means the spreadsheet may not include registrations issued after 30 January 2025. Do not label it “current as of 2026” without DPP confirmation.

### Banned products

The official DPP banned-list page links to an official PDF:
https://plantprotection.gov.pk/wp-content/uploads/2021/07/LIST-OF-BANNED-PESTICIDES-26-PRODUCTS.pdf

The indexed PDF text lists 26 banned chemicals and historical notification details, including endosulfan (SRO 1329(I)/2012). Search indexing allowed the contents to be inspected, but the PDF could not be downloaded into this workspace. Therefore this is a verified official web reference, not a locally archived snapshot with SHA-256.

### Regulatory rules

DPP's official consolidated Agricultural Pesticides Rules PDF is indexed here:
https://plantprotection.gov.pk/wp-content/uploads/2021/05/Agricultural-Pesticide-Rules-APR.pdf

The TIPP text also exposes the rules. The rules explain registration processes/forms and validity/renewal provisions. They are legal background, not a product register.

### What remains technically impossible from this workspace

- The DPP site timed out/returned gateway errors when opened.
- The direct PDF download failed in the runtime.
- The registered spreadsheet's actual linked URL was not exposed by the search index.
- Consequently, no authentic binary file, file size or SHA-256 can be claimed for either DPP list.

The log uses explicit states `web_verified_not_archived` and `secondary_report_only` rather than falsely claiming snapshot completion.

## Rights review policy applied

- **CC BY / CC BY 4.0:** reusable with attribution and licence conditions if verified on the source itself.
- **Publicly accessible government page:** public access does not automatically grant bulk redistribution or commercial reuse.
- **Open Access / free download:** not automatically an open licence; inspect the rights statement.
- **Publisher subscription or unclear terms:** do not copy full text; use citation/metadata and obtain lawful institutional access or permission.
- **FAO 2002 book:** page states educational/non-commercial reuse with attribution; commercial reuse requires permission.
- **CIMMYT 1986 guide:** repository says download, print, store and share are allowed; translations/derivative works require permission.
- **CCRI page:** copyright notice is present; permission for reuse/redistribution is not established.
- **Experimental pesticide trials:** never convert their treatment rates into farmer recommendations. Current Pakistan DPP registration and exact label must be checked.

## Coverage checker limitation discovered

The existing `check_coverage.py` counts any disease association in the metadata, regardless of `verification_status`. It is a structural coverage counter only. Its success message must never be described as proof of three scientifically verified, rights-cleared sources per disease. This report makes that limitation explicit.

## CI

The GitHub connector did not return check-run statuses for the current head commit, and the workflow-run lookup did not provide a confirmed run result for the latest branch head. CI is therefore **not verified green**. A commit on the branch should trigger the repository workflow; review the Actions tab and confirm all required checks pass before merging.

## Final disposition

Administrative staging reconciliation: **complete**.  
Source discovery: **expanded**.  
Source rights and full-text review: **partial; human approval still required**.  
DPP web evidence: **identified and indexed**.  
DPP binary snapshots and hashes: **not captured**.  
Final CI: **not confirmed**.

Week 2 must not be represented as fully evidence-accepted until the official DPP spreadsheet is captured from DPP (or confirmed directly by DPP), binary snapshots are archived and hashed, source rights are approved, and CI passes.


## Critical regulatory update discovered on 2026-11-29

A current news report published 26 November 2026 says the federal government notified the abolition of DPP effective **1 December 2026**, with pesticide regulatory functions transferring to the National Agri-trade and Food Safety Authority (NAFSA). It reports that the Ministry notification was issued 25 November 2026 and that the Agricultural Pesticides Ordinance, 1971 and Pakistan Plant Quarantine Act, 1976 are to be repealed from that date. This is a time-sensitive legal transition claim sourced to secondary reporting, not a directly inspected Gazette notification. See:
https://profit.pakistantoday.com.pk/2026/11/26/government-sets-december-1-deadline-to-abolish-dpp-transfers-regulatory-powers-to-nafsa

**Operational implication:** this project must not hard-code DPP as the permanently current authority. Until the effective date and implementation are confirmed from the Gazette/Ministry/NAFSA, retain DPP pages as the historical/legacy register source and add an authority-transition check. From 1 December 2026, check NAFSA's official portal or notification for the successor live register and banned list. A 30 January 2025 DPP spreadsheet is historical snapshot evidence only, not proof of current registrations on 29 November 2026.

The official DPP page was crawled today and still describes Form-1, Form-16 and Form-17 lists:
https://plantprotection.gov.pk/services/pesticide-registration/list-of-registered-pesticides-in-pakistan/
The official banned-list landing page is also still indexed:
https://plantprotection.gov.pk/services/pesticide-registration/list-of-banned-pesticides-in-pakistan/
The DPP downloads page lists pesticide rules, forms and SRO registration documents:
https://plantprotection.gov.pk/downloads/pesticide-registration/
The pages being visible does not prove the department remains the competent authority after the notified transfer date.

A 2026 SBP environmental and social management framework reproduces an indicative DPP banned-pesticide extract. It is useful corroboration but is explicitly an indicative extract, not the official current list:
https://www.sbp.org.pk/assets/document/RAM_s_Environmental%2C_Health_and_Safety_Guidelines_-_September_2026.pdf

## Snapshot status correction

The DPP banned-list PDF URL is now identified:
https://plantprotection.gov.pk/wp-content/uploads/2021/07/LIST-OF-BANNED-PESTICIDES-26-PRODUCTS.pdf

Search indexing exposed its title and content, but a binary download into this runtime failed. The registered-products spreadsheet link was not exposed by the official page text. No SHA-256 has been computed. Therefore, both files remain **not archived**. The correct completion path is:
1. preserve the official DPP list page and its actual linked file URL;
2. archive the file bytes with access timestamp and SHA-256;
3. verify the successor authority transition and whether NAFSA has issued a replacement/updated list;
4. keep the historical DPP snapshot separate from the post-transition current register.

Do not treat a file linked from a secondary website as the official register unless its provenance and integrity are independently established.

## Current legal-source hierarchy for pesticide status

1. Gazette of Pakistan / Ministry notification establishing the authority transfer and effective date.
2. NAFSA official register and notices after the effective transfer date, once published.
3. Archived DPP Form-1/Form-16/Form-17 and banned lists as historical records, with dates.
4. Provincial agriculture extension bulletins for crop-specific advice, cross-checked against the federal registration and product label.
5. Secondary news and institutional extracts only as discovery/corroboration, never as the sole basis for a product recommendation.
