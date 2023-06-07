from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema
from models import Question

router = APIRouter(
    prefix="/api/question"
)


@router.get("/list", response_model=list[question_schema.Question])
# db 객체가 Session 타입이며 db객체에 get_db에 의해 생성된 객체가 주입됨
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list