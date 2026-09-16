# 🤖 AI Customer Support Agent

An AI-powered customer support agent that classifies customer queries, retrieves similar historical support conversations, generates a grounded response, and decides whether the query should be **AUTO-HANDLED** or **ESCALATED TO A HUMAN**.

---

## 📁 Project Structure

```text
hiver/
│
├── dataset/
│   └── twcs/
│       └── customer_support.csv
│
├── dataset/
│   └── processed/
│       ├── support_pairs.csv
│       └── labeled_data.csv
│
├── models/
│   └── intent_classifier.pkl
│
├── src/
│   ├── agent.py
│   ├── data_processing.py
│   ├── escalation.py
│   ├── intent_classifier.py
│   ├── response_generator.py
│   └── retrieval.py
│
├── scripts/
│   ├── 01_prepare_data.py
│   ├── 02_select_brand.py
│   ├── 03_extract_brand.py
│   ├── 04_train_classifier.py
│   └── 05_test_retrieval.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 1. Requirements

Make sure the following are installed:

* Python 3.9+
* pip
* Git
* Internet connection

The project uses:

* Pandas
* NumPy
* Scikit-learn
* Sentence Transformers
* Joblib
* Streamlit

---

# 2. Clone the Repository

Open Terminal / Command Prompt and run:

```bash
git clone https://github.com/ShyamChauhann/intelligent-fraud-detection-and-risk-scoring-system.git
```

Then enter the project folder:

```bash
cd hiver
```

---

# 3. Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

After activation, the terminal should show something similar to:

```text
(.venv)
```

---

# 4. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

If `pip` does not work, use:

### macOS / Linux

```bash
python3 -m pip3 install -r requirements.txt
```

### Windows

```bash
python -m pip install -r requirements.txt
```

---

# 5. Add the Dataset

Download the **Customer Support on Twitter (TWCS)** dataset.

https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data?select=sample.csv

```text
dataset/twcs/customer_support.csv
```

The important columns are:

```text
tweet_id
author_id
inbound
created_at
text
response_tweet_id
in_response_to_tweet_id
```

---

# 6. Run the Project

Run the scripts in the following order.

## Step 1 — Prepare Dataset

```bash
python3 scripts/01_prepare_data.py
```

Windows:

```bash
python scripts/01_prepare_data.py
```

This checks:

* Dataset shape
* Columns
* Missing values
* Inbound/outbound tweets
* Number of authors
* Number of tweets

---

## Step 2 — Select a Brand

Run:

```bash
python3 scripts/02_select_brand.py
```

Windows:

```bash
python scripts/02_select_brand.py
```

This displays the support accounts available in the dataset.

Example:

```text
Top support accounts:

Account A    XXXXX
Account B    XXXXX
Account C    XXXXX
```

Choose one support account for the project.

---

# 7. Configure the Selected Brand

Open:

```text
scripts/03_extract_brand.py
```

Find:

```python
BRAND_ID = "PUT_SELECTED_BRAND_ID_HERE"
```

Replace it with the selected brand/support account ID.

For example:

```python
BRAND_ID = "AmazonHelp"
```

Use the actual ID obtained from Step 2.

---

# 8. Extract Customer-Support Conversations

Run:

```bash
python3 scripts/03_extract_brand.py
```

Windows:

```bash
python scripts/03_extract_brand.py
```

This creates:

```text
dataset/processed/support_pairs.csv
```

The file contains historical:

```text
Customer Message
       ↓
