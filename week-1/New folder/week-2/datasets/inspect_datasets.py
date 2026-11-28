"""
inspect_datasets.py — Day 9 dataset inventory (RUN LOCALLY on your machine).

WHY LOCAL: the image datasets live under /Datasets/ which is gitignored and is
NOT in the GitHub repo, and the desktop bridge to E:\\ was offline when the
Week-2 files were prepared. So the real image counts, per-class counts, corrupt
files and duplicates could NOT be computed remotely. This script computes them
on your machine and fills dataset_inventory.csv with REAL numbers.

It never invents numbers: it only reports what it actually finds on disk.

USAGE (from the project root, with the datasets present):
    python week-2/datasets/inspect_datasets.py "E:\\Interships\\ITSamplera solutions\\Datasets"

It writes/overwrites: week-2/datasets/dataset_inventory_measured.csv
Review it, then copy the real values into dataset_inventory.csv.
"""
from __future__ import annotations

import csv
import hashlib
import os
import sys
from collections import defaultdict

IMG_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tif", ".tiff"}

def is_img(name: str) -> bool:
    return os.path.splitext(name)[1].lower() in IMG_EXT

def sha1_head(path: str, nbytes: int = 1 << 16) -> str:
    """Cheap duplicate key: sha1 of the first 64 KiB + file size."""
    try:
        with open(path, "rb") as f:
            data = f.read(nbytes)
        return hashlib.sha1(data).hexdigest() + f"-{os.path.getsize(path)}"
    except OSError:
        return ""

def inspect(root: str) -> list[dict]:
    out = []
    for entry in sorted(os.listdir(root)):
        folder = os.path.join(root, entry)
        if not os.path.isdir(folder):
            continue
        total = 0
        corrupt = 0
        per_class: dict[str, int] = defaultdict(int)
        fmts: dict[str, int] = defaultdict(int)
        hashes: dict[str, int] = defaultdict(int)
        splits = {"train": 0, "val": 0, "valid": 0, "test": 0}
        for dirpath, _dirs, files in os.walk(folder):
            rel = os.path.relpath(dirpath, folder).lower()
            split_hit = next((s for s in splits if s in rel.split(os.sep)), None)
            cls = os.path.basename(dirpath)
            for fn in files:
                if not is_img(fn):
                    continue
                total += 1
                fmts[os.path.splitext(fn)[1].lower()] += 1
                per_class[cls] += 1
                if split_hit:
                    splits[split_hit] += 1
                p = os.path.join(dirpath, fn)
                h = sha1_head(p)
                if not h:
                    corrupt += 1
                else:
                    hashes[h] += 1
        dup = sum(c - 1 for c in hashes.values() if c > 1)
        out.append({
            "folder": entry,
            "total_images": total,
            "classes": len([c for c in per_class if per_class[c] > 0]),
            "per_class": "; ".join(f"{k}:{v}" for k, v in sorted(per_class.items())),
            "train": splits["train"], "valid": splits["val"] + splits["valid"], "test": splits["test"],
            "formats": "; ".join(f"{k}:{v}" for k, v in sorted(fmts.items())),
            "likely_duplicates": dup,
            "unreadable_images": corrupt,
        })
    return out

def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    root = argv[1]
    if not os.path.isdir(root):
        print(f"Not a directory: {root}", file=sys.stderr)
        return 1
    rows = inspect(root)
    out_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_inventory_measured.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else
                           ["folder", "total_images", "classes", "per_class", "train",
                            "valid", "test", "formats", "likely_duplicates", "unreadable_images"])
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r['folder']}: {r['total_images']} images, {r['classes']} classes, "
              f"dups~{r['likely_duplicates']}, unreadable={r['unreadable_images']}")
    print(f"\nWrote {out_csv}. Copy the real numbers into dataset_inventory.csv.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
