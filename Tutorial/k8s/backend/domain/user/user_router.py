from datetime import timedelta, datetime

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status
from Redis.user_login import register_login_check_user, check_black_user, check_login_cnt, check_login_list, increase_cnt, delete_login_list

from database import get_db
from domain.user import user_crud, user_schema
from domain.user.user_crud import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
# openssl rand -hex 32
SECRET_KEY = 'secretkey'
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

router = APIRouter(
    prefix="/api/user",
    tags=["User"],
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    """회원가입"""
    user = await user_crud.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    user_crud.create_user(db=db, user_create=_user_create)

@router.post("/login", response_model=user_schema.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    """로그인"""
    # 유저 비밀번호 확인
    user = await user_crud.get_user(db, form_data.username)

    if check_black_user(form_data.username) == True:
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail="Unable to log in because it keeps trying to log in",
            # headers={"WWWW-Authenticate": "Bearer"}
        )
    
    # 유저가 존재하지 않거나 비밀번호가 맞지 않을 경우
    if not user or not pwd_context.verify(form_data.password, user.password):
        if user:
            if check_login_list(user.username):
                increase_cnt(user.username)
                check_login_cnt(form_data.username)
            else:
                register_login_check_user(user.username)

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWWW-Authenticate": "Bearer"}
        )
    
    # 로그인 성공시 초기화
    delete_login_list(user.username)
    
    # access token 만들기
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }
    
def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    """헤더 정보의 토큰을 읽어 사용자 객체를 리턴"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = user_crud.get_user(db, username=username)
        if user is None:
            raise credentials_exception
        return user
    
# 회원 탈퇴 
# @router.delete("/delete", status_code=status.HTTP_200_OK)
# def user_delete():