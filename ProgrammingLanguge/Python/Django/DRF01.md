## DRF
MVT 방식
- Template는 사용자가 직접 볼 수 있는 UI
- Django Template 문법을 사용
- data를 받아올 때마다 페이지가 새로고침 됨(html, css, js를 다시 새로 가져옴)
- Templates는 프론트엔드의 영역(Anguar React Vue.js 등)
- 프론트엔드와 백엔드에서 repo를 서로 따로 가지고 있음
- 그 사이에 주고 받는 것은 Ajax를 이용해서 Json data를 사용
- Templates에 주로 JavaScript를 사용
- context를 대신 다른 것을 사용한다.
- 이것을 편하게 해주는 것이 Django Rest Framework

## 웹의 흐름(네트워크)
- Request가 있으면 Response가 있다.
- HTTP(Hyper Text Transfer Protocol) : 정보를 어떤 식으로 주고, 받을 것인지에 대한 약속

- DNS(Domain Name System) : IP주소를 알지 못해도 Domain Name으로 해당 웹페이지를 찾을 수 있게 한 것
    - Domain Name = 연락처에 저장된 이름
    - IP 주소 = 전화번호 `nslookup 주소`
    - HTTP 요청 메세지 = Request-Head & Request-Body, Response-Head & Response Body

나중에 공부해야 할 부분들
```
Domin Name 검색 -> IP 주소 조회 -> HTTP 요청 메세지 작성 -> Socket 라이브러리를 통해서 전달 -> TCP/IP 작성 -> TCP/IP 안에 HTTP 메시지가 포함 -> 전달

프로트콜 계층
어플리케이션 -> Socket Library -> TCP -> IP -> LAN -> 인터넷

TCP 3 way handshake
1. 클라이언트 -> 서버 : SYN
2. 서버 -> 클라이언트 : SYN + ACK
3. 클라이언트 -> 서버 : ACK
SYN을 통해 연결, ACK을 통해 승인

UDP(User Datagram Protocol)

Port = 항구
같은 IP 내에서 프로세스 구분을 해줄 수가 있다
0~65535 있다.
0~1023은 잘 알려진 포트로 사용하지 않는게 좋다.
Port 생략 시, http = 80, https = 443

URI(Uniform Resource Identifier) : 어디에 뭐가 있는지 알려주는 명칭
Uniform : 리소스 식별을 위한 통일 방식
Resource : 리소스
Identifier : 식별자
URL(Uniform Resource Locator)
URN(Uniform Resource Name) : 거의 쓰지 않는다.
```

## HTTP(HyperText Transfer Protocol)
- HTML(HyperText Markup Language)
- HL(HyperLink)
- WWW(world wide web)

- 1997년 HTTP 1.1버전 나옴

### HTTP 특징
- 클라이언트 서버 구조
    - Request, Response 구조
    - 클라이언트는 Request를 보내고 Response를 기다리게 된다.
    - 서버 : 데이터와 비즈니스 로직
    - 클라이언트 : UI

- 무상태 프로토콜(stateless)
    - 서버가 클라이언트의 상태를 기억하지 않는다.
    - 매번 서버에게 필요한 정보를 줘야 한다.

- <-> 상태 프로토콜(stateful)
    - 서버가 클라이언트의 상태를 기억하고 있다.
    - 서버에게 매번 정보를 줄 필요가 없다.

- 비연결성
    - 요청시마다 연결을 유지하면 클라이언트가 연결을 하면 할수록 서버가 터진다.
    - 연결 유지를 하지 않으면서 최소한의 자원 사용을 할 수 있다.
    - 서버 자원을 효율적으로 쓸 수 있다.

### HTTP 메세지
- Request message
    - Request Line
    - Header
    - A Blank Line
    - Body(Optional)

- Response message
    - Status Line
    - Header
    - A Blank Line
    - Body(Optional)

### HTTP Method
안좋은 예:
- 목록 조회 `/read-member-list`
- 조회 `/read-member-by-id`
- 등록 `/create-member`
- 수정 `/update-member`
- 삭제 `/delete-member`

리소스 식별이 가장 중요하다.<br>
리소스 : 웹상에서 존재하는 것<br>
URI = 리소스<br>
Method : 리소스를 기지고 하는 행위들<br>

좋은 예:
- 목록 조회 `/members`
- 조회 `/members/{id}`
- 등록 `/members/{id}`
- 수정 `/members/{id}`
- 삭제 `/members/{id}`

Restful API : 리소스와 메소드를 분리하는 것
- 리소스 : 존재하는 것(data)
- 메소드 : 조회(GET), 등록(POST), 변경(PUT, PATCH), 삭제(Delete)

#### Method의 종류
GET : 조회
- 데이터를 쿼리스트링으로 전달
    - 쿼리스트링 : 주소창으로 데이터를 전달하는 것

HEAD : GET과 동일하지만 상태줄과 헤더만 반환<br>

POST : 등록
- 메세지 바디를 통해 서버로 요청 데이터 전달
- 데이터를 처리(DB에 상태변화가 일어난다). ex) 등록, 변경, 삭제 등
- 새로운 리소스 생성되지 않을 수 있음

PUT : 대체, 혹은 생성
- 없으면 만들고 있으면 덮어쓴다.
- 모든 데이터를 다시 다 보내줘야 한다.

