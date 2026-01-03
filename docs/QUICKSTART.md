# Quickstart Guide

Get started with DSAT Difficulty Classification in 3 steps.

## 1. Clone & Install

```bash
git clone https://github.com/aekamban/dsat-difficulty-classifier.git
cd dsat-difficulty-classifier
pip install -r requirements.txt
```

## 2. Run the Notebook

```bash
jupyter notebook notebooks/dsat_difficulty_pipeline.ipynb
```

The notebook runs immediately using cached features—no PDFs needed!

## 3. Explore Results

The notebook will:
- Load pre-extracted difficulty labels from 6 DSAT practice tests
- Display distribution statistics (Easy/Medium/Hard breakdown)
- Generate visualizations showing difficulty patterns across tests
- Complete in <1 minute

## What You'll See

**Input → Output Flow:**

| Input | Processing | Output |
|-------|-----------|--------|
| Official DSAT practice tests (6 tests) | Computer vision detection of difficulty markers | 90 pages labeled by difficulty |
| Answer key PDFs | Binary thresholding + contour detection | Easy: 24, Medium: 47, Hard: 19 |
| Visual markers (filled circles) | Rule-based classification | 98% detection quality |

## Next Steps

- **View the pipeline diagram**: Check `images/pipeline_overview.png`
- **Read the model card**: See `docs/model_card.md` for methodology details
- **Run full OCR**: Follow `data/README.md` to process your own PDFs

## Troubleshooting

**Issue**: "No such file or directory: data/derived/difficulty_labels.csv"  
**Solution**: Make sure you're in the repository root directory

**Issue**: Missing visualization  
**Solution**: Run all cells in the notebook to generate plots

**Issue**: Want to run OCR on new PDFs  
**Solution**: 
1. Place PDFs in `data/raw/`
2. Set `RUN_OCR=True` in notebook
3. Install OCR dependencies (uncomment lines in requirements.txt)

## Support

For questions or issues, please open a GitHub issue or contact the author.
