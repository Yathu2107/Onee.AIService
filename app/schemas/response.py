from pydantic import BaseModel


class PredictionResponse(BaseModel):

    category: str

    confidence: float