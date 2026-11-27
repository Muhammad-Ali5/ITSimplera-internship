# Contributing to IT Simplera Crop Disease Assistant

Thank you for contributing.

## Scope and evidence rules
- Work only on the task assigned for the current project phase.
- Use reliable sources and record the source URL or DOI, publisher, year, access date, licence or access condition, crop, disease, and pages or sections used.
- Do not add pirated or unauthorised material.
- Do not mark a source as verified until a person has checked its identity, relevance, availability, and usage rights.
- Do not invent pesticide names, doses, mixtures, intervals, or spray schedules.
- Chemical guidance requires a current official registration and product label or official recommendation.
- Never describe Rice Tungro or Cotton Leaf Curl Disease as curable with fungicides or bactericides.

## Git workflow
The repository currently uses the `main` branch. For collaborative work, create a short-lived branch for each task when branch permissions and team workflow are ready.

Suggested branch names:
- `docs/source-register-policy`
- `feat/source-register-validator`
- `test/source-register-validation`

## Commit messages
Use short, clear messages in the imperative mood:
- `docs: add contribution guide`
- `feat: add source register validator`
- `test: cover source register validation`

## Before submitting work
Run these commands from the `week-1` directory:

```powershell
python -m pip install -r requirements-dev.txt
python scripts/validate_source_register.py
pytest
ruff check .
```

Explain what changed, how it was checked, and link any relevant research sources in the pull request or task record.
