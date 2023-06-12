from fastapi.testclient import TestClient

import pytest

from app.main import app

@pytest.fixture
def client():
    """Fast API 클라이언트 인스턴스"""
    return TestClient(app)

@pytest.fixture
def user1():
    username = "nahkim"
    return username

@pytest.fixture
def user2():
    username = "test1"
    return username

@pytest.fixture
def user3():
    username = "test2"
    return username

@pytest.fixture
def question1():
    id = 1
    subject = "test_question1"
    content = "test_question1"

    return 

@pytest.fixture
def answer1():
    id = 1
    content = "test_answer1"
