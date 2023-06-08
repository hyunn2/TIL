from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB 접속 주소
# 프로젝트 루트 디렉터리에 저장
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

# create_engine : 커넥션 풀 생성(DB 접속 세션 수 제어)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# DB 접속을 위한 클래스
# autocommit : 데이터 변경시 DB에 즉시 변경사항이 적용 유무
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB 모델 구성시 필요한 클래스
Base = declarative_base()

# ORM 사용을 위한 DB 수정(SQLite만 추가해줘야함)
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)


# DB 세션의 생성과 반환을 자동화하는 제너레이터 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()