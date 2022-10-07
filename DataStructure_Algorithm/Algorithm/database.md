기획 특강
기획 = 설계
화면 설계 - 와이어프레임(Figma)
- UI/UX의  기초
- 프로토타입
- 중요한 건 정보의 흐름!!!

DB 설계 - ER 다이어그램(draw.io)
- models.py안에 class들의 관계 =데이터들 간의 관계 & 각 컬럼의 의미
- Database란?
데이터를 저장하는 거대한 통

- RDBMS(관계형 데이터베이스)란?
DBMS = 데이터를 관리할 수 있는 프로그램(MySQL, SQLite ...)
데이터 베이스 안에 있는 데이터를 표처럼 관리하는 시스템
표 = Table
SQL = 데이터베이스 접근, 조작 언어
ORM = 클래스를 바탕으로 내부적으로 SQL언어로 바꿔주는 것

- Primary Key(PK)란?
    - 가장 중요한 데이터
    - 나머지 데이터를 특정지을 수 있는 데이터
    - 고유한 값, 변경되면 안된다
    - 비어있는 값이면 안된다('Null=True')

- Foreign Key(외래키)란?
    - 다른 Table과 연결지을 수 있는 데이터
    - 다른 Table에 있는 데이터를 가져와 쓸 수 있다
    - 다른 Table에 있는 데이터를 참조하는 Table
    - 참조하는 Table의 변경될 때(on_delete=CASEBASE, on_defult='' 등)

- One To One To 관계?
하나의 A는 하나의 B로 구성되어 있다
- One To Many 관계?
하나의 A는 하나 이상의 B로 구성되어 있다
- Many To Many 관계?
- PK, FK, 관계는 꼭 쓰기

API 설계 - API 명세서 (swagger) = djEjgrp eodlxj wnrhqkesmswl
    user -> urls.py -> views.py -> mdoles.py -> admin.py(database) -> views.py -> urls.py -> tamplates
    urls.py -> viws.py -> models.py -> admin.py(database) -> Json
    - Backend와 Frontend를 따로 개발할 때 ; Django(Backend) -> Frontend(ex. rpeact)

(+ 협업 다시보기 pullrequest)
    - 내가 소유하지 않은 원격 저장소에 push할 수 없어서
    - 작업한 'brach'를 push해야 한다
    - `git push origin branch`
순서
`git clone 'url'` or `git pull`
`git branch`
`cd '폴더 이름'`
`git branch '브랜치 이름'`
`git checkout '브랜치 이름'`
`git add '파일 이름'`
`git commit -m '메세지'`
`git puch origin mybranch`

![git](https://blog.kakaocdn.net/dn/o6KFg/btq1Kcy0tAh/6e9TdpCc1k4JY1ViAucOo1/img.png)