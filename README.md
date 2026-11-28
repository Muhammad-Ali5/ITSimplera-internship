# IT Simplera Crop Disease Assistant

An individual internship project focused on building an evidence-grounded crop disease information assistant for rice, wheat, and cotton in Pakistan.

## Project status

- **Week 1:** repository foundation, source register, validator, tests, and CI are in place. Research-source verification remains in progress.
- **Week 2:** the cumulative register contains 61 records and the coverage matrix maps the official 18 diseases. DPP snapshots, document downloads and hashes, dataset measurements, and human source verification remain outstanding.
- **Weeks 3–8:** retained as existing project planning/workspace. This update does not change them.

## Weekly documentation

- [Week 1 README](week-1/README.md)
- [Week 1 audit](week-1/AUDIT_REPORT.md)
- [Week 1 completion report](week-1/COMPLETION_REPORT.md)
- [Week 1 architecture](week-1/ARCHITECTURE.md)
- [Week 1 technology stack](week-1/TECHNOLOGY_STACK.md)
- [Week 2 README](week-2/README.md)
- [Week 2 audit](week-2/AUDIT_REPORT.md)
- [Week 2 completion report](week-2/COMPLETION_REPORT.md)
- [Week 2 architecture](week-2/ARCHITECTURE.md)
- [Week 2 technology stack](week-2/TECHNOLOGY_STACK.md)

## Key evidence

- Canonical cumulative source register: [week-1/knowledge/source_register.csv](week-1/knowledge/source_register.csv)
- Week 2 disease coverage: [week-2/reports/disease_source_coverage.csv](week-2/reports/disease_source_coverage.csv)
- Dataset inventory: [week-2/datasets/dataset_inventory.csv](week-2/datasets/dataset_inventory.csv)
- Dataset inspection utility: [week-2/datasets/inspect_datasets.py](week-2/datasets/inspect_datasets.py)
- Source coverage checker: [week-2/scripts/check_coverage.py](week-2/scripts/check_coverage.py)
- Download and hash helper: [week-2/fetch_and_hash.py](week-2/fetch_and_hash.py)
- Hash register: [week-2/SHA256SUMS.csv](week-2/SHA256SUMS.csv)

## Important research status

A populated source register or passing automated check does not prove that a source is authentic, relevant, or reusable. All source records remain pending or in review until human verification is completed. Do not use unverified chemical guidance. The registered and banned pesticide snapshots from Pakistan's Department of Plant Protection are still required before chemical recommendations can be supported.

The original internship brief in the repository is the source of truth for scope and acceptance requirements.