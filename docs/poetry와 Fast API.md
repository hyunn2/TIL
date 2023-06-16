# poetry에 Fast API 적용하여 서버 실행해보기
---

## 실행 방법

```
poetry run uvicorn main:app --reload
```

- uvicorn : 비동기 호출을 지원하는 파이썬용 저사양 웹서버
- main : main.py
- app : main.pydml app 객체
- reload : 프로그램이 변경되면 서버 재시작 없이 내용을 반영하는 옵션


## 서버 실행 성공시
![실행 화면](./poetry%20%2B%20Fast%20API%20%EC%84%9C%EB%B2%84%20%EC%8B%A4%ED%96%89.png)

127.0.0.1:8000 으로 서버 실행

### 테스트 하는 방법
URL 실행
http://127.0.0.1:8000/docs

실행 가능한 문서들이 뜨는데 거기서 테스트 가능

### 읽기 가능한 문서 보기
http://127.0.0.1:8000/redoc