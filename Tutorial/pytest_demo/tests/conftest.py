import pytest
import uuid


@pytest.fixture(scope="function")
def scope_default():
    print("Start function")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="class")
def scope_class():
    print("Start class")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="module")
def scope_module():
    print("Start module")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="package")
def scope_package():
    print("Start package")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="session")
def scope_session():
    print("Start session")
    username = uuid.uuid4().hex[:4]
    return username