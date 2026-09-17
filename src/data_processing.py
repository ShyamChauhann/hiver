import pandas as pd


def load_data(filepath):

    df = pd.read_csv(
        filepath,
        dtype={
            "tweet_id": "string",
            "author_id": "string",
            "inbound": "boolean",
            "response_tweet_id": "string",
            "in_response_to_tweet_id": "string"
        }
    )

    # Clean ID columns
    df["tweet_id"] = df["tweet_id"].str.strip()
    df["author_id"] = df["author_id"].str.strip()
    df["in_response_to_tweet_id"] = (
        df["in_response_to_tweet_id"]
        .str.strip()
    )

    return df

# def load_data(path):
#     return pd.read_csv(path)

def clean_text(text):
    if pd.isna(text):
        return ""

    text = str(text)
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    return text

def create_tweet_lookup(df):

    lookup = {}

    for _, row in df.iterrows():

        tweet_id = str(row["tweet_id"]).strip()

        lookup[tweet_id] = row

    return lookup

# def create_tweet_lookup(df):
    return {
        str(row["tweet_id"]): row
        for _, row in df.iterrows()
    }

def extract_support_pairs(df, brand_id):

    tweet_lookup = create_tweet_lookup(df)

    pairs = []

    # Select brand replies
    brand_tweets = df[
        (df["author_id"].astype(str) == str(brand_id)) &
        (df["inbound"] == False)
    ]

    print("Brand tweets found:", len(brand_tweets))

    for _, brand_tweet in brand_tweets.iterrows():

        parent_id = brand_tweet["in_response_to_tweet_id"]

        # No parent tweet
        if pd.isna(parent_id):
            continue

        parent_id = str(int(parent_id)).strip()
        # parent_id = str(parent_id).strip()

        # Parent tweet not found
        if parent_id not in tweet_lookup:
            continue

        customer_tweet = tweet_lookup[parent_id]

        # Parent must be a customer tweet
        if customer_tweet["inbound"] != True:
            continue

        customer_text = clean_text(customer_tweet["text"])
        brand_text = clean_text(brand_tweet["text"])

        # Ignore empty messages
        if not customer_text or not brand_text:
            continue

        pairs.append({
            "customer_tweet_id": customer_tweet["tweet_id"],
            "brand_tweet_id": brand_tweet["tweet_id"],
            "customer_text": customer_text,
            "brand_response": brand_text
        })

    return pd.DataFrame(pairs)

# def extract_support_pairs(df, brand_id):

    tweet_lookup = create_tweet_lookup(df)

    pairs = []

    brand_tweets = df[
        (df["author_id"] == brand_id) &
        (df["inbound"] == False)
    ]

    for _, brand_tweet in brand_tweets.iterrows():

        parent_id = brand_tweet["in_response_to_tweet_id"]

        if pd.isna(parent_id):
            continue

        parent_id = str(parent_id)

        if parent_id not in tweet_lookup:
            continue

        customer_tweet = tweet_lookup[parent_id]

        if customer_tweet["inbound"] != True:
            continue

        customer_text = clean_text(customer_tweet["text"])
        brand_text = clean_text(brand_tweet["text"])

        if not customer_text or not brand_text:
            continue

        pairs.append({
            "customer_tweet_id": customer_tweet["tweet_id"],
            "brand_tweet_id": brand_tweet["tweet_id"],
            "customer_text": customer_text,
            "brand_response": brand_text
        })

    return pd.DataFrame(pairs)