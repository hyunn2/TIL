import pytest
import uuid

# @pytest.fixture(scope="function")
# def scope_default():
#     username = uuid.uuid4().hex[:4]
#     return username

# @pytest.fixture(scope="class")
# def scope_class():
#     username = uuid.uuid4().hex[:4]
#     return username

# @pytest.fixture(scope="module")
# def scope_module():
#     username = uuid.uuid4().hex[:4]
#     return username

# @pytest.fixture(scope="package")
# def scope_package():
#     username = uuid.uuid4().hex[:4]
#     return username

# @pytest.fixture(scope="session")
# def scope_session():
#     username = uuid.uuid4().hex[:4]
#     return username



def make1(scope_default):
    assert print("default :" ,scope_default)

def make2(scope_class):
    print("default :" ,scope_class)

def make3(scope_module):
    print("module :" ,scope_module)

def make4(scope_package):
    print("package :" ,scope_package)

def make5(scope_session):
    print("session :" ,scope_session)