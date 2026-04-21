from fastapi import APIRouter

model_router = APIRouter()

@model_router.get("/models")
def get_all_models():
    """Vypise zoznam vsektych dostupnych modelov k predikcii """
    return {"models": []}

@model_router.get("/models/{model_name")
def get_model(model_name:str):
    """Vypise info o konkretnom modele"""
    return model_name

@model_router.post("/predicts/{model_name}")
def predict(model_name:str,data:dict):
    """Predikcia so zvolenym modelom"""
    pass