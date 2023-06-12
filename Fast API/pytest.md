# pytest

pytest란?
테스트를 하는데 있어서 쉽고, 확장성 있게 사용할 수 있는 프레임워크


## 특징

- Python 3.7이상 이거나 PyPy 3 가능하다.
- 테스트할 파일을 자동 검색해준다.
- 단위 테스트 및 nose test를 할 수 있다.
- 테스트에 통과하지 못한 자세한 정보를 알려준다.
- fixtures 기능
- HTTPX에 기반하여 만들어졌다.

HTTPX란?


## 사용해보기

패키지 설치
```
poetry add pytest
pytest --version
```

필요한 파일
- main.py (테스트할 파일)
- test_main.py (테스트 파일)

```
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_main():
    return {"msg" : "Hello World"}
  
```

```
# test_main.py

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_main_case1():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" : "Hello World"}
```

실행하기
2가지 방법

```
# 방법 1
pytest -q

# 방법 2
pytest 테스트할 파일
```
q 옵션 : 간략하게 보기

<br>

```
# fixtures로 선언된 함수 확인 명령어
pytest --fixtures
```



## fixtures
fixtures란?


### 특징


### fixtures을 이용하여 테스트해보기

필요한 파일
- main.py (테스트할 파일)
- fixtures.py (fixtures 적용된 파일)
- test_main.py (테스트할 파일)

```
# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_main():
    return {"msg" : "Hello World"}
```

```
# fixtures.py

from fastapi.testclient import TestClient

import pytest

from app.main import app

@pytest.fixture
def client():
    """Fast API 클라이언트 인스턴스"""
    return TestClient(app)

```

```
# test_main.py

from .fixtures import *

def test_read_main_case1(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" : "Hello World"}

```

## mocking or mock object
