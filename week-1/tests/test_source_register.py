"""Tests for the source-register validator."""

import csv

from scripts.validate_source_register import REQUIRED_COLUMNS, validate_register


def write_register(path, rows):
    with path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=REQUIRED_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def valid_row(source_id="SRC-001"):
    return {
        "source_id": source_id,
        "title": "Example research source",
        "authors": "Example author",
        "publisher": "Example publisher",
        "year": "2024",
        "type": "research article",
        "tier": "T2",
        "url_or_doi": "https://doi.org/10.1234/example",
        "licence": "Access terms to be checked",
        "crops": "wheat",
        "diseases": "leaf rust",
        "pages_used": "1-3",
        "language": "English",
        "access_date": "2026-11-27",
        "verified_by": "Not yet verified",
        "verification_status": "pending",
        "notes": "Test fixture only; not a real research source.",
    }


def test_header_only_register_is_valid(tmp_path):
    path = tmp_path / "source_register.csv"
    write_register(path, [])
    assert validate_register(path) == []


def test_valid_populated_row_is_valid(tmp_path):
    path = tmp_path / "source_register.csv"
    write_register(path, [valid_row()])
    assert validate_register(path) == []


def test_duplicate_source_ids_are_rejected(tmp_path):
    path = tmp_path / "source_register.csv"
    write_register(path, [valid_row(), valid_row()])
    assert any("duplicate source_id" in error for error in validate_register(path))


def test_invalid_tier_is_rejected(tmp_path):
    path = tmp_path / "source_register.csv"
    row = valid_row()
    row["tier"] = "T5"
    write_register(path, [row])
    assert any("invalid tier" in error for error in validate_register(path))


def test_missing_licence_is_rejected(tmp_path):
    path = tmp_path / "source_register.csv"
    row = valid_row()
    row["licence"] = ""
    write_register(path, [row])
    assert any("licence is required" in error for error in validate_register(path))


def test_expected_source_count_is_enforced(tmp_path):
    path = tmp_path / "source_register.csv"
    write_register(path, [valid_row()])
    errors = validate_register(path, expected_count=30)
    assert any("Expected 30 populated source rows" in error for error in errors)


def test_duplicate_doi_is_rejected(tmp_path):
    path = tmp_path / "source_register.csv"
    first = valid_row("SRC-001")
    second = valid_row("SRC-002")
    second["url_or_doi"] = first["url_or_doi"]
    write_register(path, [first, second])
    assert any("duplicate DOI/URL" in error for error in validate_register(path))
