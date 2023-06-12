from .fixtures import *

def test_read_main_case1(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" : "Hello World"}


##### Question #####

# 질문 리스트
# 완료
# def test_question_list():

# 질문 상세
# 완료
# def test_question_detail():

# 질문 상세
# 유효하지 않는 question_id 일 경우
# def test_question_detail():

# 질문 생성
# 완료
# def test_question_create():

# 질문 생성
# 주어진 파라미터가 빈값인 경우
# def test_question_create():

# 질문 생성
# 로그인하지 않은 경우
# def test_question_create():

# 질문 수정
# 완료
# def test_question_update():

# 질문 수정
# 빈 값인 경우
# def test_question_update():

# 질문 수정
# 로그인하지 않은 경우
# def test_question_update():

# 질문 수정
# 질문 등록자가 아닌 경우
# def test_question_update():

# 질문 수정
# 데이터가 없는 경우
# def test_question_update():

# 질문 삭제
# 완료
# def test_question_delete():

# 질문 삭제
# 질문 등록자가 아닌 경우(권한이 없는 경우)
# def test_question_delete():

# 질문 삭제
# 데이터가 없는 경우
# def test_question_delete():
