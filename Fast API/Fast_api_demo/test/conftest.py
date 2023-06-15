# from database import SessionLocal
# from models import User, Question, Answer
from fastapi.testclient import TestClient

import pytest
import uuid

from app.main import app

id_cnt = 0

# @pytest.fixture(autouse=False)
# def db():
#     yield None
#     db = SessionLocal()
#     db.query(User).delete()
#     db.query(Question).delete()
#     db.query(Answer).delete()

@pytest.fixture
def client():
    """Fast API 클라이언트 인스턴스"""
    return TestClient(app)

@pytest.fixture
def user1():
    username = uuid.uuid4().hex[:6]
    return username

@pytest.fixture
def user2():
    username = uuid.uuid4().hex[:6]
    return username

@pytest.fixture
def user3():
    username = uuid.uuid4().hex[:6]
    return username

@pytest.fixture
def pwd1():
    pwd = uuid.uuid4().hex[:6]
    return pwd

@pytest.fixture
def pwd2():
    pwd = uuid.uuid4().hex[:6]
    return pwd

@pytest.fixture
def pwd3():
    pwd = uuid.uuid4().hex[:6]
    return pwd

@pytest.fixture
def email1():
    email = uuid.uuid4().hex[:6]
    return email

@pytest.fixture
def email2():
    email = uuid.uuid4().hex[:6]
    return email

@pytest.fixture
def email3():
    email = uuid.uuid4().hex[:6]
    return email

@pytest.fixture
def subject():
    subject = uuid.uuid4().hex[:10]
    return subject

@pytest.fixture
def subject_blank():
    subject = ''
    return subject

@pytest.fixture
def content():
    content = uuid.uuid4().hex[:15]
    return content

@pytest.fixture
def content_blank():
    content = ''
    return content

@pytest.fixture
def id_counting():
    cnt = id_cnt
    id_cnt += 1
    return cnt

# @pytest.fixture
# def question1():
#     id = 1
#     subject = uuid.uuid4().hex[:10]
#     content = uuid.uuid4().hex[:20]