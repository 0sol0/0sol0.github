## Docker 배포
### postgresql
docker-compose.yml
```yml
version: '3.8'

volumes:
  postgres: {} # postgresql에서 사용 할 볼륨 지정

services:
  postgres:
    container_name: postgres
    image: postgres:14.5
    volumes:
      - postgres:/var/lib/postgresql/data/
    environment: # postgresql 컨테이너에서 사용할 환경변수 지정해주기
      - POSTGRES_USER=user # 데이터베이스 사용자 지정
      - POSTGRES_PASSWORD=P@ssw0rd # 사용자 비밀번호 지정
      - POSTGRES_DB=django # 데이터베이스 이름 지정
    restart: always
```

### gunicorn
`git clone https://github.com/sparta-course/drf-project.git ./django`

#### django
settings.py
```python
ALLOWED_HOSTS = ['*']
STATIC_ROOT = BASE_DIR / "static"
```

#### timezone
`sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime`

#### backend/Dockerfile
```Dockerfile
# python 3.10.8버전 이미지를 사용해 빌드
FROM python:3.10.8

# .pyc 파일을 생성하지 않도록 설정합니다.
ENV PYTHONDONTWRITEBYTECODE 1

# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하도록 설정합니다.
ENV PYTHONUNBUFFERED 1

# /app/ 디렉토리를 생성합니다.
RUN mkdir /app/

# /app/ 경로를 작업 디렉토리로 설정합니다.
WORKDIR /app/

# requirments.txt를 작업 디렉토리(/app/) 경로로 복사합니다.
COPY ./django/requirements.txt .

# 프로젝트 실행에 필요한 패키지들을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# gunicorn을 사용하기 위한 패키지를 설치합니다.
RUN pip install gunicorn
```

#### dockerp-compose.yml
```yml
version: '3.8'

services:
  backend:
    container_name: backend
    build: ./backend/
    # drf_project.wsgi는 프로젝트 경로에 맞게 지정해야 합니다.
    entrypoint: sh -c "python manage.py collectstatic --no-input && python manage.py migrate && gunicorn drf_project.wsgi --workers=5 -b 0.0.0.0:8000"
    ports:
      - 80:8000
    volumes:
      - ./backend/django/:/app/
      - /etc/localtime:/etc/localtime:ro # host의 timezone 설정을 컨테이너에 적용합니다.
      # ro 은 읽기 전용(read only) 속성으로 볼륨을 설정하는 것을 의미합니다.
    restart: always
```
- `sh -c` : 컨테이너에서 뒤에 작성한 명령어를 실행시킬 수 있도록 해줍니다.

- `&&` : 특정 명령어를 실행한 이후 다음 명령어를 실행시켜 줍니다.

- `python manage.py collectstatic --no-input` : 배포를 위해 static 파일을 모아줍니다. 해당 명령어를 실행시키기 위해서는 settings.py에 STATIC_ROOT가 정의되어 있어야 합니다.

- `python manage.py migrate` : django에 연결된 db를 migrate 해줍니다.

- `gunicorn project_name.wsgi --workers=5 -b 0.0.0.0:8000` : gunicorn을 사용해 django 프로젝트를 실행시킵니다.

    - `project_name` : django 프로젝트 이름을 입력합니다. 이름을 다르게 입력할 경우 에러가 발생합니다.
    - `--workers=5` : django를 실행시킬 process 갯수를 입력합니다. 일반적으로 cpu 코어 갯수 * 2 + 1만큼 지정해줍니다.(ex - 2코어라면 2*2+1=5)
    - `-b 0.0.0.0:8000` : 8000번 포트로 실행시킵니다.

### nginx
docker-compose.yml
```yml
version: '3.8'
services:
  nginx:
    container_name : nginx
    image: nginx:1.23.2
    ports:
      - "80:80" # http 포트포워딩
      - "443:443" # https 포트포워딩
    restart: always
```

default.conf
```conf
server {
  listen 80;
  server_name _; # 모든 도메인 혹은 ip로 들어오는 요청에 대해 처리해 줍니다.

  location / { # nginx로 요청이 들어왔을 때
    proxy_pass http://backend:8000/; # backend 컨테이의 8000번 포트로 전달합니다.
  }

  location /static/ { # 브라우저에서 /static/ 경로로 요청이 들어왔을 때
    alias /static/; # /static/ 경로에 있는 파일들을 보여줍니다.
  }

  location /media/ { # 브라우저에서 /media/ 경로로 요청이 들어왔을 때
    alias /media/; # /media/ 경로에 있는 파일들을 보여줍니다.
  }
}
```

