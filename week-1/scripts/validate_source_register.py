"""Validate the Week 1 agricultural research source register."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

REGISTER = Path(__file__).resolve().parents[1] / "knowledge" / "source_register.csv"

REQUIRED_COLUMNS = [
    "source_id",
    "title",
    "authors",
    "publisher",
    "year",
    "type",
    "tier",
    "url_or_doi",
    "licence",
    "crops",
    "diseases",
    "pages_used",
    "language",
    "access_date",
    "verified_by",
    "verification_status",
    "notes",
]

VALID_TIERS = {"T1", "T2", "T3", "T4"}
VALID_STATUSES = {"pending", "in_review", "verified", "rejected"}


def validate_register(path: Path = REGISTER) -> list[str]:
    """Return validation errors. An empty list means the CSV structure is valid."""
    errors: list[str] = []

    if not path.exists():
        return [f"Source register not found: {path}"]

    with path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            return ["Source register is empty. Add the required CSV header."]

        missing_columns = [column for column in REQUIRED_COLUMNS if column not in reader.fieldnames]
        if missing_columns:
            return [f"Missing required columns: {', '.join(missing_columns)}"]

        seen_ids: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue

            source_id = (row.get("source_id") or "").strip()
            if not source_id:
                errors.append(f"Line {line_number}: source_id is required.")
            elif source_id in seen_ids:
                errors.append(f"Line {line_number}: duplicate source_id '{source_id}'.")
            else:
                seen_ids.add(source_id)

            for field in ("title", "publisher", "type", "tier", "url_or_doi", "licence",
                          "crops", "diseases", "access_date", "verification_status"):
                if not (row.get(field) or "").strip():
                    errors.append(f"Line {line_number}: {field} is required.")

            tier = (row.get("tier") or "").strip()
            if tier and tier not in VALID_TIERS:
                errors.append(
                    f"Line {line_number}: invalid tier '{tier}'. Use T1, T2, T3, or T4."
                )

            status = (row.get("verification_status") or "").strip()
            if status and status not in VALID_STATUSES:
                errors.append(
                    f"Line {line_number}: invalid verification_status '{status}'. "
                    f"Use {', '.join(sorted(VALID_STATUSES))}."
                )

    return errors


def main() -> int:
    errors = validate_register()
    if errors:
        print("Source register validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Source register structure and populated rows are valid.")
    print("Reminder: this script does not verify source accuracy or licence terms.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
