# IT Simplera Crop Disease Assistant

An evidence‑grounded agricultural information assistant for **rice, wheat, and cotton
in Pakistan**, covering **18 diseases** (six per crop). The system is advisory — it must
cite its sources and never replace a plant pathologist or agriculture extension officer.

> **Status:** Weeks 1–2 (foundation + source collection) are built and documented.
> The RAG/agent system, image classifier, API and UI are later phases (not yet built).
> See each week's `COMPLETION_REPORT.md` for honest, evidence‑backed status.

## Official 18 diseases

- **Rice:** R1 Rice Blast · R2 Bacterial Leaf Blight · R3 Sheath Blight · R4 Brown Spot · R5 False Smut · R6 Rice Tungro *(virus)*
- **Wheat:** W1 Leaf Rust · W2 Stripe Rust · W3 Stem Rust · W4 Powdery Mildew · W5 Spot Blotch · W6 Loose Smut
- **Cotton:** C1 CLCuD *(virus)* · C2 Bacterial Blight · C3 Root Rot · C4 Boll Rot · C5 Anthracnose · C6 Myrothecium Leaf Spot

## Documentation

### Week 1 — Foundation (repo, workflow, source register, CI)
- [week-1/README.md](week-1/README.md)
- [week-1/COMPLETION_REPORT.md](week-1/COMPLETION_REPORT.md)
- [week-1/ARCHITECTURE.md](week-1/ARCHITECTURE.md)
- [week-1/TECHNOLOGY_STACK.md](week-1/TECHNOLOGY_STACK.md)
- [week-1/AUDIT_REPORT.md](week-1/AUDIT_REPORT.md)

### Week 2 — Source collection & verification (Days 6–10)
- [week-2/README.md](week-2/README.md)
- [week-2/COMPLETION_REPORT.md](week-2/COMPLETION_REPORT.md)
- [week-2/ARCHITECTURE.md](week-2/ARCHITECTURE.md)
- [week-2/TECHNOLOGY_STACK.md](week-2/TECHNOLOGY_STACK.md)
- [week-2/AUDIT_REPORT.md](week-2/AUDIT_REPORT.md)

### Key artefacts
- Canonical source register (61 sources): [week-1/knowledge/source_register.csv](week-1/knowledge/source_register.csv)
- Disease coverage matrix (all 18 ≥3): [week-2/reports/disease_source_coverage.csv](week-2/reports/disease_source_coverage.csv)

## Current snapshot

| Item | Value |
|------|-------|
| Registered sources | 61 (16 T1 · 45 T2) |
| Per official disease | all 18 ≥3 (range 4–8) |
| Pakistan‑relevant | rice 13 · wheat 15 · cotton 18 |
| Verification | 18 `in_review` · 43 `pending` · 0 human‑`verified` |
| Local checks | validator ✅ · pytest 7 ✅ · coverage ✅ · ruff ✅ |

## Safety non‑negotiables

Rice Tungro (R6) and Cotton Leaf Curl Disease (C1) are **viral** — never described as
curable with fungicides or bactericides. No pesticide names, doses or schedules are
invented; chemical guidance requires current official **DPP** registration. "Free to
read" ≠ "free to reuse" — licence/access is recorded per source.

## Working rhythm

Solo‑maintained repository on `main`. Local workflow: edit → run validator + pytest +
ruff → commit → push → confirm GitHub Actions. See [week-1/CONTRIBUTING.md](week-1/CONTRIBUTING.md).
