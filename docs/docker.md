# docker

컨테이너 생성 및 관리 도구

항상 동일한 동작과 결과를 가져다준다. 관리 프로세스를 단순화해준다.

## 컨테이너 특징

- 고립성
- 하나의 task에 집중
- 공유 및 재생산을 할 수 있음
- stateless(무상태) -> 볼륨을 제외한 데이터는 컨테이너가 종료되면 손실됨
- 이미지를 기반으로 컨테이너를 실행함

볼륨 : 로컬 호스트 머신의 폴더로 미러링하거나 복사할 수 있음


## 이미지 특징
dockerfile, Docker hub로 만듬

dockerfile에 코드와 환경이 포함되어 있음

- 공유가 가능
- 이미지를 기반으로 다중 컨테이너를 만들 수 있음
- 읽기 전용이므로 그 자체는 실행되지 않음
- 컨테이너의 블루프린트

멀티스테이지 빌드
 


## docker 명령어

exec

컨테이너 환경에 명령어 실행

<br>

docker image inspect

이미지에 대한 정보

<br>

docker cp

<br>

## docker 옵션

-d

보통 데몬 모드라고 부름, 컨테이너가 백그라운드로 실행

<br>


detached 모드 vs attached 모드

detached 모드

attached 모드

<br>

-i

표준 입력 활성화

<br>

-t

TTY 모드 사용

<br>

-p [host port:container port]

호스트의 포트와 컨테이너의 포트 연결

<br>

-h

컨테이너의 호스트 이름을 설정

<br>

--name

컨테이너 이름 설정

<br>

--rm

프로세스 종료시 컨테이너 자동 제거
(docker stop시 컨테이너 제거)

<br>

--save

N개의 쓰기 작업이 수행되면 M초마다 DB의 스냅샷을 저장

<br>

--loglevel

로그를 어디까지 보여줄지 선택하는 옵션

<br>

-- 네트워크 관련 --

컨테이너 이름을 도메인, 즉 주소로 사용할 수 있다.
도커는 컨테이너의 이름을 보고 코드에 플러그인된 컨테이너의 IP주소를 연결한다.


<br>

--network

```
# p 옵션 안줘도 됨
docker run -d --name mongodb --network favorite-net mongo
```

컨테이너에 연결시킬 네트워크 설정
모든 컨테이너가 서로 통신할 수 있는 네트워크가 생성됨


네트워크 생성
```
docker network create [이름 설정]

위의 코드에선 favorite-net
```

기존의 모든 네트워크 검사
```
docker network ls
```


-- 로그 확인 --
```
docker log [containerID]
```


컨테이너 로그 확인
```
docker container logs -t [containerID]
```

중지된 모든 컨테이너를 제거
```
docker container prune
```

<br>



### Dockerfile

<br>

이미지 생성

docker build [dockerfile 위치]

컨테이너 실행

docker run -p [애플리케이션에 액세스하려는 로컬 포트]:[내부 도커 컨테이너 노출 포트] [Container ID or Container Names]

p 옵션 : 컨테이너 포트를 호스트 OS와 매핑시킬수 있는 옵션

```Dockerfile
FROM 베이스 이미지

WORKDIR [지정한 폴더]
# 하위 명령어부터 root가 아니라 지정한 폴더에서 실행함

COPY [이미지 외부 경로] [컨테이너의 내부 경로]

RUN [실행할 명령어]
# 이미지가 생성될때 실행

EXPOSE [포트 번호]
# 특정 포트 노출
# 명시만 하고 컨테이너 실행시 포트를 매핑시켜야함!

CMD [실행할 명령어]
# 배열로 전달(["poetry", "add", "poetry"])
# 이미지를 기반으로 컨테이너가 시작될때 실행

```

Dockerfile에 이름을 붙이고 싶을 경우
```bash
Dockerfile => name.Dockerfile
$ docker build -f name.Dockerfile -t [image name] [Dockerfile 위치]
```

docker start로 컨테이너 정지 후 다시 실행할 경우

dettached 모드가 디폴트
콘솔에 아무것도 표시되지 않음
다른 작업을 할 수 있음

docker run으로 컨테이너 생성 후 실행할 경우

attached 모드가 디폴트
콘솔(터미널)에 표시됨

