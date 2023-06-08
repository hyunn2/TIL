
from datetime import datetime
from domain.question.question_schema import QuestionCreate

from models import Question, User
from sqlalchemy.orm import Session

def get_question_list(db: Session):
    question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return question_list

def get_question(db: Session, questio_id: int):
    question = db.query(Question).get(questio_id)
    return question

def create_question(db: Session, question_create: QuestionCreate, user: User):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now(),
                           user=user)
    
    db.add(db_question)
    db.commit()