import re

def clean_response(text):

    text = str(text)

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def generate_response(
    customer_message,
    retrieved_cases,
    threshold=0.55
):

    if not retrieved_cases:
        return None

    best_case = retrieved_cases[0]

    similarity = best_case["similarity"]

    if similarity < threshold:
        return None

    response = clean_response(
        best_case["brand_response"]
    )

    return response