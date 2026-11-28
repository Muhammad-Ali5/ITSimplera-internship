"""Check cumulative source coverage against the official 18 diseases."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "week-1" / "knowledge" / "source_register.csv"
OUT = ROOT / "week-2" / "reports" / "disease_source_coverage.csv"

OFFICIAL = [
    ("R1", "rice", "Rice Blast"), ("R2", "rice", "Bacterial Leaf Blight"),
    ("R3", "rice", "Sheath Blight"), ("R4", "rice", "Brown Spot"),
    ("R5", "rice", "False Smut"), ("R6", "rice", "Rice Tungro"),
    ("W1", "wheat", "Leaf Rust"), ("W2", "wheat", "Stripe Rust"),
    ("W3", "wheat", "Stem Rust"), ("W4", "wheat", "Powdery Mildew"),
    ("W5", "wheat", "Spot Blotch"), ("W6", "wheat", "Loose Smut"),
    ("C1", "cotton", "Cotton Leaf Curl Disease"), ("C2", "cotton", "Bacterial Blight"),
    ("C3", "cotton", "Root Rot"), ("C4", "cotton", "Boll Rot"),
    ("C5", "cotton", "Anthracnose"), ("C6", "cotton", "Myrothecium Leaf Spot"),
]
NAME2ID = {
    "rice blast": "R1", "bacterial leaf blight": "R2", "sheath blight": "R3",
    "brown spot": "R4", "false smut": "R5", "rice tungro": "R6",
    "leaf rust": "W1", "stripe rust": "W2", "yellow rust": "W2",
    "stem rust": "W3", "powdery mildew": "W4", "spot blotch": "W5",
    "loose smut": "W6", "cotton leaf curl disease": "C1",
    "bacterial blight": "C2", "root rot": "C3", "boll rot": "C4",
    "anthracnose": "C5", "myrothecium leaf spot": "C6",
}
PK = re.compile(r"Pakistan|Punjab|Sindh|PARC|CCRI|NIAB|UAF|AARI|Faisalabad|Peshawar|Vehari|Multan|NIBGE", re.IGNORECASE)


def disease_ids(value: str) -> set[str]:
    found = set(re.findall(r"\b[RWC][1-6]\b", value, re.IGNORECASE))
    lower = value.lower()
    for name, disease_id in NAME2ID.items():
        if name in lower:
            # Ambiguous shared names are resolved using crop context below.
            found.add(disease_id)
    return found


def main() -> int:
    if not REGISTER.is_file():
        print(f"Missing register: {REGISTER}", file=sys.stderr)
        return 2
    with REGISTER.open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))
    ids = {item[0] for item in OFFICIAL}
    coverage = {d: {"sources": set(), "t1": set(), "t2": set(), "pk": set()} for d in ids}
    for record in records:
        crop = (record.get("crops") or "").lower()
        evidence = " ".join(record.get(k, "") or "" for k in ("title", "notes", "publisher", "authors"))
        disease_text = record.get("diseases", "") or ""
        matched = disease_ids(disease_text)
        # Resolve generic disease names by crop to avoid assigning cotton blight to rice.
        if "bacterial blight" in disease_text.lower():
            matched.discard("C2" if crop != "cotton" else "R2")
            matched.add("C2" if crop == "cotton" else "R2")
        for disease_id in matched & ids:
            entry = coverage[disease_id]
            entry["sources"].add(record["source_id"])
            entry["t1" if record.get("tier") == "T1" else "t2"].add(record["source_id"])
            if PK.search(evidence):
                entry["pk"].add(record["source_id"])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["disease_id", "crop", "disease_name", "total_unique_sources", "T1_sources",
                         "T2_sources", "Pakistan_specific_sources", "coverage_status", "missing_requirements"])
        errors = []
        for disease_id, crop, name in OFFICIAL:
            entry = coverage[disease_id]
            count = len(entry["sources"])
            ok = count >= 3
            writer.writerow([disease_id, crop, name, count, len(entry["t1"]), len(entry["t2"]),
                             len(entry["pk"]), "MEETS (>=3)" if ok else "BELOW MIN",
                             "" if ok else f"needs {3-count} more"])
            if not ok:
                errors.append(f"{disease_id} {name}: {count} sources, need at least 3")
    if len(records) < 60:
        errors.append(f"Register has {len(records)} rows, need at least 60")
    for crop in ("rice", "wheat", "cotton"):
        crop_ids = [d for d, c, _ in OFFICIAL if c == crop]
        if not any(coverage[d]["pk"] for d in crop_ids):
            errors.append(f"No Pakistan-specific source detected for {crop}")
    if errors:
        print("Coverage check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Coverage check passed: {len(records)} records; all 18 diseases have >=3 sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
