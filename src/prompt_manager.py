
import re
from pathlib import Path


# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BASE_DIR / "prompts"


PROMPT_FILES = {
    "data_analysis": "data_analysis.txt",
    "summarization": "summarization.txt",
    "classification": "classification.txt",
    "content_generation": "content_generation.txt"
}


def load_prompt(task_name, version, replacements=None):

    if task_name not in PROMPT_FILES:
        raise ValueError(f"Unknown prompt task: {task_name}")

    if version not in [1, 2]:
        raise ValueError("Version must be 1 or 2")

    file_path = PROMPTS_DIR / PROMPT_FILES[task_name]

    if not file_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {file_path}")

    content = file_path.read_text(encoding="utf-8-sig")

    # Normalize different dash characters
    content = content.replace("–", "-").replace("—", "-")

    # Find version headings
    v1_heading = re.search(
        r"VERSION\s*1\b[^\r\n]*INITIAL\s+PROMPT[^\r\n]*",
        content,
        re.IGNORECASE
    )

    v2_heading = re.search(
        r"VERSION\s*2\b[^\r\n]*IMPROVED\s+PROMPT[^\r\n]*",
        content,
        re.IGNORECASE
    )

    if not v1_heading or not v2_heading:
        raise ValueError(
            f"Prompt headings not found in {PROMPT_FILES[task_name]}. "
            "Check VERSION 1 - INITIAL PROMPT and "
            "VERSION 2 - IMPROVED PROMPT."
        )

    if version == 1:

        if v1_heading.end() > v2_heading.start():
            raise ValueError("Invalid prompt version order.")

        prompt = content[v1_heading.end():v2_heading.start()]

    else:

        prompt = content[v2_heading.end():]

    # Remove separator lines
    prompt = re.sub(r"(?m)^\s*=+\s*$", "", prompt).strip()

    # Replace placeholders
    if replacements:

        for key, value in replacements.items():

            placeholder = "{" + key + "}"

            prompt = prompt.replace(placeholder, str(value))

    # Detect missing placeholders
    remaining = re.findall(r"\{(\w+)\}", prompt)

    if remaining:
        raise ValueError(
            f"Missing prompt data for: {remaining}"
        )

    if not prompt:
        raise ValueError("The extracted prompt is empty.")

    return prompt


# Test the prompt manager
if __name__ == "__main__":

    prompt = load_prompt(
        task_name="classification",
        version=2,
        replacements={
            "feedback_text":
            "The delivery was excellent and the product quality was great."
        }
    )

    print("\nPROMPT MANAGER TEST")
    print("=" * 50)
    print(prompt)
    print("=" * 50)
    print("TEST SUCCESSFUL!")




if __name__ == "__main__":

    test_data = {
        "data_analysis": {
            "dataset_summary": "1000 reviews. Positive: 506, Negative: 276, Neutral: 218."
        },
        "summarization": {
            "feedback_data": "Excellent quality and fast delivery. Damaged product and slow refunds."
        },
        "classification": {
            "feedback_text": "The delivery was excellent and the product quality was great."
        },
        "content_generation": {
            "feedback_summary": "Customers appreciate product quality but complain about delivery delays."
        }
    }

    for task_name, replacements in test_data.items():

        for version in [1, 2]:

            prompt = load_prompt(
                task_name=task_name,
                version=version,
                replacements=replacements
            )

            print("\n" + "=" * 60)
            print(f"TASK: {task_name.upper()} | VERSION: {version}")
            print("=" * 60)
            print(prompt[:300])
            print("\nPROMPT LOADED SUCCESSFULLY!")
