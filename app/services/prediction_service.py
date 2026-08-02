from app.models.predictor import predict

from app.config import CONFIDENCE_THRESHOLD


class PredictionService:

    @staticmethod

    def predict(text):

        result = predict(text)

        if result["confidence"] < CONFIDENCE_THRESHOLD:

            result["category"] = "Unknown"

        return result