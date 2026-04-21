from fastapi import FastAPI
from model_api.controller.model_controller import model_router

app = FastAPI()

app.include_router(model_router)