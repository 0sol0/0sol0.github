## form
```html
<form action="url" method="POST">
    <label for="content"></label>
    <input type="text" id="content" name="content" />
    <input type="submit" />
</form>
```
action = 페이지 이동(url)
method = GET, POST 지정
request = 요청, 응답에 대한 모든 정보를 답고 있는 변수
페이지가 요청이 되면 요청에 대한 meta data를 포함하고 있는 HTTP request에 담아서 보내준다.
-> 적절한 view 함수를 로드
-> HTTP request를 첫번째 인수로 전달
-> 전달 받은 HTTP request를 바탕으로 HTTP response를 작성
-> 각 view는 return을 할 때 HTTP response를 반환

## url
include = 다른 앱에 있는 url을 가지고 오는 것
urls.py
```python
from django.contrib import admin
from django.urls import path, include
from 앱이름 import views

urlpatterns = [
    path('앱이름/', include('앱이름.urls')),
]
```
namespace = django template language를 이용해 해당 url로 이동할 수 있는 것
urls.py
```python
from django.urls import path
from articles import views

urlpatterns = [
    path('주소/', views.함수이름, name="주소이름"),
]
```

html
```html
<form action="{% url '앱이름:주소이름' %}" method="POST">
    <label for="content"></label>
    <input type="text" id="content" name="content" />
    <input type="submit" />
</form>
```

## templates
