# 만든 방법
1. 
```
poetry new Fast_api_demo
```

2. 패키지 설치

```
poetry add fastapi uvicorn
```

3. main.py 작성

```
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int,
              q: Union[str, None] = None):
    return {"item_id" : item_id, "q": q}
```


4. 서버 실행

```
poetry run uvicorn main:app --reload
```

