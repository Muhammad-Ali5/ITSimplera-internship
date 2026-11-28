"""Check register-level coverage for the official 18 crop diseases.

This script checks metadata associations only. It does not verify that a source
actually supports a disease claim or that its licence permits reuse.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "week-1" / "knowledge" / "source_register.csv"
OUT = ROOT / "week-2" / "reports" / "disease_source_coverage.csv"

OFFICIAL = [
    ("R1", "rice", "Rice Blast"),
    ("R2", "rice", "Bacterial Leaf Blight"),
    ("R3", "rice", "Sheath Blight"),
    ("R4", "rice", "Brown Spot"),
    ("R5", "rice", "False Smut"),
    ("R6", "rice", "Rice Tungro"),
    ("W1", "wheat", "Leaf Rust"),
    ("W2", "wheat", "Stripe Rust"),
    ("W3", "wheat", "Stem Rust"),
    ("W4", "wheat", "Powdery Mildew"),
    ("W5", "wheat", "Spot Blotch"),
    ("W6", "wheat", "Loose Smut"),
    ("C1", "cotton", "Cotton Leaf Curl Disease"),
    ("C2", "cotton", "Bacterial Blight"),
    ("C3", "cotton", "Root Rot"),
    ("C4", "cotton", "Boll Rot"),
    ("C5", "cotton", "Anthracnose"),
    ("C6", "cotton", "Myrothecium Leaf Spot"),
]
OFFICIAL_IDS = {disease_id for disease_id, _, _ in OFFICIAL}
NAME_TO_ID = {
    "rice blast": "R1",
    "bacterial leaf blight": "R2",
    "sheath blight": "R3",
    "brown spot": "R4",
    "false smut": "R5",
    "rice tungro": "R6",
    "leaf rust": "W1",
    "stripe rust": "W2",
    "yellow rust": "W2",
    "stem rust": "W3",
    "powdery mildew": "W4",
    "spot blotch": "W5",
    "loose smut": "W6",
    "cotton leaf curl disease": "C1",
    "root rot": "C3",
    "boll rot": "C4",
    "anthracnose": "C5",
    "myrothecium leaf spot": "C6",
}
PAKISTAN_MARKERS = re.compile(
    r"Pakistan|Punjab|Sindh|PARC|CCRI|NIAB|UAF|AARI|Faisalabad|"
    r"Peshawar|Vehari|Multan|NIBGE",
    re.IGNORECASE,
)


def disease_ids(disease_text: str, crop_text: str) -> set[str]:
    """Map explicit IDs and disease names, using crop to resolve blight."""
    found = set(re.findall(r"\b[RWC][1-6]\b", disease_text, re.IGNORECASE))
    text = disease_text.lower()
    crop = crop_text.lower()

    for name, disease_id in NAME_TO_ID.items():
        if name in text:
            found.add(disease_id)

    if "bacterial blight" in text:
        found.discard("C2")
        found.discard("R2")
        if "cotton" in crop:
            found.add("C2")
        if "rice" in crop:
            found.add("R2")

    return found & OFFICIAL_IDS


def main() -> int:
    if not REGISTER.is_file():
        print(f"Missing register: {REGISTER}", file=sys.stderr)
        return 2

    with REGISTER.open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))

    coverage = {
        disease_id: {"sources": set(), "t1": set(), "t2": set(), "pk": set()}
        for disease_id in OFFICIAL_IDS
    }

    for record in records:
        crop = record.get("crops", "") or ""
        disease_text = record.get("diseases", "") or ""
        evidence = " ".join(
            record.get(field, "") or ""
            for field in ("title", "notes", "publisher", "authors")
        )
        source_id = (record.get("source_id") or "").strip()
        tier = (record.get("tier") or "").strip().upper()

        if not source_id:
            continue

        for disease_id in disease_ids(disease_text, crop):
            item = coverage[disease_id]
            item["sources"].add(source_id)
            if tier == "T1":
                item["t1"].add(source_id)
            elif tier == "T2":
                item["t2"].add(source_id)
            if PAKISTAN_MARKERS.search(evidence):
                item["pk"].add(source_id)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "disease_id", "crop", "disease_name", "total_unique_sources",
            "T1_sources", "T2_sources", "Pakistan_specific_sources",
            "coverage_status", "missing_requirements",
        ])

        for disease_id, crop, name in OFFICIAL:
            item = coverage[disease_id]
            total = len(item["sources"])
            meets = total >= 3
            writer.writerow([
                disease_id, crop, name, total, len(item["t1"]), len(item["t2"]),
                len(item["pk"]), "MEETS (>=3)" if meets else "BELOW MIN",
                "" if meets else f"needs {3 - total} more",
            ])
            if not meets:
                errors.append(f"{disease_id} {name}: {total} sources; need at least 3")

    if len(records) < 60:
        errors.append(f"Register has {len(records)} rows; need at least 60")

    for crop in ("rice", "wheat", "cotton"):
        crop_diseases = [
            disease_id for disease_id, disease_crop, _ in OFFICIAL
            if disease_crop == crop
        ]
        if not any(coverage[disease_id]["pk"] for disease_id in crop_diseases):
            errors.append(f"No Pakistan-related source metadata detected for {crop}")

    if errors:
        print("Coverage check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Coverage check passed: {len(records)} records; "
        "all 18 diseases have at least 3 associated sources."
    )
    print("Note: this is a metadata check, not scientific or licence verification.")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
