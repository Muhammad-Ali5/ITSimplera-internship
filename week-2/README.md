# Week 2 — Research Collection and Coverage

**Phase:** Days 6–10  
**Project:** IT Simplera Crop Disease Assistant  
**Status:** Partial. Register coverage targets are represented, while evidence and local inspection tasks remain outstanding.

## Objectives
- Collect Tier 1 institutional material for rice, wheat, and cotton.
- Add Tier 2 research to fill gaps in the official 18-disease scope.
- Record Pakistan's registered and banned pesticide references.
- Inventory the four locally held datasets without moving or modifying them.
- Maintain a cumulative source register and disease coverage report.

## Canonical files
- [Cumulative source register](../week-1/knowledge/source_register.csv)
- [Coverage matrix](reports/disease_source_coverage.csv)
- [Source collection log](source_collection_log.csv)
- [Week 2 source additions (research staging file)](week2_source_register_additions.csv)
- [Dataset inventory](datasets/dataset_inventory.csv)
- [Dataset inventory report](datasets/DATASET_INVENTORY_REPORT.md)
- [Dataset inspection script](datasets/inspect_datasets.py)
- [DPP snapshot log](dpp_snapshot_log.csv)
- [SHA-256 manifest](SHA256SUMS.csv)
- [Download and hash helper](fetch_and_hash.py)
- [Coverage checker](scripts/check_coverage.py)

## Official disease scope
Rice: R1 Rice Blast, R2 Bacterial Leaf Blight, R3 Sheath Blight, R4 Brown Spot, R5 False Smut, R6 Rice Tungro.  
Wheat: W1 Leaf Rust, W2 Stripe Rust, W3 Stem Rust, W4 Powdery Mildew, W5 Spot Blotch, W6 Loose Smut.  
Cotton: C1 Cotton Leaf Curl Disease, C2 Bacterial Blight, C3 Root Rot, C4 Boll Rot, C5 Anthracnose, C6 Myrothecium Leaf Spot.

## Current evidence status
The cumulative register contains 61 unique source IDs. The coverage report currently records at least three sources for each official disease and Pakistan-specific sources across all three crops. This is a register-level coverage result, not proof that all sources are human-verified or reusable.

The SHA-256 manifest currently has no document rows. DPP registered/banned list snapshots have not been captured. Dataset counts and duplicate checks have not yet been measured on the local dataset folders. These are open tasks, not completed deliverables.

## Important research controls
Do not ingest material without lawful access. Do not invent source metadata, hashes, pesticide names, doses, or schedules. Rice Tungro and Cotton Leaf Curl Disease are viral diseases and must not be described as curable with fungicides or bactericides. Chemical guidance requires current official registration and label checks.