Brand Response
```

pairs.

---

# 9. Prepare Intent-Labeled Data

Create:

```text
dataset/processed/labeled_data.csv
```

The file should contain:

```text
customer_text,intent
```

Example:

```csv
customer_text,intent
"My package has not arrived",delivery_issue
"I was charged twice",payment_issue
"I want my money back",refund_request
"I cannot login to my account",account_issue
```

The intents should be defined from the selected brand's actual customer-support data.

---

# 10. Train the Intent Classifier

Run:

```bash
python3 scripts/04_train_classifier.py
```

Windows:

```bash
python scripts/04_train_classifier.py
```

The project uses:

### TF-IDF + Logistic Regression

TF-IDF converts customer messages into numerical features, and Logistic Regression predicts the customer's intent.

The trained model is saved as:

```text
models/intent_classifier.pkl
```

---

# 11. Test Historical Retrieval

Run:

```bash
python3 scripts/05_test_retrieval.py
```

Windows:

```bash
python scripts/05_test_retrieval.py
```

The retrieval system uses:

### `all-MiniLM-L6-v2`

from Sentence Transformers.

It converts customer messages into embeddings and uses **cosine similarity** to find historically similar customer-support cases.

Example:

```text
New Query:
"My package hasn't arrived"

        ↓

Semantic Retrieval

        ↓

Historical Cases:
"My delivery is missing"       0.91
"Where is my package?"         0.89
"Delivery is delayed"          0.84
```

---

# 12. Run the Streamlit Application

After completing the above steps, run:

```bash
python3 -m streamlit run app.py
```

The terminal will show a URL similar to:

```text
Local URL: http://localhost:8501
```

Open this URL in your browser.

---

# 13. Test the AI Agent

Enter a customer message such as:

```text
My package has not arrived yet.
```

The system will display:

```text
Intent
↓
Intent Confidence
↓
Historical Similar Cases
↓
Draft Response
↓
AUTO-HANDLE / ESCALATE
↓
Reason
```

---

# 🧠 Models and Techniques Used

| Component             | Model / Technique          |
| --------------------- | -------------------------- |
| Text processing       | Pandas / Python            |
| Feature extraction    | TF-IDF                     |
| Intent classification | Logistic Regression        |
| Semantic embeddings   | `all-MiniLM-L6-v2`         |
| Similarity search     | Cosine Similarity          |
| Response generation   | Historical brand responses |
| Risk decision         | Rule-based escalation      |
| Web interface         | Streamlit                  |

---

# ⚡ Quick Run

After the initial setup, the main execution order is:

```bash
python3 scripts/01_prepare_data.py
python3 scripts/02_select_brand.py
python3 scripts/03_extract_brand.py
python3 scripts/04_train_classifier.py
python3 scripts/05_test_retrieval.py
streamlit run app.py
```

### Windows

```bash
python scripts/01_prepare_data.py
python scripts/02_select_brand.py
python scripts/03_extract_brand.py
python scripts/04_train_classifier.py
python scripts/05_test_retrieval.py
streamlit run app.py
```

---

# ⚠️ Troubleshooting

### `ModuleNotFoundError: No module named 'src'`

Run commands from the **project root**:

```text
hiver/
```

For example:

```bash
python3 scripts/03_extract_brand.py
```

Do not run:

```bash
cd src
python3 agent.py
```

---

### `FileNotFoundError`

Check that the dataset is located at:

```text
dataset/twcs/customer_support.csv
```

and that processed files are created under:

```text
dataset/processed/
```

---

### Sentence Transformer downloads a model

The first retrieval run may download:

```text
all-MiniLM-L6-v2
```

An internet connection is required for the first download. Later runs can use the locally cached model.

---

# 👨‍💻 Project Workflow

```text
Customer Support on Twitter Dataset
                ↓
        Data Preparation
                ↓
          Brand Selection
                ↓
       Conversation Extraction
                ↓
          Intent Labeling
                ↓
     TF-IDF + Logistic Regression
                ↓
        Intent + Confidence
                ↓
    Sentence Transformer Embeddings
                ↓
        Historical Retrieval
                ↓
       Grounded Response
                ↓
       Risk / Escalation Check
                ↓
       ┌────────┴────────┐
       ↓                 ↓
  AUTO-HANDLE         ESCALATE
       ↓                 ↓
    Response         Human Agent
```

---

## Important

Run the commands from the **`hiver` project root directory** and follow the script order shown above.
