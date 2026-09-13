import streamlit as st
import pandas as pd
import joblib
import sys

sys.path.append(".")

from src.agent import CustomerSupportAgent

st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def load_agent():

    classifier = joblib.load(
        "models/intent_classifier.pkl"
    )

    data = pd.read_csv(
        "dataset/processed/support_pairs.csv"
    )

    agent = CustomerSupportAgent(
        classifier,
        data
    )

    return agent

st.title(
    "🤖 AI Customer Support Agent"
)

st.write(
    """
    AI-powered customer support agent using
    historical brand conversations.
    """
)

agent = load_agent()

message = st.text_area(
    "Customer message",
    placeholder=(
        "Example: My order hasn't arrived yet..."
    ),
    height=150
)


if st.button(
    "Analyze Message",
    type="primary"
):

    if not message.strip():

        st.warning(
            "Please enter a customer message."
        )
    else:
        with st.spinner(
            "Analyzing..."
        ):
            result = agent.process(
                message
            )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Intent"
            )

            st.success(
                result["intent"]
            )

        with col2:

            st.subheader(
                "Confidence"
            )

            st.metric(
                "Classification confidence",
                f"{result['intent_confidence']:.2%}"
            )

        st.divider()

        st.subheader(
            "Historical Cases"
        )

        for i, case in enumerate(
            result["historical_cases"],
            start=1
        ):

            with st.expander(
                f"Case {i} "
                f"(similarity: "
                f"{case['similarity']:.2%})"
            ):

                st.write(
                    "**Customer:**"
                )

                st.write(
                    case["customer_text"]
                )

                st.write(
                    "**Historical Brand Response:**"
                )

                st.write(
                    case["brand_response"]
                )

        st.divider()

        st.subheader(
            "Draft Response"
        )

        if result["draft_response"]:

            st.info(
                result["draft_response"]
            )

        else:

            st.warning(
                "No sufficiently similar historical "
                "response was found."
            )

        st.divider()

        st.subheader(
            "Decision"
        )

        if result["decision"] == "AUTO-HANDLE":

            st.success(
                "🟢 AUTO-HANDLE"
            )

        else:

            st.error(
                "🔴 ESCALATE TO HUMAN"
            )

        st.write(
            "**Reason:**",
            result["decision_reason"]
        )

