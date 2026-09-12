# hiver
Trying to turn a messy real-world dataset into a working AI system and prove it works.

find dataset here : https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data?select=sample.csv


customer-support-ai-agent/
│
├── data/
│   ├── raw/
│   │   └── customer_support.csv
│   │
│   └── processed/
│       ├── brand_tweets.csv
│       ├── support_pairs.csv
│       └── labeled_data.csv
│
├── models/
│   ├── intent_classifier.pkl
│   ├── intent_vectorizer.pkl
│   └── embeddings.npy
│
├── config/
│   └── intents.json
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_processing.py
│   ├── brand_selection.py
│   ├── intent_classifier.py
│   ├── retrieval.py
│   ├── response_generator.py
│   ├── escalation.py
│   └── agent.py
│
├── scripts/
│   ├── 01_prepare_data.py
│   ├── 02_select_brand.py
│   ├── 03_create_intents.py
│   ├── 04_train_classifier.py
│   └── 05_build_retriever.py
│
├── evaluation/
│   └── evaluate.py
│
├── app.py
│
├── requirements.txt
├── README.md
└── .gitignore


inbound = True ( Customer message )
inbound = False ( Brand/support response )


run this from hiver directory
    python3 scripts/01_prepare_data.py
    python3 scripts/02_select_brand.py
    python3 scripts/03_extract_brand.py

