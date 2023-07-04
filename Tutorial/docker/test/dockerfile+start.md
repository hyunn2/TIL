# fastapi을 Dockerfile로 만든 후 도커로 실행하기


1. Dockerfile 작성하기

```Dockerfile
FROM python:3.10

MAINTAINER nahkim <nahkim@huray.net>

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

**Dockerfile에 이름 설정하기**

```bash
backend.Dockerfile

docker build -f backend.Dockerfile -t [만들 이름] [실행할 Dockerfile 위치]
```

- f 옵션 : 도커파일을 지정하는 옵션

---

# svelte를 Dockerfile로 만든 후 도커로 실행하기


1. Dockerfile 작성하기

```Dockerfile
FROM node:20.3.0-alpine

MAINTAINER nahkim <nahkim@huray.net>

WORKDIR /app

COPY ./frontend ./

RUN npm install -g npm@9.7.2

RUN npm install

RUN npm install bootstrap

CMD ["npm", "run", "dev", "--", "--host"]

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
docker run -it -d -p 5173:5173 [Image ID]
```

4. 확인

```bash
# 접속
localhost:5173
```


# backend, frontend 연결하기

```
docker build -f backend.Dockerfile -t back .

docker build -f frontend.Dockerfile -t front .

docker run --name back --rm -d -p 8000:8000 --network test-net [image ID]

docker run --name front --rm -d -p 5173:5173 --network test-net [image ID]
```