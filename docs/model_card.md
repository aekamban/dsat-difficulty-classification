# Model Card: DSAT Difficulty Classifier

## Model Overview

**Task**: Multi-class classification of Digital SAT (DSAT) test questions by difficulty level

**Labels**: Easy, Medium, Hard, Unknown

**Approach**: Computer vision-based pattern detection from answer key PDFs

## Intended Use

### Primary Use Cases
- Automated organization of DSAT practice questions by difficulty
- Curriculum planning and differentiated instruction support
- Streamlining test prep material development

### Out of Scope
- Predicting difficulty of questions not from official DSAT practice tests
- Real-time classification during test administration
- Content generation or question creation

## Data

**Source**: Official College Board DSAT practice test answer keys (6 tests)

**Inputs**: PDF pages from answer key documents

**Features**: 
- Visual markers (filled circles/boxes indicating difficulty)
- Spatial layout patterns
- Box count and size heuristics

**Size**: ~90 pages per test × 6 tests = ~540 labeled pages

## Methodology

### Detection Algorithm
1. Convert PDF pages to grayscale images (200 DPI)
2. Extract region of interest (difficulty marker area) using fixed crop coordinates
3. Apply binary thresholding
4. Detect contours and filter by size/aspect ratio
5. Classify difficulty based on number of valid markers:
   - 3+ boxes → Hard
   - 2 boxes → Medium
   - 1 box → Easy (with size validation)
   - 0 boxes → Unknown

### Confidence Estimation
- Hard: 0.85-0.99 (scales with box count)
- Medium: 0.90
- Easy: 0.75
- Unknown: 0.0

## Performance

**Detection Quality**: ~98-99% (percentage of non-Unknown classifications)

**Error Cases**:
- Pages with inconsistent formatting
- Low-quality scans affecting contour detection
- Marker positions outside expected crop region

## Limitations

### Technical Limitations
- Relies on consistent PDF formatting across tests
- Fixed crop coordinates may not generalize to different test formats
- OCR quality can vary with scan resolution and image preprocessing

### Ethical Considerations
- Not validated on unofficial or third-party test materials
- May not reflect actual student performance or question difficulty
- Could perpetuate existing biases in how questions are labeled by test creators

### Known Biases
- Answer key labeling reflects College Board's difficulty assessment, which may not align with all student populations
- Visual detection assumes consistent formatting (may fail on reformatted or digitally altered documents)

## Recommendations

### Best Practices
- Use cached features for reproducibility
- Validate detection results on sample pages before batch processing
- Combine with manual review for high-stakes applications

### Monitoring
- Track Unknown classification rate as quality metric
- Periodically audit sample predictions against ground truth
- Monitor for format changes in new practice test releases

## Version & Updates

**Current Version**: 1.0 (January 2025)

**Maintenance**: This is a demonstration project for portfolio purposes. For production use, consider:
- Validation on additional test versions
- Adaptive crop detection instead of fixed coordinates
- Integration with text-based features for enhanced accuracy

## Contact & Feedback

For questions or to report issues with this implementation, please open an issue in the GitHub repository.

---

*This model card follows guidelines from [Mitchell et al. 2019](https://arxiv.org/abs/1810.03993) and is intended for transparency and responsible AI documentation.*
