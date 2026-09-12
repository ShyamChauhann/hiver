from src.retrieval import HistoricalRetriever

from src.response_generator import (
    generate_response
)

from src.escalation import (
    escalation_decision
)


class CustomerSupportAgent:

    def __init__(
        self,
        classifier,
        historical_data
    ):

        self.classifier = classifier

        self.retriever = HistoricalRetriever(
            historical_data
        )

    def predict_intent(
        self,
        message
    ):

        prediction = self.classifier.predict(
            [message]
        )[0]

        probabilities = (
            self.classifier.predict_proba(
                [message]
            )[0]
        )

        confidence = max(
            probabilities
        )

        return prediction, confidence

    def process(
        self,
        message
    ):

        intent, confidence = (
            self.predict_intent(message)
        )

        historical_cases = (
            self.retriever.search(
                message,
                top_k=5
            )
        )

        best_similarity = 0

        if historical_cases:

            best_similarity = (
                historical_cases[0]["similarity"]
            )

        response = generate_response(
            message,
            historical_cases
        )

        decision = escalation_decision(
            confidence,
            best_similarity,
            message,
            intent
        )

        return {
            "message": message,
            "intent": intent,
            "intent_confidence": confidence,
            "historical_cases": historical_cases,
            "draft_response": response,
            "decision": decision["decision"],
            "decision_reason": decision["reason"]
        }