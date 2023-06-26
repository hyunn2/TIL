import pytest
import uuid


@pytest.fixture(scope="function")
def scope_default():
    print("End function")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="class")
def scope_class():
    print("End class")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="module")
def scope_module():
    print("End module")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="package")
def scope_package():
    print("End package")
    username = uuid.uuid4().hex[:4]
    return username

@pytest.fixture(scope="session")
def scope_session():
    print("End session")
    username = uuid.uuid4().hex[:4]
    return username


def inc(x):
    return x + 1


def test_inc_function(scope_default):
    print("====================== default ===========================")
    print("default :" ,scope_default)
    assert inc(1) == 2
    print()

def test_inc_function1(scope_default):
    print("====================== default1 ===========================")
    print("default :" ,scope_default)
    assert inc(1) == 2
    print()


def test_inc_class(scope_class):
    print("====================== class ===========================")
    print("default :" ,scope_class)
    assert inc(1) == 2
    print()

def test_inc_class1(scope_class):
    print("====================== class1 ===========================")
    print("default :" ,scope_class)
    assert inc(1) == 2
    print()

def test_inc_module(scope_module):
    print("====================== module ===========================")
    print("module :" ,scope_module)
    assert inc(1) == 2
    print()

def test_inc_module1(scope_module):
    print("====================== module1 ===========================")
    print("module :" ,scope_module)
    assert inc(1) == 2
    print()

def test_inc_package(scope_package):
    print("====================== package ===========================")
    print("package :" ,scope_package)
    assert inc(1) == 2
    print()

def test_inc_package1(scope_package):
    print("====================== package1 ===========================")
    print("package :" ,scope_package)
    assert inc(1) == 2
    print()


def test_inc_session(scope_session):
    print("====================== session ===========================")
    print("session :" ,scope_session)
    assert inc(1) == 2
    print()

def test_inc_session1(scope_session):
    print("====================== session1 ===========================")
    print("session :" ,scope_session)
    assert inc(1) == 2
    print()