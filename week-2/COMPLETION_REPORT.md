# Week 2 Completion Report

**Phase:** Days 6-10  
**Decision:** **Core repository work complete; evidence acceptance remains partial.**

## Completed repository work

| Deliverable | Evidence | Result |
|---|---|---|
| Official crop/disease scope | 3 crops and 18 disease IDs in coverage checker | Complete |
| Cumulative source register | Week 1 canonical CSV | 61 records |
| Disease coverage report | `reports/disease_source_coverage.csv` | All 18 meet the metadata threshold of 3 |
| Coverage validation | `scripts/check_coverage.py` | Passed locally |
| Dataset inventory structure | Four dataset rows in master CSV | Created; measurements pending |
| Dataset inspection utility | `datasets/inspect_datasets.py` | Created; local run pending |
| SHA-256 helper | `fetch_and_hash.py` | Path handling corrected; no approved downloads configured |
| DPP evidence log | `dpp_snapshot_log.csv` | Created; snapshots pending |
| Week 2 documentation | README, architecture, technology stack, audit, completion report | Created |

## Outstanding acceptance evidence

| Requirement | Current status | What closes it |
|---|---|---|
| Human source verification | Pending | Check each citation, bibliographic details, disease relevance and access |
| Dataset measurements | Pending | Run the inventory utility on the four local dataset folders |
| Dataset licence review | Pending | Read each dataset's original source page and licence file |
| DPP registered/banned list snapshots | Pending | Save the actual linked files with capture date and source URL |
| Downloaded-document hashes | Pending | Add approved URLs, download files and verify manifest rows |
| Staging reconciliation | Pending | Reconcile 23 staging rows against the 61-row canonical register |
| GitHub Actions Week 2 CI | Pending | Confirm the corrected workflow run is green |

## Important limitations

- Three sources per disease is a register metadata threshold, not an assessment of scientific quality.
- Pakistan-specific detection is based on text markers in source metadata and requires human confirmation.
- Dataset counts, class distributions, duplicates, and image readability have not been measured until the local utility is run.
- Exact duplicate detection uses full-file SHA-256 in the inventory utility; this does not establish that two different images are visually equivalent.
- The hash manifest must remain empty until files are actually downloaded.
- Do not redistribute source documents unless their terms permit it.

## Completion decision

The Week 2 scripts, reports, and documentation are prepared. Week 2 should not be marked fully evidence-complete until the local dataset inspection, source/licence review, DPP snapshots, staging reconciliation, and CI confirmation are finished.
