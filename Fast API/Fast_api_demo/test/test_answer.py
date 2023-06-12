from .fixtures import *

def test_read_main_case1(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" : "Hello World"}


##### Answer #####
# def test_answer_create():

# def test_answer_update():

# def test_answer_delete():