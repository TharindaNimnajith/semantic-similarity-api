from pydantic import BaseModel


class Score(BaseModel):
    spelling: int
    grammar: int
    similarity: int
    objectivity: int
