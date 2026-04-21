from fastapi import FastAPI
from model_api.service.model_service import model_router

app = FastAPI()

app.include_router(model_router)