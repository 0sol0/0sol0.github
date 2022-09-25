## 프로젝트 구조 만들기
### Django_MVT
![Django_MVT](./Image/Django%20MVT.png)

### 프로젝트 구조
기능(sns)
- 사용자 관리(회원가입 / 로그인 / 로그아웃)
- 글쓰기
- 친구만들기

#### App 만들기
- user앱 : 사용자 관리(회원가입/로그인/로그아웃)을 담당
- tweet앱 : 글 관리(글쓰기, 삭제, 수정, 댓글)을 담당

### 프로젝트 세팅
settings.py에서 INSRALLED_APPS에 새로 만든 APP 추가

## 데이터베이스와 Django ORM 알아보기
### ORM
ORM(Object Relational Mapping) : 데이터베이스를 하나의 '객체(Object)', 'class' 덩어리로 보고 데이터베이스를 SQL언어가 아닌 'class로 쉽게 표현할 수 있게 해준다.
<br>
ex)

```Python
class myBakery:
    bread_type = ''
    bake_time = ''
    price = ''
```
- class의 이름과 내부에 선언된 변수들이 '비슷한 성격'을 가지고 있다.

#### user model 만들기
필요한 것
- 사용자를 구분하는 이름
- 비밀번호
- 상태메시지
- 생성일

```Python
from django.db import models

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = ''
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

##### djanog 모델 필드의 종류
- 문자열 : CharField, TextField
- 날짜/시간 : DateTimeField, DateFiled, TimeField
- 숫자 : IntegerField, FloatField
다른 테이블과 연관을 지어 줄 때 : ForeignKey

### 새로 만든 모델 데이터베이스에 넣기
- 데이터베이스 변경을 알려주는 명령어<br>
`$ python manage.py makemigrations`
- 변경된 데이터베이스르 반영해주는 명령어<br>
`$ python manage.py migrate`

### Django-admin
super user 만들기 : `$ createsuperuser`

#### 새로 만든 모델을 admin 페이지에 등록하기
user/admin.py
```Python
from django.contrib import admin
from .models import UserModel

# Register your models here.
admin.site.register(UserModel)
```

### Tweet 모델 만들기
```Python
from django.db import models
from user.models import UserModel

# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = 'tweet'
    
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    createdd_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
```
- `author`은 새로운 사용자가 아니기 때문에 `UserModel`에 있는 데이터를 그대로 쓴다. `ForeignKey`

데이터베이스와 연결<br>
`$ python manage.py makemigrations`<br>
`$ python manage.py migrate`<br>

admin 페이지에 등록
```Python
from django.contrib import admin
from .models import TweetModel

# Register your models here.
admin.site.register(TweetModel)
``` 

model 만들기 -> 데이터베이스와 연결 -> admin페이지에 등록

## 사용자 관리와 로그인 - 화면 띄우기
#### 템플릿 만들기(HTML 작성하기)
Django Tamplate 문법 : `{% Django Tamplate %}`
- 중복된 html을 다시 작성하지 않고 이어서 작성할 수 있도록 도와준다.

### url - view - template 이어주기
![Django_MVT](./Image/Django%20MVT.png)
- M(Model) = models.py
    - 데이터베이스의 모델(ORM)
    - 저장되고 사용되는 데이터의 형태
- T(Template) = templates폴도 내의 html
    - 사용자에게 보여지는 부분
- V(view) = views.py
    - 실질적으로 프로그램이 동작하는 부분
    - url을 요청하고 응답하는 그 사이에 일어나는'서비스'들이 종재하는 곳

URL Conf : 접속할 url을 알려줌
View : 어떤 동작을 해줄 수 있는지 작성

인터넷 브라우저에서 사용자가 url 요청 
-> settings.py가 있는 가장 처음 작성한 앱에 요청 접수 
-> 앱 안의 url.py에서 등록된 url찾기
-> 해당 url에 등록된 view를 찾기

`path('', include('user.urls'))` 처음 만든 앱의 urls.py와 'user' 안에 urls.py와 연결
-> url에 맞는 view.py 작성
-> view.py와 urls.py 연결
-> user앱의 urls.py 작성

## 사용자 관리와 로그인 - 회원가입 기능 만들기
GET : 값을 읽어 올 때
`if request.method == 'GET':`
POST : 값을 저장하거나, 수정하거나, 삭제할 때
`if request.method == 'POST:`

`<from class='form-area' method='POST' action='/sigin-up/'>`

`{% csrf_token %}`

## 사용자 관리와 로그인 - 로그인 기능 만들기
