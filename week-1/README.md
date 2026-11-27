# IT Simplera Crop Disease Assistant

An evidence-grounded agricultural advisory assistant for rice, wheat, and cotton in Pakistan.

> **Project status:** Week 1 foundation. The Week 1 foundation includes project documentation, a research-source register template, a source-register validator, tests, a contribution guide, and GitHub Actions CI. The 30-source research target is tracked separately and is not complete until the entries have been researched and checked. The ingestion pipeline, OCR, disease knowledge cards, retrieval system, LangGraph agent, image classifier, API, and user interface are planned for later phases and are not implemented in Week 1.

## 1. Project overview

The Crop Disease Assistant is intended to help farmers, agriculture students, extension workers, agronomists, and field-support teams understand possible crop diseases from described symptoms. Users will be able to provide text in English, Urdu, or Roman Urdu. Image input may be supported only for disease classes with sufficient licensed and validated image data.

The assistant will return likely disease candidates, explain the supporting evidence, and provide prevention and management information with traceable references.

### Important limitation

This is an advisory information system. It does not replace laboratory diagnosis, field inspection, a plant pathologist, or an agriculture extension officer. If evidence is weak, conflicting, or outside the supported scope, the system must ask for clarification or recommend expert help instead of guessing.

## 2. Initial project scope

The first release covers three crops and 18 diseases, with six diseases per crop.

### Rice

1. Rice Blast
2. Bacterial Leaf Blight
3. Sheath Blight
4. Brown Spot
5. False Smut
6. Rice Tungro

### Wheat

1. Leaf Rust (Brown Rust)
2. Stripe Rust (Yellow Rust)
3. Stem Rust (Black Rust)
4. Powdery Mildew
5. Spot Blotch
6. Loose Smut

### Cotton

1. Cotton Leaf Curl Disease
2. Bacterial Blight (Angular Leaf Spot)
3. Root Rot
4. Boll Rot
5. Anthracnose
6. Myrothecium Leaf Spot

## 3. Project priorities and safety rules

The main release priorities are:

- Evidence-grounded answers with accurate, traceable citations.
- Clear communication of uncertainty and likely alternatives.
- A reliable no-answer path when evidence is insufficient.
- No invented pesticide names, doses, mixtures, intervals, or spray schedules.
- Chemical information only when supported by a current official registration and product label or official recommendation.
- Correct handling of viral diseases. Rice Tungro and Cotton Leaf Curl Disease must not be described as curable with fungicides or bactericides.
- Respect for document licences and copyright. Do not collect or ingest pirated or unauthorised material.

The assistant must not present a suspected disease as a confirmed diagnosis.

## 4. Week 1 objectives

Week 1 is the project-foundation phase. Its targets are:

1. Establish the GitHub repository and team workflow.
2. Prepare the initial project folder structure.
3. Add a contribution guide and automated quality checks.
4. Create the research-source register and its validator.
5. Record at least 30 research sources with licence or access terms by the Day 5 checkpoint.

The source-register template is in `knowledge/source_register.csv`.

## 5. Research-source policy

Use the following source tiers when evaluating material:

| Tier | Source type | Permitted use |
|---|---|---|
| T1 | Government, CGIAR, FAO, and official extension sources | Primary support for local recommendations. Chemical claims also require current registration and label checks. |
| T2 | Peer-reviewed research papers and reviews | Disease biology, symptoms, and epidemiology. Chemical advice still requires T1 confirmation. |
| T3 | Purchased or library-licensed reference books | Use only where lawful access exists. Record page references and do not redistribute copyrighted text. |
| T4 | Datasets, news, informal notes, and contextual material | May support dataset discovery or context, but must not be the basis for treatment advice. |

For every source, record its bibliographic details, URL or DOI, licence/access terms, relevant crop and disease, pages or sections used, access date, reviewer, and verification status. Prefer sources from the last ten years for management advice. Older sources may be useful for disease biology and symptoms but should be flagged as potentially dated.

### Initial research starting points

These are starting points, not automatically verified sources. Check availability, bibliographic details, relevance, current status, and usage rights before adding a record:

