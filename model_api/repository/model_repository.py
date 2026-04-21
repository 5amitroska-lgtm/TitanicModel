import pickle
import os
from sklearn.tree import DecisionTreeClassifier


class ModelRepository:
    def __init__(self):
        self.__model_file_path = r"C:\Users\TUF\PythonLekcie\TitanicModel\model_api\models"
    def load_model(self, model_name:str)-> DecisionTreeClassifier:
        with open(os.path.join(self.__model_file_path, f"{model_name}.pkl"), "rb") as model_file:
            loaded_model = pickle.load(model_file)
            return loaded_model
