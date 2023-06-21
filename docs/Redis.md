# Redis(REmote Dictionary Server)

키-값 기반의 인메모리 데이터 저장소

**사용하는 이유**

데이터 I/O 성능을 극대화하기 위해 사용

<br>

**사용 방법**

방법1

local에 설치

homebrew로 설치 및 실행

```
# redis 설치
brew install redis

# 서버 실행
redis-server

# 클라이언트 접속
poetry add redis
poetry run redis-cli
```

poetry에 redis 패키지는 redis client이다. 이름이 redis이다.

접속후 ping을 보내면 PONG이 온다.


<br>

---

<br>

방법2

git에서 받아서 make로 build하여 설치 및 실행
```
git clone https://github.com/redis/redis

make

cd src

./redis-server

./redis-cli
```

<br>

---

<br>

방법3

docker에서 image pull 받아서 설치 및 실행
```
docker pull redis


# 디스크에 데이터 쓰는걸로 시작하기
docker run --name some-redis -d redis redis-server --save 60 1 --loglevel warning

docker exec -it [컨테이너 아이디나 이름] /bin/bash

root@[컨테이너 아이디]:/data# redis-cli
127.0.0.1:6379> [여기서 명령어 사용]
```

--name: 컨테이너 이름 설정

-d: 컨테이너가 백그라운드로 실행

--save: 1개의 쓰기 작업이 수행되면 60초마다 DB의 스냅샷을 저장

--loglevel: 로그를 어디까지 보여줄지 선택하는 옵션



<br>

## 특징
- Key-Value 형태의 데이터 저장소
- 컬렉션 지원(List, Hash, Set, Sorted set)
- Publish/Subscribe 지원
- 디스크 저장(Persistent Layer)
- 복제(master/slave replication)
- 빠른 속도

<br>

**Key-Valuse 형태**

```
set id:username "username"

get id:username
```

<br>

**컬렉션 지원**

보통 컬렉션은 하나의 서버 내부에서 동작하지만 레디스의 경우 분산 서버 환경에서 처리 가능하다.

데이터 종류
- Strings
- Hashs
- Lists
- Sets
- Sorted Sets
- Bitmaps
- HyperLogLogs(HLL)

<br>

**pub/sub 지원**

서버간 통지시 필요하기도 하며, 특정한 주제에 대해 구독한 사람 모두에게 메세지를 발행하는 통신 방법
주로 채팅 기능이나 푸시 알림등에 사용한다


<br>

**디스크 저장**

현재의 메모리 상태를 디스크에 저장 가능
서버가 장애를 일으켜 문제가 발생해도 디스크에 저장된 데이터를 기반으로 다시 복구 가능하다.

RDB와 AOF로 2가지의 백업 옵션 종류가 있다.
- RDB

현재 메모리에 대한 덤프를 생성하는 기능

모든 작업을 멈추고 현재 메모리 상태에 대한 RDB 파일을 생성하는 것과, fork를 통해 자식 프로세스에서 RDB 파일을 저장하는 것이 있음

fork를 사용하여 RDB 파일을 저장하는 것은 메모리를 두배로 사용한다.

fork의 경우 부모 프로세스로부터 자식프로세스에 복사를 하게 되어 메모리 부족이 발생할 수 있다.

<br>

- AOF(Append Only File)

장애가 발생할 경우 AOF를 기반으로 복구한다.

<br>

**싱글 스레드**

Redis는 싱글 스레디이기 때문에 시간이 오래 걸리는 Redis 명령은 하면 안된다

<br>

**redis 서버에서 하지 말아야할 것들**

- 서버에서 keys 명령어를 사용하지 않아야함
- flushdb

<br>

**복제**

장애 발생시 빠른 서버 교체나 장비 교체를 할수 있다.

<br>

**Redis CLI 명령어**

소문자를 사용해도, 대문자를 사용해도 상관이 없으나 대문자를 사용한다.

- KEYS

해당 키를 보는 명령어
```
KEYS []
```
<br>

- SELECT

<br>

- EXISTS

해당 키가 존재하는지 확인
```
EXISTS [key]
```
key에 *를 넣으면 전체 key를 확인 할 수 있음
<br>

- set

key, value 데이터 저장
```
SET [key] [value]
```
<br>

- GET

해당 key의 value를 보는 명령어
```
GET [key 이름]
```
<br>

- DEL
```
DEL [key]
```
<br>

- EXPIRE

생성된 key의 만료시간 설정
```
EXPIRE [key] [만료 시간]
```
<br>

- SETEX

생성하면서 만료 시간 정하기
```
SETEX [key] [만료 시간] [value]
```
<br>

- TTL

time to live
```
TTL [key]
```
-1 일 경우 영속성을 지님

-2 일 경우 만료됨

<br>

**LIST**

<br>

- RPUSH
오른쪽에 마지막 끝부분에 저장
```
RPUSH [key] [value]
```

- LPUSH

왼쪽에 있는 첫번째 시작부분에 저장
```
LPUSH [key] [value]
```

- LRANGE
LPUSH를 할 경우 GET 명령어로 확인할 수 없다.
LRANGE 명령어를 통해 함수의 범위를 지정해줘야한다.
```
LRANGE [key] [start] [end]
```
0 : 처음 값
1 : 그다음 값
-1: 마지막값
-2: 마지막에서 두번째값

<br>

- RPOP

마지막 값 삭제
```
```

- LPOP

맨 첫번째 값 삭제
```
```

<br>


**SET**

모든 항목 접두사에 S를 붙이면 된다.

<br>

- SADD

<br>

- SMEMBERS

<br>

- SREM
```
SREM [지우고 싶은 집합이름] [지우고 싶은 값]
```

**HASH**

- HSET
```
HSET [집합] [key] [value 값]
```
<br>


- HGET
```
HGET [집합] [key] [value]
```

<br>

- HGETALL
모든것 가지고 오기
```
HGETALL [집합이름]
```

<br>

- HDEL

<br>

- HEXISTS
```
```



- FLUSHALL

데이터베이스의 모든 항목을 제거


- quit
```
QUIT
```
터미널 종료


<br>

# 코드에서 사용하기

redis를 터미널에서 사용하기 위해 사용할 명령어
```
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set('foo', 'bar) 
r.get('foo')

```

<br>

## 데이터 관리

<br>

**캐싱 전략**

- Cache Aside
- Read Through
- Write Back
쓰기 작업이 많아서 INSERT 쿼리를 하나만 날리지 않고 한번에 배치처리를 함

- Write Through

<br>

**redis의 모드 3가지**

| Standalone | Sentinel | Cluster |


<br>
