from typing import Any

from pydantic import BaseModel

import Answer
import Score
import Sentiment


class Result(BaseModel):
    answers: Answer.Answer
    overall: int
    scores: Score.Score
    sentiment: Sentiment.Sentiment
    matches: Any
