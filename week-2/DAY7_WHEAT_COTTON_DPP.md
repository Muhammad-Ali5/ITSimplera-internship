# Day 7 — Wheat, Cotton & DPP Source Collection

**Date:** 2026-11-28 (Asia/Karachi)
**Scope:** Official wheat **W1–W6** and cotton **C1–C6** (PDF §3.2, §3.3) + Department of Plant Protection pesticide lists
**Status:** Partial — several Pakistan T1 pages verified; **DPP pesticide lists NOT yet captured** (critical gap)

> Same environment limits as Day 6: no downloads/hashes produced here; pages
> verified only where automated reading succeeded.

## Official diseases (exact IDs)

**Wheat:** W1 Leaf Rust (*Puccinia triticina*) · W2 Stripe Rust (*P. striiformis* f. sp. *tritici*) · W3 Stem Rust (*P. graminis* f. sp. *tritici*) · W4 Powdery Mildew (*Blumeria graminis* f. sp. *tritici*) · W5 Spot Blotch (*Bipolaris sorokiniana*) · W6 Loose Smut (*Ustilago tritici*)

**Cotton:** C1 CLCuD (begomovirus + betasatellite — **virus**) · C2 Bacterial Blight (*Xanthomonas citri* pv. *malvacearum*) · C3 Root Rot (*Rhizoctonia solani* / *Macrophomina phaseolina*) · C4 Boll Rot (complex) · C5 Anthracnose (*Colletotrichum gossypii*) · C6 Myrothecium Leaf Spot (*Myrothecium/Paramyrothecium roridum*)

## Wheat Tier 1

| source_id | Source | Publisher | Covers | Verify |
|-----------|--------|-----------|--------|--------|
| W2S-004 | Wheat Diseases and Pests: A Guide for Field Identification | CIMMYT | W1–W6 | pending (handle to open) |
| W2S-005 | Practical Guide to ID of Selected Diseases of Wheat & Barley (Gilchrist et al., 1997) | CIMMYT | W1–W6 | pending |
| W2S-006 | **Bunt and Smut Diseases of Wheat** (Wilcoxson & Saari, eds., 1996) | CIMMYT | W6 Loose Smut (chapter) | **in_review — content confirmed** |
| W2S-007 | Bread Wheat: Improvement and Production | FAO | W1–W6 | pending |

**W2S-006 checked:** title, editors, ISBN 968‑6923‑37‑3 and the dedicated
**Loose Smut** chapter were confirmed directly from the CIMMYT repository
full‑text. The CIMMYT repository is reachable; the other CIMMYT handles
(W2S‑004/005) still need opening to confirm they resolve.

## Cotton Tier 1 (Pakistan‑specific — strong finds)

| source_id | Source | Publisher | Covers | Verify |
|-----------|--------|-----------|--------|--------|
| W2S-009 | CCRI Reports — Annual Progress Report 2023‑2024 | CCRI Multan | C1–C6 context | **in_review — page live** |
| W2S-010 | CCRI Cotton Pathology page | CCRI Multan | C2, C3, C4 | **in_review — content retrieved** |
| W2S-011 | Diseases of Cotton & their control | Govt of Sindh — Agriculture | C1, C2, C3, C4, C5 | **in_review — content retrieved** |

**Checked:** CCRI reports page is live (footer “© 2016 CCRI, Multan”) and lists
the **Annual Progress Report 2023‑2024** PDF. The CCRI **pathology** page gives
Pakistan context for bacterial blight (*X. campestris* pv. *malvacearum*), boll
rot and seed‑borne fungi. The **Sindh Agriculture** page covers root rot, boll
rot, anthracnose, bacterial blight and CLCV — i.e. it alone touches **four of
the five** official cotton gap diseases with Pakistan framing.

## Department of Plant Protection (DPP) — pesticide lists

| source_id | Source | URL | Status |
|-----------|--------|-----|--------|
| W2S-012 | DPP registered & banned pesticide information | plantprotection.gov.pk | **PENDING — fetch blocked** |
| W2S-013 | Agricultural Pesticides Rules (Pakistan), FAOLEX | faolex.fao.org/docs/pdf/pak4115.pdf | pending |
| W2S-008 | FAO International Code of Conduct on Pesticide Management | fao.org/pest-and-pesticide-management/… | pending |

> **⚠️ Critical honest flag.** The DPP site (`plantprotection.gov.pk`) could
> **not** be fetched here (robots unreachable). I therefore have **not** captured
> the official **registered** pesticide list or the **banned** pesticide list,
> and no dated snapshot exists yet. The whole chemical‑safety gate (PDF §10.1
> step 9, §4.2 rule 3) depends on this. **This is the single most important
> outstanding item.** When you open it:
> - find the current **registered** list and the **banned** list,
> - record page URL + displayed/update date + access date,
> - save a dated snapshot (PDF/HTML) under `sources/dpp/`,
> - **never** treat a historical list as proof of current registration, and
> - **never** invent a pesticide name, dose, interval or schedule.

## Downloads & SHA‑256 evidence

**None in this environment** (see Day 6 note). `scripts/fetch_and_hash.py`
already lists the CCRI Annual Report 2023‑2024 and the FAOLEX Rules PDF; add the
DPP list URL once located, then run it on your machine.

## Outstanding for Day 7

- [ ] **Capture DPP registered + banned pesticide lists** (dated snapshot). ← top priority
- [ ] Open CIMMYT handles 10883/1115 and 10883/3219; confirm they resolve.
- [ ] Download CCRI AR 2023‑2024 + FAOLEX Rules; hash them.
- [ ] Confirm reuse/licence terms for every institutional page.
