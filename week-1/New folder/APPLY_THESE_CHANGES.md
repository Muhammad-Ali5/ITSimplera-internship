# How to apply these Week 1 + Week 2 changes

I could **not push** to your repo (this session has read‑only git access and the
desktop bridge to `E:\` was offline), so everything is delivered as files that
mirror your repo layout. Extract the zip at your **repo root** so paths line up.

## Files in this bundle (→ where they go)

| File | Replaces / adds |
|------|-----------------|
| `README.md` (repo root) | new — links to Week 1 + Week 2 docs |
| `week-1/knowledge/source_register.csv` | **replaces** (30 → 61 rows; originals preserved) |
| `week-1/scripts/validate_source_register.py` | **replaces** (expected_count 30 → 61) |
| `week-1/README.md` | replaces (adds doc links; 30→61 count note) |
| `week-1/COMPLETION_REPORT.md` | new (Part 10) |
| `week-1/ARCHITECTURE.md` | new (Part 10) |
| `week-1/TECHNOLOGY_STACK.md` | new (Part 10) |
| `week-1/AUDIT_REPORT.md` | new (Part 10) |
| `week-2/README.md` | replaces (adds doc links) |
| `week-2/COMPLETION_REPORT.md` | new (Part 10) |
| `week-2/ARCHITECTURE.md` | new (Part 10) |
| `week-2/TECHNOLOGY_STACK.md` | new (Part 10) |
| `week-2/AUDIT_REPORT.md` | new (Part 10) |
| `week-2/scripts/check_coverage.py` | new (Week‑2 CI gate) |
| `week-2/datasets/inspect_datasets.py` | new (run locally for real image counts) |
| `week-2/datasets/dataset_inventory.csv` | new/updated (counts pending) |
| `week-2/datasets/DATASET_INVENTORY_REPORT.md` | new |
| `week-2/reports/disease_source_coverage.csv` | new |
| `week-2/hashes/SHA256SUMS.csv` | new (header only until you download) |
| `.github/workflows/week-2-ci.yml` | new |

**Note on existing files preserved (not deleted):** your `week-2/DAY6/7/8_*.md`,
`WEEK2_PROGRESS.md`, `week2_source_register_additions.csv`, `source_collection_log.csv`,
`dpp_snapshot_log.csv`, `fetch_and_hash.py` stay as‑is. The new Part‑10 docs are the
canonical weekly documentation; the DAY files remain as working notes (the PDF asks not
to *create* new daily files — existing ones are preserved).

## Verify locally (same checks I ran; all passed here)

```bash
cd week-1
python -m pip install -r requirements-dev.txt
python scripts/validate_source_register.py     # expects 61 → OK
pytest                                          # 7 passed
ruff check .                                     # OK
cd ..
python week-2/scripts/check_coverage.py          # 61 sources; all 18 >=3; PK per crop OK
ruff check week-2/scripts week-2/datasets        # OK
```

## Then do the machine‑only steps

```bash
# real image counts (point at your Datasets folder)
python week-2/datasets/inspect_datasets.py "E:\Interships\ITSamplera solutions\Datasets"

# download permitted PDFs + compute SHA-256
python week-2/fetch_and_hash.py

# DPP: open the two list pages, save dated snapshots into week-2/sources/dpp/,
# then add their hashes. (Chemical-safety gate — highest priority.)
```

## Commit (only after you're happy — I did not commit)

```bash
git checkout -b week2-completion
git add week-1/knowledge/source_register.csv week-1/scripts/validate_source_register.py \
        week-1/AUDIT_REPORT.md week-2 .github/workflows/week-2-ci.yml
git commit -m "week2: merge sources to 61, add coverage/audit/dataset tooling and CI"
git push -u origin week2-completion
```

Then open the Actions tab and confirm both `week-1` and `week-2` workflows go green.
Nothing in Week 3+ or `/Datasets/` was touched.
