
import pandas as pd

# Load customer feedback dataset
DATASET_PATH = "dataset/customer_feedback_dataset.csv"

df = pd.read_csv(DATASET_PATH)

print("\n====================================")
print(" CUSTOMER FEEDBACK DATA ANALYSIS")
print("====================================")

# 1. Dataset dimensions
print("\n1. Dataset Shape")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. First five records
print("\n2. First Five Records")
print(df.head())

# 3. Dataset information
print("\n3. Dataset Information")
print(df.info())

# 4. Missing values
print("\n4. Missing Values")
print(df.isnull().sum())

# 5. Duplicate records
print("\n5. Duplicate Records")
print(df.duplicated().sum())

# 6. Sentiment distribution
print("\n6. Sentiment Distribution")
print(df["sentiment_label"].value_counts())

# 7. Average customer rating
print("\n7. Average Customer Rating")
print(round(df["rating"].mean(), 2))

# 8. Product category analysis
print("\n8. Feedback by Product Category")
print(df["product_category"].value_counts())

# 9. Save processed dataset
df.to_csv(
    "dataset/processed_dataset.csv",
    index=False
)

print("\n====================================")
print(" DATA PREPROCESSING COMPLETED!")
print("====================================")
