# URL 단축 서비스

## 개요
긴 URL을 짧게 단축하여 사용하고, 단축된 URL을 통해 원본 URL로 리디렉션하는 기능을 제공

## 구현
**구현된 기능**
  - 단축 URL 생성
  - 원본 URL 리디렉션
  - URL 키 만료 기능
    - 키 삭제는 하지 않고, 만료 시킴. -> 로그성으로 남기고 나중에 분석 시 사용
  - 통계 기능
    - 몇 번 리디렉션 되었는지 횟수 알려줌.
    - 브라우저 캐싱 때문에 같은 url을 여러번 호출하면 카운트 안 될 수 있음 (아예 서버로 요청이 안 옴)
  - 데이터베이스: 원본 URL과 단축 키 매핑을 저장하기 위한 데이터베이스 사용.

## 개발 환경
- 언어: Python (Anaconda)
- 프레임워크: FastAPI
- 데이터베이스: SQLite



## 실행 방법

### 이동
```zsh
cd url_shortener
```

### docker 이미지 빌드
```zsh
docker build -t url-shortener .
```

### docker 이미지 실행
```zsh
docker run -p 9999:9999 url-shortener
```