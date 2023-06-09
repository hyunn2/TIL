import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

# QuestionCreate를 상속하기 때문에 검증 메소드(not_empty)도 동일하게 동작!
class QuestionUpdate(QuestionCreate):
    question_id: int

class QuestionDelete(BaseModel):
    question_id: int
