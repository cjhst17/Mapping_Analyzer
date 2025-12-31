# Mapping Analyzer

Automated X12 EDI mapping analysis tool. Upload X12 files and the pipeline runs analysis, validation, and generates code for map updates.

## How It Works

1. **Upload Files** → Push X12 files, maps, and schemas to the `uploads/` folder
2. **Pipeline Triggers** → Azure DevOps pipeline automatically detects changes
3. **Analysis Runs** → Tool analyzes uploaded files
4. **Results Generated** → Analysis results saved to `results/` folder
5. **Access Results** → Download analysis JSON, generated code, and reports

## Quick Start

```bash
# 1. Create environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Test locally
python src/analyze.py --input-dir uploads/ --output-dir results/
```

## File Structure

```
uploads/                    ← Upload X12 files here
  ├── *.edi               - X12 EDI documents (850, 810, 270, 834)
  ├── *.map               - Seeburger map files
  ├── *.xml               - XML map exports
  └── *.json              - JSON schemas

results/                    ← Analysis results (auto-generated)
  └── analysis_results.json

src/
  ├── analyze.py          - Main analysis script
  ├── analyzers/          - X12 analysis modules
  ├── validators/         - X12 compliance modules
  ├── generators/         - Code generation modules
  └── utils/              - Utilities

tests/
  ├── unit/               - Unit tests
  └── integration/        - Integration tests
```

## Pipeline Workflow

When you commit files to `uploads/`:

```
1. Upload X12 files to uploads/
2. git add uploads/
3. git commit -m "Add files for analysis"
4. git push origin main
   ↓
5. Pipeline triggers automatically
6. Python runs analysis
7. Results saved to results/
8. Artifacts published
```

## Usage

### Upload Files to Repository

```bash
# Copy your files
cp my_map.xml uploads/
cp sample_850.edi uploads/
cp schema.json uploads/

# Commit and push
git add uploads/
git commit -m "Add files for analysis"
git push origin main
```

### Run Analysis Locally

```bash
python src/analyze.py --input-dir uploads/ --output-dir results/
```

### View Results

```bash
cat results/analysis_results.json
```

## Pipeline Configuration

- **Trigger**: Any commit to `uploads/` or `src/` folders
- **Automatic**: No manual trigger needed
- **Output**: JSON results published as artifacts
