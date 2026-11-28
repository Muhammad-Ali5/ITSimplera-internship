# Week 2 Audit Report

**Audit date:** 2026-11-28  
**Scope:** Days 6–10, repository evidence, source register, dataset and safety records.

## Findings

| Requirement | Evidence | Status |
|---|---|---|
| Rice Tier 1 collection | Rice records and Day 6 research notes | Partial; some pages/downloads need confirmation |
| Wheat and cotton Tier 1 collection | Source register and Day 7 notes | Partial |
| DPP registered and banned pesticide snapshots | `dpp_snapshot_log.csv` contains page references | Blocked; dated snapshots not captured |
| Tier 2 gap-filling research | 61-record cumulative register and staging file | Partial; human verification outstanding |
| Dataset inventory | Four dataset records and local inspection script | Partial; counts/licences not fully measured |
| At least 60 cumulative sources | Canonical register has 61 unique source IDs | Count met |
| At least three sources per official disease | `reports/disease_source_coverage.csv` | Coverage report says all 18 meet threshold |
| Pakistan-specific sources for each crop | Coverage report and source register | Present in report; each source still requires verification |
| SHA-256 for downloaded material | `SHA256SUMS.csv` is header-only | Blocked; no downloaded files evidenced |

## Register reconciliation note
The repository contains a 61-row cumulative register in `week-2/source_register.csv`, while the original Week 1 register has 30 rows. The 61-row file retains the original 30 records and adds further records. The separate 23-row `week2_source_register_additions.csv` uses W2S-prefixed staging IDs and is not a one-to-one copy of the 31 additional records in the 61-row register. The canonical register is the cumulative source of truth; the staging file is retained for provenance and manual reconciliation.

## Dataset protection
The four dataset folders remain local and are not copied into GitHub. The inventory utility is intended to read files and produce a separate report. Do not move, rename, delete, overwrite, or modify original dataset contents.

## Verdict
**Week 2 is partial, not complete.** The numerical register and disease-coverage targets are represented. DPP snapshots, downloaded-document hashes, dataset measurements/licence review, and human source verification remain outstanding.
