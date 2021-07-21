# importing BaseModel class from pydantic library
# used to create a new model by parsing and validating input data from keyword arguments
from pydantic import BaseModel


# creating Answer model class inheriting BaseModel
class Answer(BaseModel):
    model_answer: str
    student_answer: str
