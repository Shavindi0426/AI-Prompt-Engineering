
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Define project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "outputs" / "prompt_evaluation.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Load evaluation data
df = pd.read_csv(INPUT_FILE)

# Remove accidental empty rows
df = df.dropna(subset=["Experiment", "Prompt Version"])

# Calculate average scores by prompt version
version_summary = (
    df.groupby("Prompt Version")["Average Score"]
    .mean()
    .reset_index()
)

print("\nOVERALL PROMPT EVALUATION")
print(version_summary.to_string(index=False))

# Compare initial and improved scores by experiment
comparison = df.pivot(
    index="Experiment",
    columns="Prompt Version",
    values="Average Score"
)

comparison["Improvement"] = (
    comparison["Improved (V2)"] - comparison["Initial (V1)"]
)

print("\nEXPERIMENT COMPARISON")
print(comparison.to_string())

# Save comparison results
comparison.to_csv(OUTPUT_DIR / "prompt_comparison.csv")

# Generate comparison chart
comparison[["Initial (V1)", "Improved (V2)"]].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Initial vs Improved Prompt Evaluation")
plt.xlabel("Prompt Engineering Experiments")
plt.ylabel("Average Evaluation Score (out of 5)")
plt.ylim(0, 5.5)
plt.xticks(rotation=0)
plt.legend(title="Prompt Version")
plt.tight_layout()

# Save chart
chart_path = OUTPUT_DIR / "prompt_comparison.png"
plt.savefig(chart_path, dpi=300)
plt.show()

print("\nEvaluation completed successfully!")
print("Comparison CSV:", OUTPUT_DIR / "prompt_comparison.csv")
print("Comparison Chart:", chart_path)
