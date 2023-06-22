import redis

r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
connection = r.ping()
print(connection)

r.set('foo', 'bar')

r.get('foo')

r.hset("user-session:123", mapping={
    "name": 'John',
    "surname": 'Smith',
    "company": "Redis",
    "age": 29
})

r.hgetall('user-session:123')
