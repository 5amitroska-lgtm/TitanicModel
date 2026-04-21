from pydantic import BaseModel

class PredictRequst(BaseModel):
    PassengerId: int
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare : float
    Embarked: float