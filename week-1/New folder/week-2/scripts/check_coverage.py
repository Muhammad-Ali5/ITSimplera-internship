"""Week-2 coverage check against the official 18 diseases.

Reads the canonical register (week-1/knowledge/source_register.csv), maps both
the legacy disease names and the official R#/W#/C# IDs onto the 18 official
diseases, and verifies the Day-10 targets:
  * >= 60 populated source rows,
  * >= 3 relevant sources for every official disease,
  * >= 1 Pakistan-specific source per crop.
Writes week-2/reports/disease_source_coverage.csv and exits non-zero on failure.
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
OFFICIAL_IDS = {oid for oid, _, _ in OFFICIAL}
NAME2ID = {
    "rice blast": "R1", "bacterial leaf blight": "R2", "sheath blight": "R3",
    "brown spot": "R4", "false smut": "R5", "rice tungro": "R6",
    "wheat rust (stripe/yellow rust)": "W2", "powdery mildew": "W4",
    "spot blotch": "W5", "loose smut": "W6",
    "cotton leaf curl disease": "C1", "bacterial blight": "C2", "root rot": "C3",
}
PK = re.compile(
    r"Pakistan|Punjab|Sindh|PARC|CCRI|NIAB|UAF|AARI|Faisalabad|Peshawar|Vehari|Multan|NIBGE"
)


def ids_for(diseases: str) -> set[str]:
    found = set(re.findall(r"[RWC]\d", diseases))
    low = diseases.lower()
    for name, did in NAME2ID.items():
        if name in low:
            found.add(did)
    return {i for i in found if i in OFFICIAL_IDS}


def main() -> int:
    rows = list(csv.DictReader(REGISTER.open(encoding="utf-8-sig")))
    cov = {oid: {"all": set(), "T1": set(), "T2": set(), "PK": set()} for oid in OFFICIAL_IDS}
    for r in rows:
        blob = r["title"] + r["notes"] + r["publisher"] + r["authors"]
        for did in ids_for(r["diseases"]):
            cov[did]["all"].add(r["source_id"])
            cov[did]["T1" if r["tier"] == "T1" else "T2"].add(r["source_id"])
            if PK.search(blob):
                cov[did]["PK"].add(r["source_id"])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["disease_id", "crop", "disease_name", "total_unique_sources",
                    "T1_sources", "T2_sources", "Pakistan_specific_sources",
                    "coverage_status", "missing_requirements"])
        for oid, crop, name in OFFICIAL:
            c = cov[oid]
            tot = len(c["all"])
            ok = tot >= 3
            w.writerow([oid, crop, name, tot, len(c["T1"]), len(c["T2"]), len(c["PK"]),
                        "MEETS (>=3)" if ok else "BELOW MIN",
                        "" if ok else f"needs {3 - tot} more"])

    errors: list[str] = []
    if len(rows) < 60:
        errors.append(f"register has {len(rows)} rows; need >= 60.")
    for oid, crop, name in OFFICIAL:
        if len(cov[oid]["all"]) < 3:
            errors.append(f"{oid} {name}: only {len(cov[oid]['all'])} sources (need >= 3).")
    for crop in ("rice", "wheat", "cotton"):
        pk = set().union(*(cov[o]["PK"] for o, c, _ in OFFICIAL if c == crop))
        if not pk:
            errors.append(f"{crop}: no Pakistan-specific source.")

    if errors:
        print("Week 2 coverage check FAILED:")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"Week 2 coverage OK: {len(rows)} sources; all 18 diseases >= 3; Pakistan per crop satisfied.")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
