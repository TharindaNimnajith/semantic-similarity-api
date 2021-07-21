# importing BaseModel class from pydantic library
# used to create a new model by parsing and validating input data from keyword arguments
from pydantic import BaseModel


# creating Score model class inheriting BaseModel
class Score(BaseModel):
    spelling: float
    grammar: float
    similarity: float
