# peotry이란?

파이썬에서 의존성 관리 및 패키징을 위한 도구

시스템 요구사항 : 파이썬 3.7 이상

---

## 특징

- build/publish 지원
- 가상환경(virtualenv)을 자체적으로 관리



## 설치 및 기본적인 사용법


### 설치 방법

리눅스, macOS, WSL
``` curl -sSL https://install.python-poetry.org | python3 - ```

만약 오류가 날 경우
`Exception: This build of python cannot create venvs without using symlinks`

```brew install poetry```

설치 확인
``` poetry --version ```



### 기본적인 사용법

방법 1. 프로젝트를 설정한다.

``` poetry new [프로젝트명] ```
그 후 pyproject.toml파일에서 수정

방법 2. 
프로젝트 폴더에 들어간 후 명령어 실행

``` poetry init ```
pyproject.toml 파일만 생성되며, 대화 형식으로 패키지 설치


### 종속성(의존성) 설치

``` poetry install ```

위의 명령어 실행전 상태
1. poetry.lock 포함하지 않은 상태
2. poetry.lock 포함한 상태


**poetry.lock의 역할**
poetry.lock은 정의된 의존성 파일을 설치하여 같은 환경에서 개발을 할 수 있게 도와준다.

1. poetry.lock이 없는 상태에서 명령어(poetry install)를 실행할 경우
pyproject.toml 파일에 있는 패키지의 의존성을 해결하고 가장 최신 버전으로 다운로드함
그 후 모든 패키지와 버전을 파일(poetry.lock)에 기록하고 프로젝트 팀원들과 동일한 버전을 공유(사용)하기 위해선 poetry.lock파일을 커밋해야한다.


2. poetry.lock이 있는 상태에서 명령어(poetry install)를 실행할 경우
이미 poetry.lock이 있다는 것은 이미 명령어(poetry install)를 실행한 상태이므로 
명령어(poetry install)를 실행할 경우 poetry.lock 파일에 있는 버전으로 패키지들이 다운받아진다.
최신 버전이 아닐 수 있으니 주의!


### 명령어
- new
- init
- install
- update
- add
- remove
- show
- build
- publish
- config
- run
- check
- search
- lock
- export
- env info


#### 기타
**requirements.txt 추출하기**

```bash poetry export -f requirements.txt > requirements.txt```

(poetry build 명령어를 이용해 생성된 파일로 배포도 가능)

**명령어 사용법 확인**

1. 

``` poetry help [명령어] ```

2. 

``` poetry [명령어] --help ```