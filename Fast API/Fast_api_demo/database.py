from sqlalchemy import create_engine
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

