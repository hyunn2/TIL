from fastapi.testclient import TestClient

import pytest
import uuid


@pytest.fixture(scope="function")
def scope_default():
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="class")
def scope_class():
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="module")
def scope_module():
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="package")
def scope_package():
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="session")
def scope_session():
    username = uuid.uuid4().hex[:4]
    return username