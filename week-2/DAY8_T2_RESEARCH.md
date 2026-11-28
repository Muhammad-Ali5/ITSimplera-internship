# Day 8 — Tier 2 Scientific Research Papers (gap filling)

**Date:** 2026-11-28 (Asia/Karachi)
**Goal:** Find ≥1 credible peer‑reviewed source for every **priority research gap** across the official 18 diseases.
**Status:** Gaps filled; several DOIs confirmed this session, a few still to confirm.

## The official gap list (from the internship PDF, §5.5)

> “locate current, credible sources for **cotton bacterial blight, root rot,
> boll rot, anthracnose** and **wheat loose smut**, preferably with Pakistan
> field evidence. Also obtain a T1/T2 source for **wheat powdery mildew
> management in Pakistan**.”

I also checked the diseases that had **zero** coverage after Week 1 because of
the scope mismatch (see README): **W1 Leaf Rust, W3 Stem Rust, C4 Boll Rot,
C5 Anthracnose, C6 Myrothecium Leaf Spot.**

## Papers found (Tier 2)

| source_id | Disease | Paper (short) | Journal | DOI / link | Status |
|-----------|---------|---------------|---------|-----------|--------|
| W2S-014 | **C4 Boll Rot** | First report of *Fusarium incarnatum‑equiseti* complex on cotton boll rot in **Pakistan** (Chohan & Abid, 2019) | Plant Disease | AGRIS record; APS DOI to confirm | pending |
| W2S-015 | **C5 Anthracnose** | Management of cotton anthracnose (*C. gossypii*) with fungicides (Yadav et al., 2025) | Indian J. Agric. Sciences | 10.56093/ijas.v95i9.166797 | in_review |
| W2S-016 | **C5 Anthracnose** | Pest categorisation of *Colletotrichum gossypii* (EFSA PLH, 2018) | EFSA Journal | 10.2903/j.efsa.2018.5305 | in_review |
| W2S-017 | **C6 Myrothecium** | Myrothecium leaf spot of cotton — first report (Meyer et al., Brazil) | Summa Phytopathologica | repositorio.unesp.br record; DOI to confirm | pending |
| W2S-018 | **C6 Myrothecium** | Cotton weeds as hosts of *M. roridum* — **Pakistan** (Tanveer et al., 1974) | Pakistan J. Botany | pakbs.org paper 4916 | pending |
| W2S-019 | **W4 Powdery Mildew** | High prevalence of wheat powdery mildew, N. Himalayan **Pakistan** (Rehman et al., 2019) | Sarhad J. Agriculture | 10.17582/journal.sja/2019/35.1.187.193 | in_review |
| W2S-020 | **W6 Loose Smut** | Stable resistance sources vs loose smut (Kumar et al., 2022) | J. Cereal Research (ICAR) | 10.25174/2582-2675/2022/119668 | in_review |
| W2S-021 | **W6 Loose Smut** | Genetic analysis of loose‑smut resistance (2020) | BMC Plant Biology | 10.1186/s12870-020-02525-x | in_review |
| W2S-022 | **W6 Loose Smut** | Loose‑smut infection assessment — **Pakistan/PARC** (Khanzada et al., 2000) | (confirm via AGRIS) | AGRIS record | pending |
| W2S-023 | **W1/W2/W3/W6 + rice** | Wheat & rice diseases in **Pakistan**: a review (Javaid & Anjum, 2005) | (confirm via AGRIS) | AGRIS record | pending |

**C2 Bacterial Blight** and **C3 Root Rot** are covered on the Tier‑1 side by the
Pakistan government pages logged on Day 7 (CCRI pathology W2S‑010; Sindh
Agriculture W2S‑011). If your Week‑1 register already holds a bacterial‑blight
(e.g. *Phytopathologia Mediterranea* “Bacterial blight of cotton”, 2015) or a
*Macrophomina* review, **map those to C2 / C3 rather than re‑adding** — I did not
duplicate them here because this environment could not read your Week‑1 register.

## How each was verified (honestly)

- **in_review** (9 rows): I retrieved the **DOI + abstract** (and usually the
  author list) from the publisher page, PubMed Central, or ICAR epubs **this
  session, 2026‑11‑28**. That is strong evidence — but **no human has opened
  them**, so they are not marked “verified”. A DOI alone is **not** proof of
  peer review (PDF caution); confirm journal standing when you review.
- **pending** (rows seen via AGRIS / repository index or where the DOI was not
  shown): confirm the full citation and DOI on the publisher page before use.
- Nothing was marked `verified`. Nothing was downloaded or ingested — only
  metadata was recorded (PDF §5.5 / §8 forbid ingesting copyrighted full text
  without rights).

## Coverage after Day 8 (official 18)

Every one of R1–R6, W1–W6, C1–C6 now has **at least one** Week‑2 source
(the additions CSV references all 18 IDs). Depth is uneven — see README §“Honest
coverage” for which diseases are thin (W1, W3, C6) and should get a dedicated
Pakistan paper next.

## Outstanding for Day 8

- [ ] Confirm APS DOI for Chohan & Abid 2019 (C4) and the SciELO DOI for the
      Myrothecium first report (C6).
- [ ] Confirm journal + DOI for the AGRIS‑only Pakistan records (W2S‑022, 023).
- [ ] Add a dedicated Pakistan paper for **W1 Leaf Rust** and **W3 Stem Rust**
      (currently only covered by the CIMMYT field guide + the 2005 PK review).
