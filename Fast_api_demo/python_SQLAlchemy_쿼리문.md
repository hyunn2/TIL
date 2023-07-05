# python + SQLAlchemy 쿼리문

```
from database import SessionLocal
db = SessionLocal()

[내가 수행할 쿼리문]

db.commit()
```
commit을 해야 반영이 됨!

## 수행할 쿼리문

데이터 전체 확인
```
from models import [모델 이름]
db.query([모델 이름]).all()
```

특정 데이터 확인
```
db.query([모델 이름]).filter([조건문])
```

데이터 삽입
```
q = [모델 이름]([모델 필드]=' 입력 하기 ', [모델 필드]=' 입력 하기 ')

db.add(q)
db.commit()
```

데이터 전체 삭제
```
db.query([모델 이름]).delete()
db.commit()
```