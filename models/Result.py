from typing import Any

from pydantic import BaseModel

from . import Answer
from . import Score
from . import Sentiment


class Result(BaseModel):
    answers: Answer.Answer
    overall: int
    scores: Score.Score
    sentiment: Sentiment.Sentiment
    matches: Any
