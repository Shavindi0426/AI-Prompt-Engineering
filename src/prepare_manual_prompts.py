
import sys
from pathlib import Path
import pandas as pd

# Import prompt manager
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

from prompt_manager import load_prompt


# File paths
DATASET_PATH = BASE_DIR / "dataset" / "processed_dataset.csv"

OUTPUT_DIR = BASE_DIR / "outputs" / "manual_prompts"

INITIAL_DIR = OUTPUT_DIR / "initial"
IMPROVED_DIR = OUTPUT_DIR / "improved"


def prepare_dataset_summary(df):
    """
    Prepare statistical information for data analysis.
    """

    total_reviews = len(df)

    sentiment_counts = (
        df["sentiment_label"].value_counts().to_dict()
    )

    average_rating = df["rating"].mean()

    category_ratings = (
        df.groupby("product_category")["rating"]
        .mean()
        .round(2)
        .to_dict()
    )

    channel_counts = (
        df["feedback_channel"].value_counts().to_dict()
    )

    summary = f"""
CUSTOMER FEEDBACK DATASET SUMMARY

Total Reviews: {total_reviews}

Average Customer Rating: {average_rating:.2f}/5

Sentiment Distribution:
{sentiment_counts}

Average Rating by Product Category:
{category_ratings}

Feedback Channels:
{channel_counts}
"""

    return summary


def prepare_feedback_data(df):
    """
    Select representative feedback for summarization.
    """

    samples = []

    for sentiment in ["Positive", "Negative", "Neutral"]:

        subset = df[df["sentiment_label"] == sentiment].head(10)

        for _, row in subset.iterrows():

            samples.append(
                f"Review ID: {row['review_id']}\n"
                f"Category: {row['product_category']}\n"
                f"Rating: {row['rating']}/5\n"
                f"Feedback: {row['feedback_text']}\n"
                f"Reference Sentiment: {sentiment}"
            )

    return "\n\n".join(samples)


def prepare_classification_feedback(df):
    """
    Select one sample customer review for classification.
    """

    sample = df.iloc[0]

    return {
        "review_id": sample["review_id"],
        "feedback_text": sample["feedback_text"]
    }


def prepare_feedback_summary(df):
    """
    Prepare findings for content generation.
    """

    summary = prepare_dataset_summary(df)

    negative_feedback = df[
        df["sentiment_label"] == "Negative"
    ]["feedback_text"].head(10).tolist()

    summary += "\n\nEXAMPLES OF CUSTOMER COMPLAINTS:\n"

    for feedback in negative_feedback:
        summary += f"- {feedback}\n"

    return summary


def save_prompt(task_name, version, prompt):
    """
    Save completed prompts into separate folders.
    """

    target_dir = INITIAL_DIR if version == 1 else IMPROVED_DIR

    target_dir.mkdir(parents=True, exist_ok=True)

    file_path = target_dir / f"{task_name}.txt"

    file_path.write_text(prompt, encoding="utf-8")

    print(f"Saved: {file_path.relative_to(BASE_DIR)}")


def main():

    print("\nCUSTOMER FEEDBACK PROMPT PREPARATION")
    print("=" * 50)

    # Load dataset
    df = pd.read_csv(DATASET_PATH)

    print("Dataset loaded successfully.")
    print("Total records:", len(df))

    # Prepare data for each task
    dataset_summary = prepare_dataset_summary(df)

    feedback_data = prepare_feedback_data(df)

    classification_data = prepare_classification_feedback(df)

    feedback_summary = prepare_feedback_summary(df)

    task_data = {

        "data_analysis": {
            "dataset_summary": dataset_summary
        },

        "summarization": {
            "feedback_data": feedback_data
        },

        "classification": classification_data,

        "content_generation": {
            "feedback_summary": feedback_summary
        }
    }

    # Generate initial and improved prompts
    for task_name, replacements in task_data.items():

        for version in [1, 2]:

            prompt = load_prompt(
                task_name=task_name,
                version=version,
                replacements=replacements
            )

            save_prompt(
                task_name,
                version,
                prompt
            )

    print("\n" + "=" * 50)
    print("ALL PROMPTS PREPARED SUCCESSFULLY!")
    print("Total prompts generated: 8")
    print("=" * 50)


if __name__ == "__main__":
    main()
