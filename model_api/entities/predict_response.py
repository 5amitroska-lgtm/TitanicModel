from pydantic import BaseModel

class PredictResponse(BaseModel):
    PassengerId: int
    Survived: bool