# Week 2 progress — Days 6–10

Use this page to understand the task and record evidence. Work as one contributor; no team branches or peer reviews are assumed.

## Day 6 — Rice T1 collection

**What T1 means:** authoritative sources such as IRRI, FAO, government agriculture departments and official extension/research institutes.

**What to do:** open the IRRI rice disease fact sheets and diagnostic guide, check that the links work, download only where access permits, and record the exact access date and SHA-256 hash for each local file.

- [ ] IRRI disease fact-sheet page checked
- [ ] IRRI diagnostic guide link checked
- [ ] Lawfully accessible rice files downloaded to `week-2/sources/rice/`
- [ ] Source title, URL, access date and rights recorded in `source_collection_log.csv`
- [ ] SHA-256 recorded in `SHA256SUMS.csv`

**Understand it:** SHA-256 is a fingerprint of a file. If even one byte changes, its hash will normally change. It helps prove which exact copy you collected; it does not prove that the document is accurate.

## Day 7 — Wheat/cotton T1 and DPP snapshots

- [ ] CIMMYT wheat guide record checked
- [ ] CCRI pathology page checked
- [ ] CCRI Annual Progress Report 2023–24 saved or access details recorded
- [ ] DPP registered pesticide list page captured with access date
- [ ] DPP banned pesticide list page captured with access date
- [ ] Downloaded snapshot filenames and hashes recorded where files are downloaded

**Understand it:** DPP is Pakistan's Department of Plant Protection. Its official lists are regulatory references. Save dated snapshots because web pages and downloadable lists can change. Never treat an old snapshot as proof of today's registration status.

## Day 8 — T2 research and gaps

- [ ] Identify the priority disease gaps in the canonical register
- [ ] Find peer-reviewed papers from journal/publisher pages or DOI records
- [ ] Confirm paper title, authors, journal, year and disease relevance
- [ ] Add new rows to `../week-1/knowledge/source_register.csv` (do not make a duplicate master register)
- [ ] Record exact pages/sections and licence/access terms
- [ ] Leave unconfirmed details as pending

**Understand it:** T2 means peer-reviewed research papers/reviews. A DOI is a persistent identifier, but a DOI alone does not prove that a paper is peer-reviewed or relevant.

## Day 9 — Dataset inventory

- [ ] Inspect each dataset folder and its own README/metadata/licence
- [ ] Count images per class, not just total files
- [ ] Identify train/validation/test splits and duplicates if metadata permits
- [ ] Record whether images are field or laboratory/controlled images; use `unknown` if not stated
- [ ] Record source URL, licence and permitted use
- [ ] Complete `dataset_inventory.csv`

**Understand it:** a dataset inventory is an audit sheet. It tells us what we have, where it came from, which disease classes it contains, how many images exist, and whether we are allowed to use them. Do not infer image origin from how a photo looks.

## Day 10 — 60-source checkpoint

- [ ] Canonical source register has at least 60 records
- [ ] Every one of the 18 diseases has at least 3 relevant sources
- [ ] At least 1 Pakistan-specific source exists for rice, wheat and cotton
- [ ] No source with prohibited/unknown reuse rights is ingested
- [ ] Coverage report and CI checks reviewed

**Understand it:** 60 total records is not enough by itself. The distribution matters: three sources for each of 18 diseases means 54 disease-linked source assignments, plus Pakistan-specific crop coverage. One source may support more than one disease only when the document genuinely covers each disease.

## Final status

Do not mark Week 2 complete until all Day 6–10 evidence and the Day 10 coverage checks are actually present. Blank values and pending states are honest; invented metadata is not evidence.
