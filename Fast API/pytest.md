# pytest

테스트를 하는데 있어서 쉽고, 확장성 있게 사용할 수 있는 프레임워크

<br>

## 특징

- Python 3.7이상 이거나 PyPy3에서 가능하다.
- 테스트할 파일을 자동 검색해준다.
- 단위 테스트 및 nose test를 할 수 있다.
- 테스트에 통과하지 못한 자세한 정보를 알려준다.
- fixtures 기능
- HTTPX에 기반하여 만들어졌다.

<br>

HTTPX란?
<br>
sync와 async API 및 HTTP/1.1과 HTTP/2를 지원하는 파이썬3용 HTTP 클라이언트

<br>

## 사용해보기

**패키지 설치**
```
poetry add pytest
pytest --version
```

**필요한 파일**
- main.py (테스트할 파일)
- test_main.py (테스트 파일)

<br>

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

## 실행하기
2가지 방법이 있다.

```
# 방법 1
pytest -q -s

# 방법 2
pytest 테스트할 파일 경로
```
q 옵션 : 간략하게 보기



s 옵션 : Captured stdout call 켜기

<br>

```
# fixtures로 선언된 함수 확인 명령어
pytest --fixtures
```



## fixtures
fixtures란?

<br>

### 특징

### Fixture scopes

Fixtures는 테스트시 처음 요청될 때 생성되며, 스코프 기반에 따라 소멸된다.


<br>

``` @pytest.fixture(scope="function") == @pytest.fixture ```
- function: 기본 스코프이며, 함수가 끝나면 소멸된다. (함수 단위로 생성됨)


<br>

``` @pytest.fixture(scope="class") ```
- class: 클래스가 끝나면 소멸된다. (클래스 단위로 생성)

<br>

``` @pytest.fixture(scope="module") ```
- module: 모듈이 끝나면 소멸된다. (모듈 단위로 생성)

<br>

``` @pytest.fixture(scope="package") ```
- package: 패키지 단위로 소멸된다. (패키지 단위로 생성)

<br>

``` @pytest.fixture(scope="session") ```
- session: 세션 단위로 소멸된다. (세션 단위로 생성)

한번에 하나의 인스턴스가 캐쉬된다.

<br>

### yield fixtures

return 대신 사용한다.

<br>

### fixtures을 이용하여 테스트해보기

**필요한 파일**
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
