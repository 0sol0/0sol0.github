## Docker 명령어
### Docker
#### Pakage 설치
`sudo apt update`
`sudo apt install docker.io -y`
`sudo docker --version`

#### container 실행
`sudo docker run -d -p 80:80 httpd:latest`
- `run` 컨테이너 실행
- `-d` 컨테이너를 데몬(백그라운드)으로 실행
- `-p 80:80` 80번 포트로 접속했을 때 컨테이너에 접근(포토포워딩)
- `httpd:latest` httpd의 가장 최신 이미지로 컨테이너 생성

#### container 확인
`sudo docker ps`
- `CONTAINER ID` : 컨테이너가 가지고 있는 고유한 id
- `IMAGE` : 컨테이너가 생성될 때 사용된 이미지
- `COMMAND` : 컨테이너가 생성될 때 실행되는 명령어
- `CREATED` : 생성 후 경과 시간
- `STATUS` : 컨테이너 상태
- `PORTS` : 사용중인 포트
- `-a` : 중지된 컨테이너 목록까지 포함해서 모두 확인하기

#### Image 확인
`sudo docker images`
- `REPOSITORY` : 이미지 저장소 이름
- `TAG` : 이미지 버전
- `IMAGE ID` : 이미지의 고유한 id
- `CREATED` : 이미지 생성일(마지막 업데이트 일)
- `SIZE` : 이미지 용량

#### conainer 안으로 들어가기
`sudo docker exec -it $container_id /bin/bash`
- `$containser_id` : sudo docker ps를 쳤을 때 확인되는 container_id를 입력합니다.
- `/bin/bash` : 컨테이너에 접속할 때 사용되는 쉘을 입력합니다.

### Docker compose
`sudo mkdir -p /usr/lib/docker/cli-plugins`
- `/usr/lib/docker` 경로에 cli-plugins라는 디렉토리를 생성합니다.
- `-p` 만약 상위 디렉토리가 없다면 함께 생성합니다.

`sudo curl -SL https://github.com/docker/compose/releases/download/v2.11.2/docker-compose-linux-x86_64 -o /usr/lib/docker/cli-plugins/docker-compose`
- github에 release 된 docker-compose 파일을 /usr/lib/docker/cli-plugins/ 경로에 다운로드 받습니다.


`sudo chmod +x /usr/lib/docker/cli-plugins/docker-compose`
- 다운받은 docker-compose 파일에 실행 권한을 부여해 줍니다.

`sudo docker compose version`
- docker-compose가 정상적으로 설치되었는지 확인합니다.

`sudo docker compose stop` 컨테이너를 중지 시킨다.
`sudo docker compose down` 컨테이너를 종료 시킨다.

### post forwarding
#### docker-compose.yml
```yml
version: '3.8' # docker-compose.yml에 사용될 문법 버전을 정의합니다.

services:
  example: # 서비스 이름을 지정합니다. 서비스 이름은 컨테이너끼리 통신할 때 사용됩니다.
    container_name: example # 컨테이너 이름을 지정합니다.
    image: 'httpd:latest' # 컨테이너를 생성할 때 사용될 이미지를 지정합니다.
    ports: # 포트포워딩을 설정해줍니다.
     - 80:80 # 외부에서 80 포트로 접속했을 때 컨테이너의 80 포트로 연결해줍니다.
    restart: always # 컨테이너가 종료됐을 때 다시 실행시켜 줍니다.
```

### volume
#### docker-compose.yml(bind mount)
```yml
version: '3.8' # docker-compose.yml에 사용될 문법 버전을 정의합니다.

services:
  example: # 서비스 이름을 지정합니다. 서비스 이름은 컨테이너끼리 통신할 때 사용됩니다.
    container_name: example # 컨테이너 이름을 지정합니다.
    image: 'httpd:latest' # 컨테이너를 생성할 때 사용될 이미지를 지정합니다.
    ports: # 포트포워딩을 설정해줍니다.
      - 80:80 # 외부에서 80 포트로 접속했을 때 컨테이너의 80 포트로 연결해줍니다.
    volumes: # volume을 성정해줍니다.
      - ./example_http_code/:/usr/local/apache2/htdocs/ # 정의한 volume의 mount할 경로를 지정합니다.
    restart: always # 컨테이너가 종료됐을 때 다시 실행시켜 줍니다.
```

