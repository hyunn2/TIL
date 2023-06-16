# uvicorn vs gunicorn

Uvicorn
ASGI 프로토콜을 지원하는 앱 서버
single process

Gunicorn
WSGI 표준을 지원하는 애플리케이션 서버
WSGI HTTP 서버

Fast API는 최신 ASGI 버전을 사용하기때문에 Gunicorn은 자체적으로 호환되지 않음

