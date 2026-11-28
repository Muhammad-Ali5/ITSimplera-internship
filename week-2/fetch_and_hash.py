#!/usr/bin/env python3
"""
fetch_and_hash.py  —  Week 2 reproducible source downloader + hasher.

WHY THIS EXISTS
---------------
The Week 2 source metadata was collected in a sandbox whose network could not
reach institutional sites (IRRI, FAO, CCRI, DPP ...), so NO source documents
were downloaded there and SHA256SUMS.csv was left empty of document rows.
Run THIS script on your own machine (where the network is open) to:
  1. download the documents that are legally downloadable,
  2. compute their SHA-256 hashes and sizes,
  3. write/append rows to week-2/SHA256SUMS.csv.

RULES BUILT IN
--------------
* It only downloads the URLs YOU list in DOWNLOADS below. Review each one and
  confirm it is legally downloadable before adding it. Do NOT add paywalled /
  copyrighted full texts you are not licensed to download.
* It never invents a hash: if a download fails, it records status=FAILED with
  no hash, so the evidence stays honest.
* Re-running is safe: it rewrites SHA256SUMS.csv from scratch each run.

USAGE
-----
    python scripts/fetch_and_hash.py
(from the repo root, or adjust REPO_ROOT below.)
"""
from __future__ import annotations

import csv
import datetime
import hashlib
import os
import sys
import urllib.error
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # week-2/
SUMS = os.path.join(REPO_ROOT, "SHA256SUMS.csv")

# (relative_path_to_save, url) — EDIT THIS LIST. Confirm each is legal to download.
# Relative paths follow the week-2/sources/ layout required by the brief.
DOWNLOADS = [
    # --- rice (T1) ---
    ("sources/rice/pdfs/IRRI_Diagnosis_of_Common_Diseases_of_Rice.pdf",
     "https://www.knowledgebank.irri.org/images/docs/diagnostic-of-common-diseases-of-rice.pdf"),
    # --- cotton (T1) ---
    ("sources/cotton/pdfs/CCRI_Annual_Progress_Report_2023-2024.pdf",
     "https://ccri.gov.pk/Annual Report 2023-2024.pdf"),
    # --- pesticides / DPP & legal (T1) ---
    ("sources/dpp/pdfs/FAOLEX_Agricultural_Pesticides_Rules_Pakistan_pak4115.pdf",
     "https://faolex.fao.org/docs/pdf/pak4115.pdf"),
    # Add more AFTER confirming they are legally downloadable, e.g. the DPP
    # registered / banned pesticide list once you locate its exact URL on
    # https://plantprotection.gov.pk/ .
]

def sha256_of(path: str) -> tuple[str, int]:
    h = hashlib.sha256(); size = 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk); size += len(chunk)
    return h.hexdigest(), size

def main() -> int:
    rows = []
    for rel, url in DOWNLOADS:
        dest = os.path.join(REPO_ROOT, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ITSimplera-week2/1.0"})
            with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as out:
                out.write(resp.read())
            digest, size = sha256_of(dest)
            rows.append([os.path.basename(rel), rel, digest, size, now])
            print(f"OK    {rel}  ({size} bytes)")
        except (urllib.error.URLError, OSError) as e:
            rows.append([os.path.basename(rel), rel, "", "", f"FAILED:{now}:{e}"])
            print(f"FAIL  {rel}  -> {e}", file=sys.stderr)

    with open(SUMS, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["filename", "relative_path", "sha256", "file_size_bytes", "downloaded_at"])
        w.writerows(rows)
    print(f"\nWrote {SUMS} ({len(rows)} rows). Review FAILED rows and licence terms before use.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
