from pydantic import BaseModel


class Score(BaseModel):
    spelling: float
    grammar: float
    similarity: float
    comprehensiveness: float
    objectivity: float