- IRRI Rice Knowledge Bank: https://www.knowledgebank.irri.org/training/fact-sheets/pest-management/diseases
- IRRI, *Diagnosis of Common Diseases of Rice*: https://www.knowledgebank.irri.org/images/docs/diagnostic-of-common-diseases-of-rice.pdf
- CIMMYT wheat disease guide: https://hdl.handle.net/10883/1115
- CIMMYT repository: https://repository.cimmyt.org/handle/10883/3219
- Central Cotton Research Institute (CCRI): https://ccri.gov.pk/
- CCRI reports: https://ccri.gov.pk/reports.html
- Department of Plant Protection, Pakistan: https://plantprotection.gov.pk/
- Punjab Agriculture Department: https://agripunjab.punjab.gov.pk/
- Pakistan Agricultural Research Council: https://www.parc.gov.pk/
- National Institute for Biotechnology and Genetic Engineering: https://www.niab.org.pk/
- Ayub Agricultural Research Institute: https://aari.punjab.gov.pk/
- FAO: https://www.fao.org/

## 6. Week 1 repository structure

The project files for this phase live in `week-1/`. GitHub Actions and issue templates must live in the repository-level `.github/` directory so GitHub can discover them:

```text
crop-disease-assistant/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── task.yml
│   └── workflows/
│       └── ci.yml
├── knowledge/
│   └── source_register.csv
├── scripts/
│   └── validate_source_register.py
├── tests/
│   └── test_source_register.py
├── .gitignore
├── CONTRIBUTING.md
├── README.md
├── pyproject.toml
└── requirements-dev.txt
```

Future implementation folders such as `app/`, `ingestion/`, `data/`, `eval/`, and `ui/` will be added when their respective phases begin. They are intentionally not created as empty folders in Week 1.

## 7. Development setup

### Requirements

- Python 3.11
- Git
- GitHub account
- VS Code or another Python editor

### Windows PowerShell setup

```powershell
# Clone your GitHub repository after creating it
git clone https://github.com/<YOUR_GITHUB_USERNAME>/crop-disease-assistant.git
cd crop-disease-assistant

# Create and activate a virtual environment
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install development tools
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

If PowerShell blocks virtual-environment activation, run this for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 8. Validate the source register

The CSV file starts with its required header. Add one source per row and complete the relevant fields.

Run the validator:

```powershell
python scripts/validate_source_register.py
```

Run tests:

```powershell
pytest
```

Run the linter:

```powershell
ruff check .
```

The validator checks the required columns, duplicate or empty source IDs, missing key metadata in populated rows, and invalid source-tier values. A source marked as `verified` should have been checked by a person; the script does not independently verify the source or its licence.

## 9. Git and contribution workflow

Use the following branch approach:

- `main`: stable project branch.
- `develop`: integration branch for ongoing work.
- `feature/<short-task-name>`: individual task branches.

Recommended workflow:

1. Create or select a GitHub issue before starting a task.
2. Create a feature branch from `develop`.
3. Make a small, focused change.
4. Run the validator, tests, and linter locally.
5. Push the branch and open a pull request into `develop`.
6. Request review before merging.
7. Keep `main` stable; merge reviewed work from `develop` when a milestone is accepted.

See [CONTRIBUTING.md](CONTRIBUTING.md) for commit and pull-request guidance.

## 10. Week 1 acceptance checklist

- [ ] GitHub repository created and accessible to the team.
- [ ] Team members can clone the repository.
- [ ] `main` branch is available.\n- [ ] Create and agree on a `develop` branch with the team if the internship workflow requires it.
- [ ] Week 1 folder structure is committed.
- [ ] README and contribution guide are available.
- [ ] GitHub Actions workflow runs linting and tests.
- [ ] Source-register CSV has the required columns.
- [ ] Source-register validator runs successfully.
- [ ] At least 30 genuine sources are recorded with checked licence/access terms by Day 5.
- [ ] Week 1 review and demonstration completed.

## 11. Current development status

This repository template represents the Week 1 foundation only. Do not claim that the 30-source target, expert review, disease cards, or system capabilities are complete until the work has actually been performed and checked.

## 12. Disclaimer

The planned assistant provides agricultural information for educational and field-support purposes. It is not a substitute for professional diagnosis or official local guidance. Users should consult a qualified plant pathologist or local agriculture extension officer before taking treatment decisions, especially before applying any pesticide.
