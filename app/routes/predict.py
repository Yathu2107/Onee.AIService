from fastapi import APIRouter, Depends

from app.schemas.request import PredictionRequest

from app.services.prediction_service import PredictionService

from app.core.response import success

from app.core.security import verify_api_key

router = APIRouter(

    prefix="/api/v1/predict",

    tags=["Prediction"],

    dependencies=[Depends(verify_api_key)]

)

@router.post("")

def predict(request: PredictionRequest):

    result = PredictionService.predict(

        request.text

    )

    return success(result)