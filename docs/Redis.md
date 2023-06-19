# Redis

대용량 데이터 처리 관련
- NoSQL
- Cache
- Redis
- Memcache
- Sharding


## 특징
- Key-Value 형태의 데이터 저장소
- 컬렉션 지원(List, Hash, Set, Sorted set)
- Publish/Subcrin 지원
- 디스크 저장(Persistent Layer)
- 복제(master/slave replication)
- 빠른 속도

**Key-Valuse 형태**

```
set id:username "username"

get id:username
```

**컬렉션 지원**
보통 컬렉션은 하나의 서버 내부에서 동작하지만 레디스의 경우 분산 서버 환경에서 처리 가능하다.

**pub/sub 지원**
서버간 통지시 필요

**디스크 저장**
현재의 메모리 상태를 디스크에 저장 가능
서버가 장애를 일으켜 문제가 발생해도 디스크에 저장된 데이터를 기반으로 다시 복구 가능하다.
- RDB
현대 메모리에 대한 덤프를 생성하는 기능
모든 작업을 멈추고 현재 메모리 상태에 대한 RDB 파일을 생성하는 것과, fork를 통해 자식 프로세스에서 RDB 파일을 저장하는 것이 있음


- AOF(Append Only File)
장애가 발생할 경우 AOF를 기반으로 복구한다.



**싱글 스레드**
Redis는 싱글 스레디이기 때문에 시간이 오래 걸리는 Redis 명령은

redis에서 하지 말아야할 것들
- 서버에서 keys 명령어를 사용하지 않아야함
- flushall/flushdb


**복제**
장애 발생시 빠른 서버 교체나 장비 교체를 할수 있다.