#### Dockerfile
```Dockerfile
# python 3.10.8버전 이미지를 사용해 빌드
FROM python:3.10.8

# .pyc 파일을 생성하지 않도록 설정합니다.
ENV PYTHONDONTWRITEBYTECODE 1

# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하도록 설정합니다.
ENV PYTHONUNBUFFERED 1

# /app/ 디렉토리를 생성합니다.
RUN mkdir /app/

# /app/ 경로를 작업 디렉토리로 설정합니다.
WORKDIR /app/

# requirments.txt를 작업 디렉토리(/app/) 경로로 복사합니다.
COPY ./django/requirements.txt .

# 프로젝트 실행에 필요한 패키지들을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# gunicorn과 postgresql을 사용하기 위한 패키지를 설치합니다.
RUN pip install gunicorn psycopg2
```

#### django
setting.py
```python
import os

# 환경변수에 따라 DEBUG모드 여부를 결정합니다.
DEBUG = os.environ.get('DEBUG', '0') == '1'

# 접속을 허용할 host를 설정합니다.
ALLOWED_HOSTS = ['backend', ]

# postgres 환경변수가 존재 할 경우에 postgres db에 연결을 시도합니다.
POSTGRES_DB = os.environ.get('POSTGRES_DB', '')
if POSTGRES_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': POSTGRES_DB,
            'USER': os.environ.get('POSTGRES_USER', ''),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
            'HOST': os.environ.get('POSTGRES_HOST', ''),
            'PORT': os.environ.get('POSTGRES_PORT', ''),
        }
    }

# 환경변수가 존재하지 않을 경우 sqlite3을 사용합니다.
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# CORS 허용 목록에 ec2 ip를 추가합니다.
CORS_ORIGIN_WHITELIST = ['http://$ec2_public_ip']
# ex) CORS_ORIGIN_WHITELIST = ['http://43.201.72.190']

# CSRF 허용 목록을 CORS와 동일하게 설정합니다.
CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST
```

#### docker-compose.yml
```yml
version: '3.8'

volumes:
  postgres: {}
  django_media: {}
  django_static: {}

services:
  postgres:
    container_name: postgres
    image: postgres:14.5
    volumes:
      - postgres:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=P@ssw0rd
      - POSTGRES_DB=django
    restart: always

  backend:
    container_name: backend
    build: ./backend/
    entrypoint: sh -c "python manage.py collectstatic --no-input && python manage.py migrate && gunicorn drf_project.wsgi --workers=5 -b 0.0.0.0:8000"
    volumes:
      - ./backend/django/:/app/
      - /etc/localtime:/etc/localtime:ro
      - django_media:/app/media/ # nginx에서 media를 사용할 수 있도록 volume을 지정해줍니다.
      - django_static:/app/static/ # nginx에서 static을 사용할 수 있도록 volume을 지정해줍니다.
    environment: # django에서 사용할 설정들을 지정해줍니다.
      - DEBUG=1
      - POSTGRES_DB=django
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=P@ssw0rd
      - POSTGRES_HOST=postgres
      - POSTGRES_PORT=5432
    depends_on:
      - postgres
    restart: always

  nginx:
    container_name : nginx
    image: nginx:1.23.2
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
      - django_media:/media/ # django의 media를 사용할 수 있도록 volume을 지정해줍니다.
      - django_static:/static/ # django의 static 사용할 수 있도록 volume을 지정해줍니다.
    depends_on:
      - backend
    restart: always
```

#### .env
```
DEBUG=1
POSTGRES_DB=django
POSTGRES_USER=user
POSTGRES_PASSWORD=P@ssw0rd
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

```yml
version: '3.8'

volumes:
  postgres: {}
  django_media: {}
  django_static: {}

services:
  postgres:
    container_name: postgres
    image: postgres:14.5
    # 만약 .env 파일을 다른 이름으로 사용할 경우 env_file 옵션을 사용해 불러올 수 있습니다.
    # env_file:
    #   - prod.env
    volumes:
      - postgres:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
    restart: always

  backend:
    container_name: backend
    build: ./backend/
    entrypoint: sh -c "python manage.py collectstatic --no-input && python manage.py migrate && gunicorn drf_project.wsgi --workers=5 -b 0.0.0.0:8000"
    volumes:
      - ./backend/django/:/app/
      - /etc/localtime:/etc/localtime:ro
      - django_media:/app/media/
      - django_static:/app/static/
    environment: # 
      - DEBUG
      - POSTGRES_DB
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_HOST
      - POSTGRES_PORT
    depends_on:
      - postgres
    restart: always

  nginx:
    container_name : nginx
    image: nginx:1.23.2
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
      - django_media:/media/ # django의 media를 사용할 수 있도록 volume을 지정해줍니다.
      - django_static:/static/ # django의 static 사용할 수 있도록 volume을 지정해줍니다.
    depends_on:
      - backend
    restart: always
```