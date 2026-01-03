# Data Directory

## Overview

This directory contains derived features for the DSAT difficulty classification pipeline. **Raw test images and PDFs are not distributed** in this repository due to copyright restrictions.

## Structure

```
data/
├── raw/          # NOT included - place your DSAT PDFs here
├── derived/      # Cached features (included for reproducibility)
└── README.md     # This file
```

## Obtaining Source Data

To run the full pipeline with OCR enabled:

1. **Obtain official DSAT practice tests** from College Board's official resources
2. Place PDF files in `data/raw/` with the naming pattern: `SAT{N}.pdf` and `SAT{N}_Key.pdf`
3. Expected files:
   - Test PDFs: `SAT1.pdf`, `SAT2.pdf`, etc.
   - Answer key PDFs: `SAT1_Key.pdf`, `SAT2_Key.pdf`, etc.

## Using Cached Features

By default, the notebook uses pre-extracted features from `data/derived/` so you can run the pipeline without the original PDFs. This allows:
- Reproducible model training
- Faster iteration
- IP-compliant sharing

## Full OCR Pipeline

To run OCR feature extraction from scratch:
1. Place PDFs in `data/raw/` as described above
2. Install OCR dependencies: `pip install pdf2image pytesseract poppler-utils`
3. In the notebook, set `RUN_OCR = True`
4. Run all cells

## License Note

Official DSAT practice materials are copyrighted by College Board. This repository contains only code and derived features, not the original test content.
