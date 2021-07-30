from typing import Any

from pydantic import BaseModel

from . import Answer
from . import Score
from . import Sentiment


class Result(BaseModel):
    answers: Answer.Answer
    sentiment: Sentiment.Sentiment
    matches: Any
    scores: Score.Score
    overall: int
    ratio: float
    suggestion: str
