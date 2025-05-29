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
