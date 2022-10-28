## 시리얼라이져
object형식 data를 string형식 data로 바꿔주는 것
request를 response할 때, `JSON`형식이 필요한데. 프로젝트 폴더에 있는 `models.py`의 data들을 `JSON`형식으로 바꿔주는 것

## 데코레이터
함수를 꾸며주는 함수
인자로 함수를 받고, 받은 함수 값의 위, 아래에 새로 실행하는 값을 더해서 꾸며진 함수를 return시켜주는 함수
```python
def wrapper_funtion(funtion):
    def decorator_funtion():
        print("함수 이전에 실행")
        funtion()
        print("함수 이후에 실행")
    return decorator_funtion

def base_funtion():
    print("실행하고자 하는 함수")

base_funtion()

new_funtion = wrapper_funtion(base_funtion())
new_funtion()
```

```python
@wrapper_funtion
def base_funtion():
    print("실행하고자 하는 함수")
```

## swagger
프로젝트에 있는 API를 자동으로 문서화하는 라이브러리
