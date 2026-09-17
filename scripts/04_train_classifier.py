import pandas as pd
import joblib
import os
import sys

sys.path.append(".")

from src.intent_classifier import train_classifier


DATA_FILE = "hiver/dataset/processed/labeled_data.csv"

MODEL_FILE = "models/intent_classifier.pkl"

df = pd.read_csv(DATA_FILE)

print("Dataset:")
print(df.shape)

print("\nIntent distribution:")
print(df["intent"].value_counts())

model = train_classifier(df)

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    MODEL_FILE
)

print("\nModel saved:")
print(MODEL_FILE)