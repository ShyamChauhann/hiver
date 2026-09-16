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
git clone https://github.com/ShyamChauhann/hiver.git
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



## Problem Framing

### What does "good" mean for this brand?

For this project, a good customer-support agent is not simply one that produces a fluent response. The primary goal is to provide a response that is:

* **Correctly classified** into the appropriate customer-support intent.
* **Grounded in historical brand responses** rather than invented policies or unsupported information.
* **Safe to automate** when sufficient evidence exists.
* **Escalated to a human** when confidence is low, historical evidence is weak, or the issue requires account-specific or high-risk investigation.
* **Consistent with the brand's historical support behavior.**

We therefore evaluate the system at three levels:

1. **Intent understanding** — Can the system correctly identify what the customer needs?
2. **Historical grounding** — Can it retrieve relevant examples from previous customer-support interactions?
3. **Trustworthy handling** — Does it correctly distinguish cases that can be handled automatically from cases that should be reviewed by a human?

The goal is therefore not maximum automation. The goal is **appropriate automation with a safe fallback to human support**.

### What we chose not to build

To keep the system focused and reproducible, we intentionally did not build:

* A system that directly accesses customer accounts or makes real transactions.
* Automatic refunds, cancellations, payments, or other irreversible actions.
* A system that invents company policies or customer-specific information.
* A fully autonomous customer-support system with no human escalation.
* A general-purpose chatbot for topics outside the selected brand's support domain.

The system is designed as a **decision-support and response-drafting agent**, rather than an unrestricted autonomous customer-service system.

---

# Results

All final results are measured on the manually labelled **Golden Evaluation Set**, which contains [N] examples that were kept separate from the training data.

## Baselines

We compare our system against two baselines.

### Baseline 1 — Majority-Class Baseline

For every customer message, the system predicts the most frequent intent in the training data.

```text
Input
  ↓
Most frequent intent
  ↓
Prediction
```

This is a trivial baseline that establishes the performance that can be obtained without actually understanding the customer message.

### Baseline 2 — TF-IDF + Simple Classifier

The simple baseline uses TF-IDF features with a basic Logistic Regression classifier without the additional historical retrieval and trust layer.

This measures how much value is added by the complete agent architecture beyond a straightforward text-classification system.

## Headline Results

| System                       | Accuracy | Macro F1 | Recall@3 | False Auto-Handle Rate |
| ---------------------------- | -------: | -------: | -------: | ---------------------: |
| Majority-class baseline      |     [XX] |     [XX] |      N/A |                    N/A |
| TF-IDF + Logistic Regression |     [XX] |     [XX] |      N/A |                   [XX] |
| **Full Support Agent**       | **[XX]** | **[XX]** | **[XX]** |               **[XX]** |

> Replace the `[XX]` values with the actual measurements produced by the evaluation scripts. No metric is reported from the training set.

### Models used in the full system

* **TF-IDF** — text feature extraction.
* **Logistic Regression** — customer-intent classification.
* **all-MiniLM-L6-v2** — semantic text embeddings.
* **Cosine Similarity** — historical-case retrieval.
* **Historical response retrieval / LLM** — grounded response drafting.
* **Rule-based risk engine** — AUTO-HANDLE vs ESCALATE decision.

---

# Failure Analysis

We manually reviewed errors from the Golden Evaluation Set and identified the following five major failure modes.

## 1. Ambiguous customer messages

**Example:**

> "[Insert real example from golden_set.csv]"

**Observed problem:**
The message can reasonably belong to more than one intent.

**Hypothesis:**
Short Twitter messages often contain insufficient context. The classifier has limited information from which to distinguish closely related intents.

**Possible improvement:**
Use conversation history or ask a clarification question when intent confidence is low.

---

## 2. Multiple issues in one message

**Example:**

> "[Insert real example from golden_set.csv]"

**Observed problem:**
The customer mentions multiple problems, such as a delivery problem together with a refund request.

**Hypothesis:**
The current classifier predicts a single intent, while real customer messages can contain multiple intents.

**Possible improvement:**
Introduce multi-label intent classification or prioritize the issue requiring the most urgent action.

---

## 3. Weak historical precedent

**Example:**

> "[Insert real example from golden_set.csv]"

**Observed problem:**
The intent classifier correctly identifies the issue, but the retriever returns historically weak or only partially related examples.

**Hypothesis:**
The selected brand has limited historical examples for some less-common problems.

**Possible improvement:**
Increase retrieval coverage, use intent-aware retrieval, or require stronger evidence before generating an automatic response.

---

## 4. Very short or noisy Twitter messages

**Example:**

> "[Insert real example from golden_set.csv]"

**Observed problem:**
Messages containing only a few words, mentions, abbreviations, or informal language are difficult to classify.

**Hypothesis:**
TF-IDF depends heavily on words and phrases present in the training data. Twitter's informal language creates vocabulary variation.

**Possible improvement:**
Use a transformer-based intent classifier or augment the training data with additional examples.

---

## 5. Correct intent but incorrect handling decision

**Example:**

> "[Insert real example from golden_set.csv]"

**Observed problem:**
The classifier identifies the correct intent with high confidence, but the system incorrectly chooses AUTO-HANDLE instead of ESCALATE.

**Hypothesis:**
Intent confidence measures how certain the classifier is about the category; it does not measure whether the case is safe to automate.

**Possible improvement:**
Calibrate the escalation thresholds using a dedicated labelled escalation set and incorporate additional risk signals.

---

# What is misleading about my headline number?

The headline metric should not be interpreted as meaning that the agent is correct on every customer-support problem.

First, the Golden Evaluation Set contains only **[N] manually selected examples** from the selected brand's historical Twitter conversations. It therefore represents a specific sample of the brand's support distribution rather than every possible customer issue.

Second, **intent classification performance does not measure response quality**. A message can be assigned the correct intent while the retrieved historical response is irrelevant or the final draft is not sufficiently helpful.

Third, retrieval quality and escalation quality are separate from classification accuracy. A high intent-confidence score does not guarantee that the system has enough evidence to safely automate the case.

Finally, the evaluation is based on historical Twitter conversations. Customer language, support policies, products, and operating procedures can change over time. Therefore, the reported metrics should be interpreted as evidence of performance on this evaluation set, **not as a guarantee of production performance**.

For this reason, we report multiple metrics rather than relying on a single accuracy number:

* Intent Macro F1
* Intent accuracy
* Retrieval Recall@K
* Response groundedness
* AUTO-HANDLE precision
* False Auto-Handle Rate
* Escalation performance
