from fastapi import APIRouter

model_router = APIRouter()

@model_router.get("/models")
def get_all_models():
    return {"models": []}