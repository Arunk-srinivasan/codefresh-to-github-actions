import streamlit as st
import openai

# Get API key from user
st.title("🚀 Codefresh to GitHub Actions Converter")
api_key = st.text_input("Enter your OpenAI API Key", type="password")

uploaded_file = st.file_uploader("Upload a Codefresh YAML file", type=["yml", "yaml"])

# Use OpenAI v1-style client if key is provided
if uploaded_file and api_key:
    client = openai.OpenAI(api_key=api_key)
    codefresh_yaml = uploaded_file.read().decode("utf-8")

    with st.spinner("Converting with GPT..."):
        prompt = f"""
Convert this Codefresh pipeline to a GitHub Actions workflow with:
- Separate jobs for clone, build, test, and deploy
- Environment-specific secrets and manual approval for production
- Matrix test strategy
- Docker image caching and reuse

Codefresh YAML:
{codefresh_yaml}

GitHub Actions Workflow:
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        output = response.choices[0].message.content

        # Optional: Clean markdown wrappers like ```yaml
        output = output.replace("```yaml", "").replace("```", "").strip()

        st.code(output, language="yaml")
        st.download_button("Download Workflow", output, file_name="github-actions.yml")
