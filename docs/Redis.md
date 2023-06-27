# Redis(REmote Dictionary Server)

키-값 기반의 인메모리 데이터 저장소

<br>

**사용하는 이유**

데이터 I/O 성능을 극대화하기 위해 사용

<br>

## 사용 방법

<br>

방법1

local에 설치

homebrew로 설치 및 실행

```bash
# redis 설치
brew install redis

# 서버 실행
redis-server

# 클라이언트 접속
poetry add redis
poetry run redis-cli
```

poetry에 redis 패키지는 redis client이다.(redis-py) 이름이 redis이다.

접속후 ping을 보내면 PONG이 온다.


<br>

---

<br>

방법2

git에서 받아서 make로 build하여 설치 및 실행

```bash
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

```bash
docker pull redis


# [둘 중 하나 선택]
# 기본 시작하기
docker run -p 6379:6379 redis
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

```bash
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

Redis는 싱글 스레드이기 때문에 시간이 오래 걸리는 Redis 명령은 하면 안된다

<br>

**배포된 redis 서버에서 하지 말아야할 것**

- 서버에서 keys 명령어를 사용하지 않아야함

keys의 경우 한번에 모든 key들을 가져오는데 key가 많을 수록 처리 시간이 많이 소요되며, 그동안 다른 명령을 처리하지 못한다.

반면, scan의 경우 한번에 특정 갯수씩 조회하고 명령어를 수행하는 동안 다른 명령을 처리할 수 있다.

대신 scan이나 sets을 사용을 하는 것을 추천

|명령어|KEYS|SCAN|
|---|---|---|
|시간 복잡도|O(N)|모든 호출은 O(1), 전체 순회의 경우 O(N)|
|특징|한번에 모든 key들을 가져옴|한번에 key의 특정 갯수들을 가져옴|
||처리하는 동안 다른 명령어를 처리 불가능|처리하는 동안 다른 명령어 처리 가능|



<br>


**복제**

장애 발생시 빠른 서버 교체나 장비 교체를 할수 있다.

<br>

---

<br>

redis 자료구조 종류
- Strings (가장 기본 자료구조)
- Lists
- Sets
- Hashes
- Sorted sets
- stream
등등이 있다.

<br>

---

<br>

## Redis CLI 명령어

<br>

소문자를 사용해도, 대문자를 사용해도 상관이 없으나 대문자를 사용한다.

- KEYS

해당 키를 보는 명령어
```bash
KEYS []
```

<br>

- EXISTS

해당 키가 존재하는지 확인
```bash
EXISTS [key]
```
key에 *를 넣으면 전체 key를 확인 할 수 있음

<br>

---

<br>

## Strings 명령어

<br>

- SET

key, value 데이터 저장
```bash
SET [key] [value]
```
<br>


- GET

해당 key의 value를 보는 명령어
```bash
GET [key 이름]
```
<br>

- MGET
여러개의 key의 value를 확인하는 명령어
```bash
MGET <key> [key ...]
```

<br>

- DEL
```bash
DEL [key]
```
<br>

- EXPIRE

생성된 key의 만료시간 설정
```bash
EXPIRE [key] [만료 시간]
```

<br>


- TTL

time to live
```bash
TTL [key]
```
-1 일 경우 영속성을 지님

-2 일 경우 만료됨

<br>

- QUIT
```bash
QUIT
```
터미널 종료

<br>

---

<br>

## LISTS 명령어

<br>

- LPUSH

왼쪽에 있는 첫번째 시작부분에 저장

```bash
LPUSH <key> <value>
```

<br>

- RPUSH
오른쪽에 마지막 끝부분에 저장

```bash
RPUSH <key> <value>
```


<br>

- LPOP

맨 첫번째 값 삭제

```bash
LPOP <key> [count]
```

<br>

- RPOP

마지막 값 삭제

```bash
RPOP <key> [count]
```

<br>

- LLEN

키의 갯수

```bash
LLEN <key>
```


<br>

- LMOVE
값 이동

```bash
LMOVE source destination <LEFT | RIGHT> <LEFT | RIGHT>
```
source 부분의 맨<왼쪽 | 오른>쪽에 있는 key를 destination의 맨<오른쪽 | 왼쪽>으로 이동시킴


<br>

- LTRIM
목록 자르기

```bash
LTRIM key start stop
```
start ~ stop 구간의 있는 값을 자른다.

<br>

- LRANGE

LPUSH를 할 경우 GET 명령어로 확인할 수 없다.
LRANGE 명령어를 통해 함수의 범위를 지정해줘야한다.
```bash
LRANGE <key> <start> <end>
```
0 : 처음 값

1 : 그다음 값

-1: 마지막값

-2: 마지막에서 두번째값


<br>


<br>

---


## SETS 명령어

<br>

모든 항목 접두사에 S를 붙이면 된다.

<br>

- SETEX

생성하면서 만료 시간 정하기
```bash
SETEX <key> <만료 시간> <value>
```
<br>

- SADD
key를 저장하며 key가 존재하지 않는다면, 새로운 set을 만든다.
```bash
SADD key member [member ...]
``` 

<br>

- SMEMBERS
set에 있는 모든 값을 반환
```bash
SMEMBERS key
```

<br>

- SREM

지정된 값 삭제
```bash
SREM <지우고 싶은 집합이름> <지우고 싶은 값>
```

<br>

- SINTER
공통된 값 반환
```bash
SINTER key [key ...]
```

<br>

- SCARD
특정 집합의 카디널리티 반환
```bash
SCARD key
```

<br>

---

## HASH 명령어

<br>

- HSET
```bash
HSET <집합> <key> <value>
```
<br>


- HGET
```bash
HGET <집합> <key> <value>
```

<br>

- HMGET
주어진 필드의 맞는 모든 value값 반환
```bash
HMGET key field [field ...]
```

<br>

- HGETALL
모든것 가지고 오기
```bash
HGETALL <key>
```

<br>

- HDEL
hash에 저장된 키값의 필드 삭제
```bash
HDEL <key> <field>
```

<br>

- HEXISTS
```bash
HEXISTS <key> <field>
```

<br>

- HINCRBY
해시에 저장된 숫자를 주어진 숫자(increment)로 증가시킴
```bash
HINCRBY key field increment
```


<br>

---

<br>

## Sorted Sets 명령어

중복이 없으며 정렬이 되어있다.


- ZADD
값을 추가하되 이미 있는 key라면 value를 수정한다.
```bash
ZADD key [NX | XX] [GT | LT] [CH] [INCR] score member [score member ...]
```

- ZRANGE
지정된 범위의 key의 value를 반환
```bash
ZRANGE key start stop [BYSCORE | BYLEX] [REV] [LIMIT offset count] [WITHSCORES]
```

- ZRANK
값이 작은 value를 가지고 있는 순으로 순위를 반환
```bash
ZRANK key member [WITHSCORE]
```

- ZREVRANK
값이 큰 value를 가지고 있는 순으로 순위를 반환
```bash
ZREVRANK key member [WITHSCORE]
```


<br>

---

<br>

## Database 관련 명령어

<br>

- SELECT

데이터베이스를 선택하는 명령어

Database가 여러 개일 경우 db를 선택하여 처리하는것

연결시에는 항상 데이터베이스 0을 사용한다(default)

```bash
SELECT [index]
```

<br>

- BGSAVE
백그라운드에서 DB 저장
일반적으로 성공시 OK 반환
Redis fork와 부모 프로세스는 클라이언트에 서비스를 제공하고 자식 프로세스는 디스크에 DB를 저장 후 종료

```bash
BGSAVE [SCHEDULE]
```

<br>

- DBSIZE
DB의 현재 키의 갯수

```bash
DBSIZE
```

<br>


- FLUSHALL
DB의 모든 항목을 삭제
```bash
FLUSHALL [ASYNC | SYNC]
```

<br>

- FLUSHDB
현재 선택된 DB의 모든 키를 삭제
```bash
FLUSHDB [ASYNC | SYNC]
```

<br>

- MOVE
현재 선택된 DB로 key를 이동시킨다.
```bash
MOVE [key] [db]
```

<br>

- RANDOMKEY
현재 선택된 DB의 랜덤한 key를 생성한다.
```bash
RANDOMKEY
```

<br>

- SAVE
RDB 파일 형식으로 동기식 저장을 수행
```bash
SAVE
```

<br>

- SCAN
현재 DB에 있는 key값을 특정 갯수를 출력
cursor에 0을 넣고 그다음 값이 출력되는데 그 값을 넣으면 그다음 key들이 나온다.
```bash
SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]
```

<br>


- SHUTDOWN
```bash
SHUTDOWN [NOSAVE | SAVE] [NOW] [FORCE] [ABORT]
```

<br>

- SWAPDB

두 개의 DB를 바꾼다.
```bash
SWAPDB [index1] [index2]
```


<br>

# 코드에서 사용하기

redis를 터미널에서 사용하기 위해 사용할 명령어

```bash
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

  

reids.conf 권장 설정
1. Maxclient 값을 충분히 높히기
2. RDB/AOP 설정 비활성화
3. 부하가 심한 커맨드 비활성화 ex)KEYS
rename-command CONFIG ""
