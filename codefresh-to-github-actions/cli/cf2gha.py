import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

INPUT_DIR = "codefresh-pipelines"
OUTPUT_DIR = ".github/workflows"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_pipeline(cf_yaml):
    prompt = f"""
Convert the following Codefresh pipeline to an advanced GitHub Actions workflow. Include:
- Separate jobs for clone, build, test, and deploy
- Environment variables and secrets
- Matrix test strategy
- Docker build and reuse

```yaml
{cf_yaml}
```

GitHub Actions Workflow:
"""
    res = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return res.choices[0].message['content']

def main():
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".yml") or file.endswith(".yaml"):
            with open(os.path.join(INPUT_DIR, file), "r") as f:
                cf_yaml = f.read()

            gha_yaml = convert_pipeline(cf_yaml)
            output_path = os.path.join(OUTPUT_DIR, file.replace("pipeline", "workflow"))

            with open(output_path, "w") as out:
                out.write(gha_yaml)
                print(f"✅ Converted {file} → {output_path}")

if __name__ == "__main__":
    main()
