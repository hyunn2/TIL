# FastAPI


## Fast API 특징
- 


## 작동 방식
1. 특정 요청에 대해 경로가 있는지 검증한다.
2. 특정 요청에 대해 매개변수가 있을 경우 맞는 타입이 들어왔는지 검증한다.
3. 쿼리가 있다면 쿼리 매개변수를 검사한다.
4. 요청에 대한 매개변수를 JSON로 읽고 함수를 실행후 retrun 해줌


- Starlette(웹 관련)
- Pydantic(데이터 검증 관련)

데이터 검증에서 만약 users/me와 users/{user_id} (int) 2개가 있을 경우
경로는 순차적으로 검증을 하기 때문에 users/me가 먼저 와야한다.
그렇지 않으면 users/{user_id}는 매개변수 user_id의 값을 "me"라고 생각하여 에러를 발생시킬 수 있음
그러면 users/{int형} users/{str형} 일 경우는 없으니까 상관이 없는건가? 있을수는 없나?

## 모델 관련
alembic 사용법
```
poetry add alembic
poetry run alembic init migrations
```

## 가상환경 쉘 실행

```
poetry shell
python
>>> 모델 객체 생성후 SessionLocal 클래스를 생성
>>> db = SessionLocal()
>>> db.add([쿼리])
>>> db.commit() # DB에 데이터 저장
```

만약 이미 가상환경이 실행되고 있다면 파이썬으로 쉘 접속해서 사용하면 됨!

## 라우터 설정
1. 도메인 디렉토리를 생성 후 특정 테이블 관련 API 생성 (main.py에 모두 넣을 경우 규모가 커질시 찾기도 어렵고 유지보수가 어렵고 확장성이 부족하다)
2. 라우터 import 및 생성
```
# domain/폴더이름(도메인 이름)/파일 이름
from fastapi import APIRouter

router = APIRouter(
  prefix="/api/question"
)

@router.get("/list")
def question_list():
  pass
```
3. main.py에 등록하기
```
# main.py

from domain.[폴더 이름(도메인)] import [파일 이름]

app.include_router([파일 이름].router)

```

## 의존성 주입(DB 세션 생성과 반환 자동화)
- contextlib 라이브러리 사용
1. database.py 파일에 설정한다.
```
# 라이브러리 설정
import contextlib

# 제너레이터 함수 생성
# 아래 어노테이션을 적용해야 with문과 함께 사용 가능하다.
@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```
방법 1. 의존성 주입할 함수에 설정한다. (with문)
```
from database import get_db

def [의존성 주입할 함수]():
  with get_db() as db:
    원래 함수 내용

```

방법 2. with문 말고 FastAPI의 Depends 사용하기
어노테이션 제거한다. (@contextlib.contextmanager)
Depends의 경우 contextmanager를 자동으로 적용되기 때문에 제거한다.(제거 안하면 오류 발생)

```
from fastapi import Depends
from sqlalchemy.orm import Session

def [의존성 주입할 함수](db: Session = Depends(get_db)):
  원래 함수 내용

```

## Pydantic
입출력 항목을 정의하고 검증하는 라이브러리

- 입출력 항목 갯수와 타입 설정
- 입출력 항목 필수값 확인
- 입출력 항목 데이터 검증

**스키마를 사용하면 좋은 점**
데이터 출력시 실제 리턴되는 값을 수정하지 않고 스키마에서 제외만하면 되기 때문에 편리하다.


**적용 방법**
1. 출력 스키마 생성
```
# 스키마 파일 생성

import datetime

from pydantic import BaseModel

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    # Question모델은 Question 스키마로 자동 변환이 되지 않기 때문에 아래 설정을 해줘야함
    class Config:
        orm_mode = True

```
*스키마 : 데이터 구조와 명세

필수 항목 설정을 제외하려면
```
# 문자열 또는 None값을 가지고 디폴트 값은 None값이다.
subject: str | None = None
```

2. 스키마 적용하기
```
# response_model 추가
@router.get("/list", response_model=list[question_schema.Question])
```



참고 :
[문서](https://fastapi.tiangolo.com/)
[소스 코드](https://github.com/tiangolo/fastapi)