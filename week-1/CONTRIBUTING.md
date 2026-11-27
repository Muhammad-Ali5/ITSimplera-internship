# Individual contribution workflow

This project is currently maintained by one intern. No team, reviewer, or multi-contributor workflow is assumed.

## Working alone
- Use the `main` branch for this individual internship repository.
- Make small, focused commits with clear messages.
- Before each commit, review the changed files and run the local checks.
- Keep research records traceable. Record the publication URL or DOI, bibliographic details, access date, relevant crop and disease, pages or sections used, and licence/access terms.
- Mark a source as `verified` only after checking its publication identity, relevance, availability, and rights. Otherwise use `pending` or `in_review`.

## Evidence and safety rules
- Do not add pirated or unauthorised material.
- Do not invent pesticide names, doses, mixtures, intervals, or spray schedules.
- Chemical guidance requires a current official registration and product label or official recommendation.
- Never describe Rice Tungro or Cotton Leaf Curl Disease as curable with fungicides or bactericides.
- A source being publicly viewable does not automatically mean its full text may be redistributed or ingested.

## Commit messages
Use short, clear messages:
- `docs: add individual workflow`
- `feat: add source register validator`
- `test: cover source register validation`
- `research: add verified rice references`

## Run checks from the `week-1` directory

```powershell
python -m pip install -r requirements-dev.txt
python scripts/validate_source_register.py
pytest
ruff check .
```

Record the test result and link the GitHub Actions run in the Week 1 evidence notes.
