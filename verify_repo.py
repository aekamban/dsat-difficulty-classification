#!/usr/bin/env python3
"""
Verification script to ensure repository is ready for GitHub.
"""

from pathlib import Path
import sys

def check_file_exists(filepath, description):
    """Check if a file exists and report status."""
    if Path(filepath).exists():
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ MISSING {description}: {filepath}")
        return False

def verify_repository():
    """Verify all required files are present."""
    print("=" * 60)
    print("DSAT DIFFICULTY CLASSIFIER - REPOSITORY VERIFICATION")
    print("=" * 60)
    
    all_good = True
    
    # Core files
    print("\n📁 Core Files:")
    all_good &= check_file_exists("README.md", "Main README")
    all_good &= check_file_exists("requirements.txt", "Dependencies")
    all_good &= check_file_exists(".gitignore", "Git ignore rules")
    
    # Notebook
    print("\n📓 Notebook:")
    all_good &= check_file_exists("notebooks/dsat_difficulty_pipeline.ipynb", "Main pipeline notebook")
    
    # Data
    print("\n📊 Data:")
    all_good &= check_file_exists("data/README.md", "Data documentation")
    all_good &= check_file_exists("data/derived/difficulty_labels.csv", "Cached features")
    
    # Documentation
    print("\n📄 Documentation:")
    all_good &= check_file_exists("docs/model_card.md", "Model card")
    all_good &= check_file_exists("docs/QUICKSTART.md", "Quickstart guide")
    
    # Images
    print("\n🖼️  Images:")
    all_good &= check_file_exists("images/pipeline_overview.png", "Pipeline diagram")
    all_good &= check_file_exists("images/difficulty_distribution.png", "Distribution plot")
    
    # Summary
    print("\n" + "=" * 60)
    if all_good:
        print("✅ ALL CHECKS PASSED - Repository is ready!")
        print("\nNext steps:")
        print("  1. Review README.md for accuracy")
        print("  2. Test notebook execution")
        print("  3. Initialize git: git init")
        print("  4. Add files: git add .")
        print("  5. Commit: git commit -m 'Initial commit: DSAT difficulty classifier'")
        print("  6. Push to GitHub")
    else:
        print("❌ SOME CHECKS FAILED - Please review missing files above")
        sys.exit(1)
    print("=" * 60)

if __name__ == "__main__":
    verify_repository()