#### docker-compose.yml(docker volume)
```yml
version: '3.8' # docker-compose.yml에 사용될 문법 버전을 정의합니다.

volumes:
  example_http_code: {} # docker volume을 정의합니다.

services:
  example: # 서비스 이름을 지정합니다. 서비스 이름은 컨테이너끼리 통신할 때 사용됩니다.
    container_name: example # 컨테이너 이름을 지정합니다.
    image: 'httpd:latest' # 컨테이너를 생성할 때 사용될 이미지를 지정합니다.
    ports: # 포트포워딩을 설정해줍니다.
      - 80:80 # 외부에서 80 포트로 접속했을 때 컨테이너의 80 포트로 연결해줍니다.
    volumes: # volume을 성정해줍니다.
      - example_http_code:/usr/local/apache2/htdocs/ # 정의한 volume의 mount할 경로를 지정합니다.
    restart: always # 컨테이너가 종료됐을 때 다시 실행시켜 줍니다.
```

#### volume 보기
`sudo docker volume ls`
`sudo docker volume inspect $volume_name` 자세한 정보 확인하기

#### volume 삭제
`sudo docker volume prune`

### Dockerfile
#### Dockerfile
```Dockerfile
FROM httpd:latest

# 현재 경로에 존재하는 index.html 파일을 컨테이너 내부로 복사합니다.
COPY ./index.html /usr/local/apache2/htdocs/index.htm
```

#### docker-compose.yml
```yml
version: '3.8' # docker-compose.yml에 사용될 문법 버전을 정의합니다.

services:
  example: # 서비스 이름을 지정합니다. 서비스 이름은 컨테이너끼리 통신할 때 사용됩니다.
    container_name: example # 컨테이너 이름을 지정합니다.
    build: . # 현재 경로에 있는 Dockerfile을 사용해 이미지를 생성합니다.
    ports: # 포트포워딩을 설정해줍니다.
      - 80:80 # 외부에서 80 포트로 접속했을 때 컨테이너의 80 포트로 연결해줍니다.
    restart: always # 컨테이너가 종료됐을 때 다시 실행시켜 줍니다.
```

### entrypoint
#### Dockerfile
```Dockerfile
FROM python:3.9.15

# .pyc 파일을 생성하지 않도록 설정합니다.
ENV PYTHONDONTWRITEBYTECODE 1

# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하도록 설정합니다.
ENV PYTHONUNBUFFERED 1

# /app/ 디렉토리를 생성합니다.
RUN mkdir /app/

# /app/ 경로를 작업 디렉토리로 설정합니다.
WORKDIR /app/

# main.py 파일을 /app/ 경로로 복사합니다.
COPY ./main.py /app/
```

#### docker-compose.yml
```yml
FROM python:3.9.15

# .pyc 파일을 생성하지 않도록 설정합니다.
ENV PYTHONDONTWRITEBYTECODE 1

# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하도록 설정합니다.
ENV PYTHONUNBUFFERED 1

# /app/ 디렉토리를 생성합니다.
RUN mkdir /app/

# /app/ 경로를 작업 디렉토리로 설정합니다.
WORKDIR /app/

# main.py 파일을 /app/ 경로로 복사합니다.
COPY ./main.py /app/
```

### container 2개 이상 띄우기
#### docker-compose.yml
```yml
version: '3.8'

services:
  example1:
    container_name: example1
    image: 'httpd:latest'
    ports:
      - 80:80
    depends_on:
      - example2 # 해당 컨테이너보다 먼저 실행되어야 하는 컨테이너를 지정합니다.
    restart: always
    
  example2: # 서비스 이름이 동일하면 컨테이너가 정상적으로 생성되지 않을 수 있습니다.
    container_name: example2 # 컨테이너 이름이 동일하면 컨테이너 생성 시 에러가 발생합니다.
    build: .
    entrypoint: sh -c "python3 main.py"
    
    restart: always
```