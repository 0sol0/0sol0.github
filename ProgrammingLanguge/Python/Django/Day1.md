## Python 가상환경 만들기
1. 가상환경 만들기 `python -m venv venv`
- 파이썬 버전 확인하기 `python --version`
- pip list 확인하기 `pip list`
2. 가상환경 들어가기 `source venvv/Scripts/activate`
- pip list 확인하기 `pip list`
3. 인터프리터 설정하기 `'venv':venv`로 설정
4. django 설치하기 `pip install django`
5. 현재 pip list 저장하기 `pip freeze > requirements.txt`
- 현재 pip list 설치하기 `pip install -r requirements.txt`

## Git 연결하기
0. gitignore 설정 `.gitignore`
1. git 들어가기 `git init`
2. 원격저장소 연결하기 `git remote add origin github주소`
- branch이름 main으로 바꾸기 `git branch -M main`
3. 현재 폴더 stage에 올리기 `git add .`
4. 현재 폴더 commit하기 `git commit -m 'init'`
5. 현재 폴더 push하기 `git push origin main`

## Django 프로젝트 세팅하기
1. 프로젝트 만들기 `django-admin startproject project이름 .`
- `git add .`
- `git commit -m 'init project'`
- `git push origin main`
2. 어플리케이션(앱) 만들기 `python manage.py startapp app이름`
- `git add .`
- `git commit -m 'Add app이름 app'`
- `git push origin main`
3. 어플리케이션(앱) 등록하기 `settigs.py`-> `INSTALLED_APPS` -> `app이름`추가
- `settings.py` -> `LANGUAGE_CODE` -> `ko-kr`로 변경
- `settings.py` -> `TIME_ZONE` -> `Asia/Seoul`로 변경
4. 서버 실행하기 `python manage.py runserver`

## Django 프로젝트 구조
`__init__.py` : python에게 이 diractory를 하나의 pakage로 다루도록 지시해주는 파일
`settings.py` : 웹사이트의 모든 설정이 포함되어 있는 파일
`urls.py` : url들을 모아놓은 파일
`wsgi.py` : WSGI 동기식 웹서버 배포할 때 사용
`asgi.py` : ASGI 비동기식 웹서버 배포할 때 사용

`admin.py` : 관리자용 페이지를 관련 기능 작성하는 파일
`apps.py` : 앱의 정보가 있는 파일
`models.py` : database에 들어가는 것을 작성하는 파일
`test.py` : 테스트 코드를 만드는 파일
`views.py` : API의 logic이 짜지는 파일

## 
1. `urls.py`작성
```python
from django.urls import path
from django.contrib import admin
from 앱이름(라이브러리) import views(모듈)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url이름/', views.함수이름),
    path('url이름/<str:변수이름>', views.함수이름),
    path('url이름/<int:변수이름>', views.함수이름),
]

```
- 변수 url : 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것
    - `urls.py`에 입력한 `<str:변수이름>` `views.함수이름` -> `views.py`에 입력한 `def 함수이름(request, 변수이름):`  -> `context = {'변수이름':변수이름}` -> `return render(request, template이름, context)` -> `html`에 입력한 `{{변수이름}}`
ex) user profile에서 url에 username이 들어갈 때

2. `views.py`작성
```python
from django.shortcuts import render

def 함수이름(request):
    return render(request, 'template이름')

def 함수이름(request):
    context = {
        'key':value
    }
    return render(request, 'template이름', context)

def 함수이름(request, 변수이름):
    context = {
        '변수이름':변수이름
    }
    return render(request, 'template이름', context)
```

3. `templates`작성
- `어플리케이션(앱)` -> `templates`폴더 생성 -> `.html`작성
- `views.py`에서 `html`로 data를 넘겨주기 위해 `context = {'key':value}`를 사용
- `views.py`에 있는 `context = {'key':value}` 값을 `html`에 표시하기 위해 `{{key}}`사용
- templates 문법
    - {% for k in key %} {{k}} {% endfor %}
    - {% if %} {% elif %} {% else %} {% endif %}
    