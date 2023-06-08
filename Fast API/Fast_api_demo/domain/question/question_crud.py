from models import Question
from sqlalchemy.orm import Session

def get_question_list(db: Session):
    question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return question_list

def get_question(db: Session, questio_id: int):
    question = db.query(Question).get(questio_id)
    return question
