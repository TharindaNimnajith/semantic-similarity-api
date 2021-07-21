# importing List from typing module
from typing import Any

# importing BaseModel class from pydantic library
# used to create a new model by parsing and validating input data from keyword arguments
from pydantic import BaseModel

# importing Answer model class from Answer module
from . import Answer
# importing Score model class from Score module
from . import Score
# importing Sentiment model class from Sentiment module
from . import Sentiment


# creating Result model class inheriting BaseModel
class Result(BaseModel):
    answers: Answer.Answer
    overall: int
    scores: Score.Score
    sentiment: Sentiment.Sentiment
    matches: Any
