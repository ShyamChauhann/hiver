import pandas as pd
import os

INPUT_FILE = "hiver/dataset/twcs/customer_support.csv"

OUTPUT_DIR = "hiver/dataset/processed"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nInbound distribution:")
print(df["inbound"].value_counts())

print("\nNumber of unique authors:")
print(df["author_id"].nunique())

print("\nNumber of unique tweets:")
print(df["tweet_id"].nunique())