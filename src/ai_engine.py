
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


# Locate project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# API configuration
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-5.5")


# Initialize OpenAI client
if not API_KEY or API_KEY == "your_actual_api_key":
    raise ValueError(
        "OpenAI API key is missing. "
        "Please configure your .env file."
    )

client = OpenAI(api_key=API_KEY)


def generate_response(prompt):
    """
    Generate an AI response using OpenAI API.
    """

    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt
    )

    return response.output_text


# Test API connection
if __name__ == "__main__":

    test_prompt = """
    Classify this customer feedback into Positive,
    Negative, or Neutral.

    Customer feedback:
    "The product quality is excellent and delivery
    was very fast."

    Give a short explanation.
    """

    print("\nOPENAI API CONNECTION TEST")
    print("=" * 50)

    try:
        result = generate_response(test_prompt)

        print("\nAI RESPONSE:")
        print(result)

        print("\nAPI CONNECTION SUCCESSFUL!")

    except Exception as error:
        print("\nAPI CONNECTION FAILED!")
        print("Error:", error)
