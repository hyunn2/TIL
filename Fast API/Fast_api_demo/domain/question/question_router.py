from fastapi import APIRouter

from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question"
)


@router.get("/list")
def question_list():
    # @contextlib.contextmanager 어노테이션 적용으로 인해 with 사용 가능
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list