# Redis-namespace

redis namespace를 사용하기 위해선 ":"(콜론)을 사용하여 구분한다.


### python에서 사용하는 방법

```
poetry add redis-namespace
```

```python
import redis
from redis_namespace import StrictRedis

redis_connection = redis.StrictRedis()
namespaced_redis = StrictRedis(namespace='ns:')
namespaced_redis.set('foo', 'bar')  # redis_connection.set('ns:foo', 'bar')

namespaced_redis.get('foo')
redis_connection.get('ns:foo')

namespaced_redis.delete('foo')
namespaced_redis.get('foo')
redis_connection.get('ns:foo')
```

만약 내가 username과 cnt를 저장하고 싶다면?
```python
import redis
from redis_namespace import StrictRedis

r = redis.StrictRedis()

```