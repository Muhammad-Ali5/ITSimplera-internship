"""Read-only inventory of image files in local Week 2 dataset folders.

Run from the repository root:
    python week-2/datasets/inspect_datasets.py "E:\\Interships\\ITSamplera solutions\\Datasets"

The script writes a separate measured CSV beside this file. It does not edit
or move the original dataset files. Duplicate detection uses full-file SHA-256.
The unreadable count means files that could not be read, not validated corrupt
image files (image decoding is intentionally outside this lightweight utility).
"""
from __future__ import annotations

import csv
import hashlib
import os
import sys
from collections import defaultdict
from pathlib import Path

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tif", ".tiff",
}
OUTPUT = Path(__file__).resolve().with_name("dataset_inventory_measured.csv")
FIELDNAMES = [
    "folder", "total_images", "classes", "per_class", "train", "valid",
    "test", "formats", "exact_duplicates", "unreadable_files",
]


def is_image(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS


def file_sha256(path: Path) -> str | None:
    """Return a full-file digest, or None when the file cannot be read."""
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError:
        return None
    return digest.hexdigest()


def inspect_dataset(folder: Path) -> dict[str, object]:
    per_class: dict[str, int] = defaultdict(int)
    formats: dict[str, int] = defaultdict(int)
    hashes: dict[str, int] = defaultdict(int)
    splits = {"train": 0, "val": 0, "valid": 0, "test": 0}
    total = 0
    unreadable = 0

    for path in folder.rglob("*"):
        if not path.is_file() or not is_image(path):
            continue

        total += 1
        formats[path.suffix.lower()] += 1
        relative_parts = path.relative_to(folder).parts
        parent_parts = relative_parts[:-1]

        split = next(
            (part.lower() for part in parent_parts
             if part.lower() in splits),
            None,
        )
        if split:
            splits[split] += 1

        if split:
            split_index = next(
                index for index, part in enumerate(parent_parts)
                if part.lower() == split
            )
            class_name = (
                parent_parts[split_index + 1]
                if split_index + 1 < len(parent_parts)
                else "(no class folder)"
            )
        else:
            class_name = parent_parts[-1] if parent_parts else "(root)"
        per_class[class_name] += 1

        digest = file_sha256(path)
        if digest is None:
            unreadable += 1
        else:
            hashes[digest] += 1

    duplicates = sum(count - 1 for count in hashes.values() if count > 1)
    class_rows = "; ".join(
        f"{name}:{count}" for name, count in sorted(per_class.items())
    )
    format_rows = "; ".join(
        f"{extension}:{count}" for extension, count in sorted(formats.items())
    )

    return {
        "folder": folder.name,
        "total_images": total,
        "classes": len(per_class),
        "per_class": class_rows,
        "train": splits["train"],
        "valid": splits["val"] + splits["valid"],
        "test": splits["test"],
        "formats": format_rows,
        "exact_duplicates": duplicates,
        "unreadable_files": unreadable,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2

    root = Path(argv[1]).expanduser()
    if not root.is_dir():
        print(f"Dataset directory not found: {root}", file=sys.stderr)
        return 1

    rows = [
        inspect_dataset(folder)
        for folder in sorted(root.iterdir())
        if folder.is_dir()
    ]

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(
            f"{row['folder']}: {row['total_images']} images, "
            f"{row['classes']} classes, "
            f"exact duplicates={row['exact_duplicates']}, "
            f"unreadable files={row['unreadable_files']}"
        )

    print(f"Measured inventory written to: {OUTPUT}")
    print("Review class names and splits manually before updating the master CSV.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
