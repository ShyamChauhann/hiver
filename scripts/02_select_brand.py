import pandas as pd

INPUT_FILE = "hiver/dataset/twcs/customer_support.csv"

df = pd.read_csv(INPUT_FILE)

# Brand/support tweets
outbound = df[df["inbound"] == False].copy()

print("Number of outbound/support tweets:", len(outbound))

brand_counts = (
    outbound
    .groupby("author_id")
    .size()
    .sort_values(ascending=False)
)

print("\nTop support accounts:\n")
print(brand_counts.head(20))