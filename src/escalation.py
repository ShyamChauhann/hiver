def escalation_decision(
    intent_confidence,
    retrieval_similarity,
    customer_message,
    intent
):

    message = customer_message.lower()

    reasons = []

    # 1. Low intent confidence
    if intent_confidence < 0.60:

        reasons.append(
            "Low intent classification confidence"
        )

    # 2. Weak historical match
    if retrieval_similarity < 0.55:

        reasons.append(
            "No strong historical precedent"
        )

    # 3. Account-specific signals
    account_terms = [
        "account",
        "charged",
        "payment",
        "refund",
        "money",
        "bank",
        "transaction"
    ]

    if any(
        word in message
        for word in account_terms
    ):

        if intent in [
            "payment_issue",
            "refund_request",
            "account_issue"
        ]:

            reasons.append(
                "Account-specific issue may require human investigation"
            )

    # 4. Legal/risk signals
    risk_terms = [
        "lawyer",
        "legal",
        "police",
        "fraud",
        "lawsuit",
        "court"
    ]

    if any(
        word in message
        for word in risk_terms
    ):

        reasons.append(
            "Potential high-risk or legal issue"
        )

    # 5. Strong negative escalation
    escalation_terms = [
        "still not fixed",
        "again",
        "third time",
        "nobody helped",
        "already contacted"
    ]

    if any(
        phrase in message
        for phrase in escalation_terms
    ):

        reasons.append(
            "Customer reports repeated or unresolved issue"
        )

    if reasons:

        return {
            "decision": "ESCALATE",
            "reason": "; ".join(reasons)
        }

    return {
        "decision": "AUTO-HANDLE",
        "reason": (
            "High-confidence classification with "
            "sufficient historical precedent and "
            "no major escalation signals."
        )
    }