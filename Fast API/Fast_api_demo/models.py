from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base


# database.py에서 정의한 Base 클래스를 상속하여 만듬
class Question(Base):
    # 모델에 의해 관리되는 테이블
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

