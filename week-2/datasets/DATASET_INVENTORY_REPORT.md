# Week 2 Dataset Inventory Report

**Status:** Partial. Four dataset folders are listed, but their actual local image counts, class distributions, duplicates, and full licence evidence have not yet been verified.

| Dataset | Folder | Current note |
|---|---|---|
| DS-001 | Cotton Leaf Disease Dataset with Severity Levels | Confirm extracted folder/ZIP are not double-counted; verify source and licence |
| DS-002 | long-diseases | Crop and classes need inspection |
| DS-003 | rice ninja | Inspect local metadata and licence file |
| DS-004 | rice_leaf_diseases | Confirm source/licence and whether "Leaf smut" maps to an official class |

Run the read-only inspection utility locally:

```powershell
python week-2/datasets/inspect_datasets.py "E:\Interships\ITSamplera solutions\Datasets"
```

The utility should write a separate measured report. Review its output before updating the inventory. Do not move, rename, delete, overwrite, or modify the original dataset files. Image classification is conditional future work and should not begin until licensing, labels, data quality, and class counts are validated.
