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
    except WebSocketDisconnect:
        await websocket.close()
