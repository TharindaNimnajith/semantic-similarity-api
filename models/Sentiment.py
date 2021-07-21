from pydantic import BaseModel


class Sentiment(BaseModel):
    polarity: float
    subjectivity: float
