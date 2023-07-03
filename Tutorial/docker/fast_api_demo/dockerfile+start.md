# fastapi을 dockerfile로 만든 후 도커로 실행하기


1. Dockerfile 작성하기

```Dockerfile
FROM python:3.10

MAINTAINER nahkim "<nahkim@huray.net>"

ENV POETRY_VERSION=1.5.1

ENV POETRY_HOME=/etc/poetry

ENV PATH=/etc/poetry/bin:$PATH

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /src

CMD echo poetry --version

COPY ./backend ./

RUN poetry install --no-root

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

2. Dockerfile 빌드

```bash
docker build -t [만들 이미지 이름] [실행할 Dockerfile 위치]

# ex
docker build -t test:1 .
```
t 옵션 : 이름과 태그 설정 (위의 예시론 [이름:태그], 태그를 안쓸 경우 latest로 뜬다.)


3. images 실행

```bash
docker run -it -d -p 8000:8000 [Image ID]
```

4. 확인

```bash
# 접속
localhost:8000
```

<br>

**컨테이너 접속하기**

컨테이너가 실행되고 있어야함!
```bash
docker exec -it [container ID] /bin/bash
```


**Container log 보기**

```bash
docker container logs -t [Container ID]
```