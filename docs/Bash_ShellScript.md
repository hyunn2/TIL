# Bash 쉘스크립트

<br>

## 커널(Kernel)

하드웨어와 애플리케이션 간에 상호 작용을 도와주는 운영체제의 핵심 구성 요소

<br>

커널 버전 확인 방법
```
uname -r
```

<br>

## 쉘(Shell)

유닉스 계열 시스템에서 사용하는 대화형 인터페이스

```
# 현재 사용중인 쉘 확인
echo $SHELL

# 사용가능한 쉘 확인
cat /etc/shells
```

<br>

### 프로세스 실행 방식

```
# 포그라운드 방식
sample.sh

# 백그라운드 방식 (명령어 뒤에 & 추가)
sample.sh &


# nohup(no hang up)
# 작업 시간이 오래 걸릴 경우 nohup 명령어를 사용하여 사용자 터미널 세션이 종료되어도 작업이 종료될때까지 프로세스 실행
nohup sample.sh &

```

<br>

### 한글이 깨질시

LANG을 UTF-8로 수정하면 됨

```
# LANG 확인
locale
```

<br>

vi에서 일시적으로 설정 방법
EX 모드에서 set encoding=utf-8 입력
```
:set encoding=utf-8
```

<br>

기본 설정 방법 2가지
1. ~/.vimrc 파일에 encoding=utf-8 입력후 저장
2. /etc/vim/vimrc 파일에 encoding=utf-8 입력후 저장

<br>

### 명령어 종류

- 관리 명령어
  - 시스템 관리
  - 사용자 관리
  - 파일 시스템
  - 압축

<br>

- 처리 명령어
  - 문자열 처리
  - 날짜
  - 파일
  - 네트워크
  - 형식 파일
  - 기타

<br>

# 쉘 스크립트
bash built-in 명령어

- 파이프, 리다이렉션
- env, set, export

<br>

**파이프**

표준 입력, 출력 및 에러를 연결하기 위해 사용

```
# 기본 형태
command1 | command2

# 에러도 전달할 경우
command1 |& command2

ex) cat file.txt | grep word
```

<br>

**리다이렉션**

```
command [FD] > filename
```

종류
- '<' 파일 읽기
- '>' 파일 쓰기(overwrite)
- '>>' 파일 쓰기(insert)

<br>

- 2>&1
<br>
표준 에러를 표준 출력으로 리다이렉션 (파일 디스크립터 번호를 통해)

- /dev/null
<br>
표준 출력을 버리기 위한 용도로 사용하는 디스크립터


