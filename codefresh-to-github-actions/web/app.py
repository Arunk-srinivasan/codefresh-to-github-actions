import streamlit as st
import openai

st.title("🚀 Codefresh to GitHub Actions Converter")
openai.api_key = st.text_input("Enter your OpenAI API Key", type="password")

uploaded_file = st.file_uploader("Upload a Codefresh YAML file", type=["yml", "yaml"])

if uploaded_file and openai.api_key:
    codefresh_yaml = uploaded_file.read().decode("utf-8")

    with st.spinner("Converting..."):
        prompt = f"""
Convert this Codefresh pipeline into GitHub Actions format with multiple jobs, matrix strategy, docker image caching, secrets, and environment variables:

```yaml
{codefresh_yaml}
```

GitHub Actions Workflow:
"""
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        converted = response.choices[0].message['content']
        st.code(converted, language="yaml")
        st.download_button("Download Workflow", converted, file_name="github-actions.yml")
