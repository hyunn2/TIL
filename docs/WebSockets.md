# WebSockets

websocket이란?


<br>

## 설치 방법
```
[pip 사용하는 경우]
pip install websockets


[poetry 사용하는 경우]
poetry add websockets
```

<br>

## 웹소켓을 이용한 텍스트 주고 받기
```
from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 서버가 클라이언트의 통신 연결을 허락함
    await websocket.accept()
    try:
        # 문자열 수신을 기다림
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was : {data}")
    # 연결이 끊길 경우
    except WebSocketDisconnect:
        await websocket.close()

```
<br>

## 웹소켓 + asyncio를 이용한 비동기 처리
```
import asyncio
from datetime import datetime

from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()

async def echo_message(websocket: WebSocket):
    data = await websocket.receive_text()
    await websocket.send_text(f"Message text was: {data}")

async def send_time(websocket: WebSocket):
    await asyncio.sleep(10)
    await websocket.send_text(f"It is {datetime.utcnow().isoformat()}")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 서버가 클라이언트의 통신 연결을 허락함
    await websocket.accept()
    try:
        # 문자열 수신을 기다림
        while True:
            echo_messaget_task = asyncio.create_task(echo_message(websocket))
            send_time_task = asyncio.create_task(send_time(websocket))
            done, pending = await asyncio.wait(
                {echo_messaget_task, send_time_task},
                return_when=asyncio.FIRST_COMPLETED,
            )
            for task in pending:
                task.cancel()
            for task in done:
                task.result()
    # 연결이 끊길 경우
    except WebSocketDisconnect:
        await websocket.close()

```
