import os
import argparse
import openai
import yaml

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def convert_pipeline(cf_yaml, prompt_path):
    with open(prompt_path, "r") as f:
        base_prompt = f.read()

    prompt = base_prompt.format(cf_yaml=cf_yaml)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content

def validate_yaml(yaml_str):
    try:
        yaml.safe_load(yaml_str)
        return True
    except yaml.YAMLError as e:
        print(" YAML validation failed:", e)
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert Codefresh pipelines to GitHub Actions using OpenAI GPT")
    parser.add_argument("--input", default="../codefresh-pipelines", help="Directory containing Codefresh YAML files")
    parser.add_argument("--output", default="../.github/workflows", help="Directory to save GitHub Actions workflows")
    parser.add_argument("--prompt", default="../prompt.txt", help="Path to the prompt template")
    parser.add_argument("--log", default="../conversion.log", help="Log file for conversions")

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    with open(args.log, "w") as log:
        for file in os.listdir(args.input):
            if file.endswith(".yml") or file.endswith(".yaml"):
                input_path = os.path.join(args.input, file)
                with open(input_path, "r") as f:
                    cf_yaml = f.read()

                print(f" Converting {file}...")

                gha_yaml = convert_pipeline(cf_yaml, args.prompt)

                if not validate_yaml(gha_yaml):
                    log.write(f" {file}: YAML validation failed.\n")
                    continue

                output_filename = file.replace("pipeline", "workflow")
                output_path = os.path.join(args.output, output_filename)

                with open(output_path, "w") as out:
                    out.write(gha_yaml)
                    print(f" Saved to {output_path}")
                    log.write(f" {file} -> {output_path}\n")

if __name__ == "__main__":
    main()
