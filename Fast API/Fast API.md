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


참고 :
[문서](https://fastapi.tiangolo.com/)
[소스 코드](https://github.com/tiangolo/fastapi)