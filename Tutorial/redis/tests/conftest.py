from fastapi.testclient import TestClient

import pytest
import uuid

from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def user1():
    username = "nahkim"
    return username

