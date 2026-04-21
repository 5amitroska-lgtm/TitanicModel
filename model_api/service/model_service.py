import pandas as pd
from fastapi.encoders import jsonable_encoder
from model_api.entities.predict_request import PredictRequst
from model_api.entities.predict_response import PredictResponse
from model_api.repository.model_repository import ModelRepository


class ModelService:

    def __init__(self, model_repository:ModelRepository):
        self.__model_repository = model_repository

    def get_model_info(self, model_name):
        model = self.__model_repository.load_model(model_name)
        return model

    def predict(self, model_name:str, predict_request: PredictRequst):
        model = self.__model_repository.load_model(model_name)
        input_df = pd.DataFrame([jsonable_encoder(predict_request)])
        result = list(model.predict(input_df))
        return PredictResponse(PassengerId=predict_request.PassengerId, Survived=bool(result[0]))
