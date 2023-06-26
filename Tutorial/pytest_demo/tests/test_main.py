
def inc(x):
    return x + 1


def test_inc_function(scope_default):
    print("default :" ,scope_default)
    assert inc(1) == 2

def test_inc_class(scope_class):
    print("default :" ,scope_class)
    assert inc(1) == 2

def test_inc_module(scope_module):
    print("module :" ,scope_module)
    assert inc(1) == 2

def test_inc_package(scope_package):
    print("package :" ,scope_package)
    assert inc(1) == 2

def test_inc_session(scope_session):
    print("session :" ,scope_session)
    assert inc(1) == 2