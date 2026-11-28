# Week 2 Dataset Inventory Report

**Status:** Inventory structure prepared; local measurements and licence checks remain pending.

Four local dataset folders have been identified:

| Dataset ID | Folder | Current note |
|---|---|---|
| DS-001 | Cotton Leaf Disease Dataset with Severity Levels | Check whether folder and ZIP are two copies of the same dataset before counting |
| DS-002 | long-diseases | Inspect contents and metadata to identify crop and classes |
| DS-003 | rice ninja | Read the local `LICENSE.md`, README and metadata; confirm original creator and source |
| DS-004 | rice_leaf_diseases | Review class folders; "Leaf smut" must not automatically be treated as official Rice False Smut |

## Measure local files

Run this from the repository root:

```powershell
python week-2/datasets/inspect_datasets.py "E:\\Interships\\ITSamplera solutions\\Datasets"
```

The script writes `dataset_inventory_measured.csv` beside itself. It reports file counts, folder-based class counts, common split folders, image extensions, exact duplicate files (full-file SHA-256), and files that could not be read.

The utility does not decode images to prove that they are valid images. Its class and split counts are folder-name based and must be reviewed against each dataset's README and metadata.

## Dataset protection and licence

- The utility reads files and writes a separate report. It does not modify original images.
- Do not move, rename, delete, or overwrite the original dataset folders.
- Record the original dataset page, publisher/creator, exact licence and any attribution requirements.
- A public download link does not automatically grant permission to redistribute or train on the images.
- Do not combine extracted and archived copies in totals without checking for duplication.

No image totals, class counts, or licence approvals are claimed until the local inspection and human review are complete.
