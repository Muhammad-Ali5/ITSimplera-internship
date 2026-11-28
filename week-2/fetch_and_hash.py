#!/usr/bin/env python3
"""Download explicitly approved Week 2 documents and record SHA-256 hashes.

Run from the repository root:
    python week-2/fetch_and_hash.py

Only add a URL to DOWNLOADS after checking that downloading it is permitted.
The script stores files under week-2/sources/ and writes week-2/SHA256SUMS.csv.
It records failed downloads without inventing a hash. It does not make any
claim that a downloaded file may be redistributed or used for model training.
"""
from __future__ import annotations

import csv
import datetime
import hashlib
import os
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

WEEK2_DIR = Path(__file__).resolve().parent
MANIFEST = WEEK2_DIR / "SHA256SUMS.csv"
MAX_DOWNLOAD_BYTES = 100 * 1024 * 1024

# Add only documents whose download terms have been checked.
# Keep the list empty until each document has an explicit approval decision.
DOWNLOADS: list[tuple[str, str]] = []


def sha256_file(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return digest.hexdigest(), size


def download_one(relative_path: str, url: str) -> tuple[str, str, str, str, str]:
    destination = (WEEK2_DIR / relative_path).resolve()
    if WEEK2_DIR.resolve() not in destination.parents:
        raise ValueError(f"Destination must stay inside {WEEK2_DIR}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    request = urllib.request.Request(
        url, headers={"User-Agent": "ITSimplera-Week2-Research/1.0"}
    )

    temporary_path: Path | None = None
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            with tempfile.NamedTemporaryFile(
                mode="wb", dir=destination.parent, delete=False
            ) as temporary:
                temporary_path = Path(temporary.name)
                size = 0
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > MAX_DOWNLOAD_BYTES:
                        raise ValueError("Download exceeded the 100 MB safety limit")
                    temporary.write(chunk)

        digest, size = sha256_file(temporary_path)
        os.replace(temporary_path, destination)
        return (
            destination.name,
            str(destination.relative_to(WEEK2_DIR)),
            digest,
            str(size),
            timestamp,
        )
    except (OSError, urllib.error.URLError, ValueError) as error:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink()
        return (
            destination.name,
            str(destination.relative_to(WEEK2_DIR)),
            "",
            "",
            f"FAILED:{timestamp}:{error}",
        )


def main() -> int:
    rows = []
    failures = 0

    for relative_path, url in DOWNLOADS:
        try:
            row = download_one(relative_path, url)
        except ValueError as error:
            print(f"SKIP {relative_path}: {error}", file=sys.stderr)
            failures += 1
            continue

        rows.append(row)
        if row[2]:
            print(f"OK   {row[1]} ({row[3]} bytes)")
        else:
            failures += 1
            print(f"FAIL {row[1]}: {row[4]}", file=sys.stderr)

    with MANIFEST.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "filename", "relative_path", "sha256",
            "file_size_bytes", "downloaded_at",
        ])
        writer.writerows(rows)

    print(f"Wrote manifest: {MANIFEST}")
    print(f"Successful downloads: {len(rows) - failures}; failures: {failures}")
    print("An empty manifest is expected while DOWNLOADS has no approved entries.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
