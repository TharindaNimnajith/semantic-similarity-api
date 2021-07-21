from pydantic import BaseModel


class Answer(BaseModel):
    model_answer: str
    student_answer: str
