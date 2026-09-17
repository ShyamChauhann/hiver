import pandas as pd
import sys
import os

sys.path.append(".")
from src.data_processing import load_data,extract_support_pairs

INPUT_FILE = "hiver/dataset/twcs/customer_support.csv"

# CHANGE THIS AFTER RUNNING 02_select_brand.py
BRAND_ID = "sprintcare"

OUTPUT_FILE = "hiver/dataset/processed/support_pairs.csv"

print("Loading dataset...")

df = load_data(INPUT_FILE)

print("Extracting conversations...")

pairs = extract_support_pairs(
    df,
    BRAND_ID
)

print("\nNumber of support pairs:")
print(len(pairs))

os.makedirs("data/processed", exist_ok=True)

pairs.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nSaved:")
print(OUTPUT_FILE)