# Setting Up Azure Pipelines with GitHub

## Step 1: Connect GitHub to Azure DevOps

1. Go to your **Azure DevOps Project**
2. Go to **Project Settings** → **Service connections**
3. Click **New service connection** → **GitHub**
4. Choose **GitHub** (not GitHub Enterprise)
5. Click **Authorize** and sign in with your GitHub account
6. Name it `GitHub` and save

## Step 2: Create the Pipeline

1. In Azure DevOps, go to **Pipelines** → **Create Pipeline**
2. Select **GitHub** as your code repository
3. Select **cjhst17/Mapping_Analyzer** repository
4. Choose **Existing Azure Pipelines YAML file**
5. Branch: `main`
6. Path: `.ado/pipelines/ci.yml`
7. Click **Continue** and **Save**

## Step 3: Trigger the Pipeline

The pipeline will trigger automatically when you:
- Push to `main` branch
- Modify files in `uploads/`, `src/`, or `tests/`
- Create a pull request

## Step 4: View Results

1. Go to **Pipelines** in Azure DevOps
2. Click your pipeline run
3. View logs and artifacts
4. Download analysis results from **Published artifacts**

## Alternative: Use GitHub Actions Instead

If you prefer GitHub's native CI/CD:

1. Push code to GitHub
2. Go to your repo → **Actions**
3. GitHub automatically detects `.github/workflows/ci.yml`
4. Workflow runs automatically on push
5. View results in **Actions** tab

## Troubleshooting

### Pipeline not triggering?
- Check **Service connection** is configured
- Make sure you're pushing to `main` branch
- Verify files are in `uploads/`, `src/`, or `tests/`

### Need to re-authorize?
- Go to **Project Settings** → **Service connections**
- Find GitHub connection
- Click **Edit** → **Re-authorize**

## Repository Configuration

Your setup:
- **Repository**: https://github.com/cjhst17/Mapping_Analyzer
- **Branch**: main
- **Pipeline Type**: Azure Pipelines
- **Triggers**: uploads/*, src/*, tests/*
