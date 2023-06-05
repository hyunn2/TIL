# commitizen이란?
커밋 규칙을 잡아주는 파이썬 라이브러리

## 사용 방법
git add [파일이나 폴더명]
git commit 명령어 : **cz c**
git push

## 명령어 종류
- Init
- Commit
- Bump
- Check
- Changelog

## 커밋시 나오는 메세지(commit command)
```
<타입>[적용 범위(선택 사항)]: <설명>
[본문(선택 사항)]
[꼬리말(선택 사항)]
```

1. 커밋 타입
  build: 빌드 시스템 또는 외부 종속성에 영향을 미치는 변경 사항
  ci: CI 구성 파일 및 스크립트에 대한 변경 사항
  docs: 문서가 변경되었을 경우
  feat: 새로운 기능
  fix: 버그 수정
  perf: 성능 향상 코드로 변경
  refactor: 버그를 수정하거나 기능을 추가하지 않는 코드 변경(폴더명 바꾸기 및 삭제)
  test: 누락된 테스트 추가 및 기존 테스트 수정

2. 변경된 파일의 스코프(git add한 것을 쓰면 자동으로 괄호 안에 파일을 넣어줌 위에선 적용 범위 부분을 뜻함)
3. 커밋 제목(설명 부분)
4. 커밋 메세지(본문 부분)
5. BREAKING CHANCE (API가 크게 변경할 경우)
6. footer (꼬리말)



참고 : 
[commitizen Docs](https://commitizen-tools.github.io/commitizen/)
[Conventional Commits](https://www.conventionalcommits.org/ko/v1.0.0-beta.4/#breaking-change%EC%97%90-%EC%A3%BC%EC%9D%98%EB%A5%BC-%EC%A3%BC%EA%B8%B0-%EC%9C%84%ED%95%B4-%EC%98%B5%EC%85%98%EC%9D%B8-%EB%A5%BC-%ED%8F%AC%ED%95%A8%ED%95%9C-%EC%BB%A4%EB%B0%8B-%EB%A9%94%EC%84%B8%EC%A7%80)