PATCH : 부분번경(바꾸고 싶은 부분만 보내도 된다.)

DELETE : 삭제
- 리소스 삭제

#### 데이터 전송
쿼리 파라미터
- GET
- ex) 검색, 정렬 필터 등

메세지 바디
- POST, PUT, PATCH
- ex) 회원가입, 상품주문, 리소스 등록 변경

HTML Form을 통한 데이터 전송
- GET, POST만 지원

HTTP API를 통한 데이터 전송
- POST, PUT, PATCH
- Form대신 JS를 이용한 통신
- 서버 to 서버/앱 클라이언트/웹클라이언트(ajax)

API 설계 예시
- GET `/members` -> 목록 조회
- POST `/members` -> 등록
- GET `/members/{id}` -> 조회
- POST, PUT, PATCH `/members/{id}` -> 수정 
- DELETE `/members/{id}` -> 삭제 

파일관리 시스템
- GET `/files` -> 목록 조회
- GET `/files/{filename}` -> 조회
- PUT `/files/{filename}` -> 등록
- DELETE `/files/{filename}` -> 삭제 
- POST `/files` -> 파일 대량 등록

### HTTP 상태코드
- Informational responses `100`~`199`
    - 정보를 담아서 보낼 때
    - 요청이 수신되어 처리중
    - 거의 사용되지 않음

- Successful responses `200`~`299`
    - 요청 정상 처리
    - 200 OK
    - 201 Created : Header에 Location을 추가해서 새로운 리소스의 URI를 알려줄 수 있다.
    - 202 Accepted : 요청은 접수했다.
    - 204 No Content : save 버튼을 눌러서 저장만 하고 화면 변화가 필요 없을 때에
    - 200, 201을 많이 쓴다.

- Redirection messages `300`~`399`
    - 추가 행동 필요
    - Redirect를 할 때 써짐
    - 영구 리다이렉트 : 메소드와 바디가 바뀌는 301과 안바뀌는 308이 있다.
    - 일시 리다이렉트 : 일시적 변경
    - 302 : 리다이렉트시 메소드는 GET으로, 본문은 제거
    - 307 : 리다이렉트시 메소드와 본문 유지

- Client error responses `400`~`499`
    - 클라이언트 에러
    - 오류의 원인이 클라이언트에 있다
    - 400 : 요청 내용을 다시 검토해야한다(프론트엔드에서 오타나 누락된 것).
    - 401 : 인증이 안됨(로그인 안됨)
    - 403 : 권한이 없다(운영자, 스텝이 아니다).
    - 404 : 리소스가 없다(url이 틀렸다).

- Server error responses `400`~`499`
    - 서버 에러
    - 500 : 서버 내부 문제(백엔드 로직이 잘못된 것)
    - 503 : 서버가 일시 과부하

### HTTP Header
- field-name(key): value
- HTTP전송에 필요한 모든 부가정보
    - 메세지 바디의 내용
    - 메세지 바디의 크기
    - 압축
    - 인증
    - 요청 클라이언트
    - 캐시관리
- 바디의 데이터를 해석할 수 있는정보 제공

#### 표현
- Content-Type : 형식
    - text/html;charset=utf-8
    - application/josn
    - image/png
- Content-Encoding : 압축방식
    - gzip
    - deflate
    - identity : 압축 안했다는 뜻
- Content-Laguage : 언어
    - ko
    - en
- Content-Length : 길이
    - 바이트 단위

#### 컨텐트 협상(Content Negotiation)
요청시에만 사용된다.
- Accept : 클라이언트가 선호하는 미디어 타입
- Accept-Charset : 클라이언트가 선호하는 문자 인코딩
- Accept-Encoding : 클라이언트가 선호하는 압축 인코딩
- Accept-Language : 클라이언트가 선호하는 자연 언어

#### 전송방식
- 단순 전송
    - Content-Length
- 압축 전송
    - Content-Encoding: gzip
- 분할 전송
    - Transfer-Encoding: chunked
- 범위 전송
    - Range

#### 일반정보
- referer : 유입경로
- user-agent : 브라우저
- server : 요청을 처리하는 서버의 소프트웨어 정보

#### 특별정보
- HOST : 요청한 호스트 정보(도메인)
- Allow : 허용 가능한 메서드
    - 405 리스폰스를 줄 때 응답에 포함한다.
- Retry-After

#### 인증
- Authorization : 클라이언트의 인증정보를 서버에 전달
- WWW-Authenticate : 리소스 접근시 필요한 인증 방법 정의
    - 리스폰 시 401 Unauthorized와 함께 사용
    - 인증정보를 어떻게 만들지에 대한 정보

#### 쿠키
- HTTP는 무상태 연결이기에 상태를 매번 보내줘야 한다.
- 모든 요청과 링크에 사용자 정보를 포함해야 한다는 단점이 있다.
- 이를 해결하기 위해 쿠기가 도입됐다.
- Set-Cookie : 리스폰시 서버에서 클라이언트로 쿠키 전달
- Cookie : 클라이언트가 서버에서 받은 쿠키 저장
    - 요청시 서버로 전달

#### 캐시(Cache)
- Cache-control : max-age
    - 캐시 유효기간
- Cache-control : no-cache
    - 서버에 검증하고 사용
- Cache-control : no-store
    - 민감한 정보 최대한 빨리 삭제