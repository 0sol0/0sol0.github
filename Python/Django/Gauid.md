## Web FramWork
웹을 편하게 만들 수 있는 기계

- 인증 : 로그인/로그아웃
- 데이터 저장 : 대이터베이스 관리
- 요청에 대한 응답 : HTML, JSON
- 보안기능
코드의 재 사용성
...

사용법이 익히는 것이 첫번째(주니어)<br>
내부 구조를 들여다보는 것이 두번째(시니어)<br>

## Django
Python을 기반으로 만들어진 Web Frameworke
Flask? Django?

| 구분 | Flask | Django|
|---|---|---|
1 | 단순한 기계 | 복잡한 기계
2 | 제공기능 적음 | 제공기능 많음
3 | 사용법 단순 | 사용법 복잡
4 | 배우기 쉬움 | 실무
5 | test용 web | web service
6 |             | admin panel 관리자 페이지
7 | web Framework
8 |             | Database
9 | perfomance
10 |            | Security
11 | Fiexbillity |
12 |            | Usage & community : 사용자가 더 맣다.
13 | Template Engine : HTML 내에서 Python처럼 변수, if문, for문을 사용 가능
14 |            | Reusable Components : 코드 재사용성
---

### Django의 큰 그림
모든 Python 파일을 하나하나 분석할 필요없다
중요한 건 파일간의 티키타카
- 파일간에 어떤 데이터를 주고 받는지
- 그 과정에서 각 파일들은 어떤 역할을 하는지

ex)
MVC, MTV(Model Views Template) pettern : <br>
클라이언트 요청 /url <-> urls.py[path(/url, url관련된 함수)] <-> view.py[hello 함수 = (hellow.html)] <-> db.sqlite(회원이름)
- view.py는 분석하는 것이 좋음

### 중요
- 데이터 관리
    - 객체 관리(ORM) = class
- 인증 : 지금 접속한 클라이언트의 정보를 다루는 것
    - 회원 가입
    - 회원 탈퇴
    - 로그인/로그아웃
    - 회원 정보 수정
- 요청에 대한 응답을 하기까지
    - Request 가공
    - Response 가공
- +베포

## 가상환경 = 통
- PIP : 패키지 관리자(설치, 제거, 조회 등)
- Pakage : 외부기능을 제공해주는 설치의 대상
- Module : 다른 파일에 있는 코드뭉치
- Library : 미리 만들어 둔 코드
- FrameWork : 어떤 목적을 위해서 미리 만들어 둔 코드

pakage를 설치하면 컴퓨터 전체에 영향을 미치는데,
가상환경 안에 pakage를 설치하면 가상환경 안에서만 영향을 미친다.<br>
가상환경 밖에선 pakage를 쓸 수 없다.
가상환경을 켠 상태에서 

### 가상환경 만들기
가상환경 만들기<br>
`$ python -m venv <가상환경 이름>`<br>
가상환경 켜기<br>
`$ source myvenv/scripts/actuvate`<br>
가상환경 끄기<br>
`$ deactivate`<br>

패키지 설치<br>
`$ pip install`<br>
패키지 제거<br>
`$ pip uninstall`<br>
설치된 패키지 이름 및 버전 조회<br>
`$ pip freeze`<br>
설치된 패키지 목록을 requirements.txt로 내보내기<br>
`$ pip freeze >> requirements.txt`<br>
requirements.txt 안에 적힌 파일 설치하기<br>
`$ pip install -r ./requirements.txt`<br>
