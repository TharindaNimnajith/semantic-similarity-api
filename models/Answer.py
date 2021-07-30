from pydantic import BaseModel


class Answer(BaseModel):
    question: str
    word_limit: int
    word_count: int
    model_answer: str
    student_answer: str
