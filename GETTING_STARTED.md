# Getting Started

## Step 1: Setup Local Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Add Your Files

Place files in the `uploads/` folder:

```
uploads/
├── my_map.xml              # Seeburger map file
├── sample_850.edi          # X12 850 document
└── input_schema.json       # Input schema
```

## Step 3: Test Locally

```powershell
python src/analyze.py --input-dir uploads/ --output-dir results/
```

Check `results/analysis_results.json` for output.

## Step 4: Push to Azure DevOps

```bash
git add uploads/
git commit -m "Add files for analysis"
git push origin main
```

The pipeline will automatically:
- Run the analysis
- Generate results
- Publish artifacts

## What Gets Analyzed

The tool processes:
- **EDI files** (`.edi`) - X12 documents (850, 810, 270, 834)
- **Map files** (`.map`) - Seeburger binary maps
- **XML maps** (`.xml`) - Seeburger XML exports
- **Schemas** (`.json`) - Input/output validation schemas

## Output

Results are saved to `results/analysis_results.json`:

```json
{
  "timestamp": "2025-12-30T10:00:00",
  "files_processed": 3,
  "analysis_results": [
    {
      "file": "sample_850.edi",
      "type": "EDI",
      "standard": "X12-850",
      "segment_count": 12,
      "status": "analyzed"
    }
  ]
}
```

## Next Steps

1. Add your X12 files to `uploads/`
2. Push to repository
3. Pipeline runs automatically
4. Download results from Azure DevOps artifacts
5. Expand `src/` modules for custom analysis
