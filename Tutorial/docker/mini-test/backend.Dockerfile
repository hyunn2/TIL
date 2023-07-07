FROM python:3.10

LABEL maintainer="<nahkim@huray.net>"

ENV POETRY_VERSION=1.5.1

ENV POETRY_HOME=/etc/poetry

ENV PATH=/etc/poetry/bin:$PATH

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /src

COPY ./backend-tutorial ./

RUN poetry install --no-root

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]