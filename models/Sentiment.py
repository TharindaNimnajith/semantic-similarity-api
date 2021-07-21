# importing BaseModel class from pydantic library
# used to create a new model by parsing and validating input data from keyword arguments
from pydantic import BaseModel


# creating Sentiment model class inheriting BaseModel
class Sentiment(BaseModel):
    polarity: float
    subjectivity: float
