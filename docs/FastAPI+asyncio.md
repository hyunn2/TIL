# Fast API + asyncio
동시성과 async / await


## 요약
서드파티의 라이브러리를 사용하는 경우엔 `await`를 사용하며, 함수에는 비동기 함수임을 선언해야한다. 코루틴 안에서 다른 코루틴을 실행할 경우 `await`을 무조건 붙여줘야한다!
ex)
```
results = await some_library()
```
```
@app.get('/')
async def read_results():
  results = await some_library()
  return results
```

만약 DB나 API, 파일 시스템 등과 같은 것들과 커뮤니케이션할 경우에는 `await`을 지원하지 않기 때문에 `def`만 써줘야한다.
ex)
```
@app.get('/')
async def read_results():
  results = await some_library()
  return results
```

def와 async def를 섞어서 사용할 수 있다.


## Asynchronous(비동기 코드)

동시성과 병렬성

I/O binding

## async 와 await

## Coroutines(코루틴)


참고 : [Fast API async](https://fastapi.tiangolo.com/async/)