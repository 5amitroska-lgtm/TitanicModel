from fastapi import APIRouter

from model_api.entities.predict_request import PredictRequst
from model_api.repository.model_repository import ModelRepository
from model_api.service.model_service import ModelService

model_router = APIRouter()
model_service = ModelService(
    model_repository=ModelRepository()
)
@model_router.get("/models")
def get_all_models():
    """Vypise zoznam vsektych dostupnych modelov k predikcii """
    return {"models": []}

@model_router.get("/models/{model_name}")
def get_model(model_name:str):
    """Vypise info o konkretnom modele"""
    return model_service.get_model_info(model_name)

@model_router.post("/predicts/{model_name}")
def predict(model_name:str,predict_request: PredictRequst):
    """Predikcia so zvolenym modelom"""
    model_service.predict(model_name, predict_request)