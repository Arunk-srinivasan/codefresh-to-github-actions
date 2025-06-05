# 🚀 Codefresh to GitHub Actions Pipeline Converter

## 📘 Overview

This project automates the migration of CI/CD pipelines from **Codefresh** to **GitHub Actions**, leveraging the power of **OpenAI's GPT-4o model**.

It includes:

* ✅ A **CLI tool** to batch-convert Codefresh pipelines
* ✅ A **Streamlit web app** for manual, on-demand conversion
* ✅ Integration with OpenAI's LLM to intelligently generate GitHub Actions workflows from Codefresh YAML

The goal is to streamline pipeline migrations, reduce manual effort, and provide a developer-friendly interface to transition CI/CD from Codefresh to GitHub-native tooling.

---

## 🧩 Components

### 1. `cf2gha.py` (CLI Script)

* Reads Codefresh pipeline YAML files
* Uses a prompt template to instruct GPT on how to convert it
* Calls OpenAI API
* Extracts valid YAML from the response
* Writes the result to `.github/workflows/`
* Validates YAML correctness before saving

### 2. `app.py` (Streamlit Web App)

* Upload a Codefresh YAML file
* Enter OpenAI API Key
* Click to convert and download the GitHub Actions workflow

### 3. `prompt.txt`

* Prompt template that guides the LLM in how to structure GitHub Actions workflows
* Can be customized to change deployment strategies, add security scans, Slack notifications, etc.

---

## ✅ What This Can Do

| Capability                               | Supported            |
| ---------------------------------------- | -------------------- |
| Convert Codefresh YAML to GitHub Actions | ✅                    |
| Matrix builds (e.g., Python 3.8/3.11)    | ✅                    |
| Docker build/reuse strategy              | ✅                    |
| Use GitHub Environments                  | ✅                    |
| Manual approvals via `production` env    | ✅ (UI only)          |
| Per-env secrets (`staging`, `prod`)      | ✅                    |
| Add Slack notifications                  | ✅ (via prompt tweak) |
| Security scan jobs (Trivy, OWASP)        | ✅                    |

---

## ❌ What It Cannot Do (yet)

| Limitation                               | Explanation                                      |
| ---------------------------------------- | ------------------------------------------------ |
| Migrate secrets automatically            | GitHub secrets must be added manually            |
| Set environment protection rules in YAML | Must be configured in GitHub UI                  |
| Translate custom Codefresh plugins 1:1   | May need prompt tweaking or manual edits         |
| Validate entire GitHub workflow context  | Only checks YAML structure, not runtime behavior |
| Push changes to GitHub automatically     | Git must be used separately                      |

---

## 👷 Manual Steps After Conversion

1. **Review Workflow Logic**

   * Check if the conversion aligns with your deployment process.

2. **Add GitHub Secrets**

   * Go to `Settings → Secrets and variables → Actions`
   * Add all required environment variables/secrets manually

3. **Configure Environments in GitHub**

   * Go to `Settings → Environments`
   * Create `staging`, `production`, etc.
   * Add required reviewers, rules, and secrets

4. **Test the Workflow**

   * Use `act` locally or push to a test branch in GitHub

5. **Push Converted Workflows**

   ```bash
   git add .github/workflows/
   git commit -m "Add GitHub Actions workflow converted from Codefresh"
   git push
   ```

---

## 💡 Suggested Improvements

* Add support for reusable GitHub workflows
* Auto-map common Codefresh steps/plugins to GitHub Actions equivalents
* Provide UI toggle for different conversion styles (e.g., basic vs secure)
* Enable GitHub push directly from web app (with PAT)

---

## 📂 Folder Structure

```
codefresh-to-github-actions/
├── cli/
│   └── cf2gha.py               # CLI script
├── web/
│   └── app.py                  # Streamlit UI
├── .github/workflows/          # Output GitHub Actions workflows
├── codefresh-pipelines/        # Input folder for Codefresh YAMLs
├── prompt.txt                  # Customizable prompt
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

---

## 🏁 Final Words

This tool is built for DevOps teams and developers looking to accelerate migration away from Codefresh. It provides an AI-powered bridge to GitHub-native CI/CD pipelines and offers both flexibility and control.

While it greatly reduces manual effort, **final validation, secrets configuration, and environment setup must still be done in GitHub**.

For large-scale or enterprise-wide migrations, this tool can be integrated into internal tooling or CI pipelines as a helper service.

> Built with ❤️ using GPT-4o + GitHub + Python


# Codefresh → GitHub Actions Converter

A tool powered by OpenAI GPT-4o to convert Codefresh pipelines to GitHub Actions workflows using either a CLI or a Web UI.

## 🔧 CLI Usage

```bash
export OPENAI_API_KEY=your_key
python cli/cf2gha.py
```

## 🌐 Web UI

```bash
streamlit run web/app.py
```

Upload `.yml` → Get `.github/workflows/your-pipeline.yml`

---

Powered by [OpenAI](https://platform.openai.com/) 💡
