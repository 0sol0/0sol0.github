## 웹의 동작 순서 및 개념
### 용어 정리
- 클라이언트 : 요청을 보내는 곳<br>
- 서버 : 요청을 받아서 응답 해 주는 곳<br>
- API : 데이터를 어떻게 주고 받자! 라고 정한 약속<br>

![웹의 동작 구조](./Image/%EC%9B%B9%EC%9D%98%20%EB%8F%99%EC%9E%91%20%EA%B5%AC%EC%A1%B0.png)

- 페이지를 받는 경우 : HTML, CSS, Javascript가 적절하게 섞여있는 페이지를 받는 경우<br>
- 데이터만 받는 경우 : 페이지나 화면은 크게 필요 없고, '데이터' 만을 받고 싶은 경우<br>

## Python 기초 문법
### Python Data Type
**변수** : 데이터를 담는 바구니<br>
`변수 = 값`

#### 숫자형
`number = 1`
```Python
number1 = 3
number2 = 2

sum_number = number1 + number2
min_number = number1 - number2
mult_number = number1 * number2
div_number = number1 / number2
print(sum_number)   # 5
print(min_number)   # 1
print(mult_number)  # 6
print(div_number)   # 
```

#### 문자형
`string = 'hello'`
```Python
string_a = 'a'
string_b = 'b'
sum_string = string_a + string_b
print(sum_string)   # ab

string_c = 'a, b, c'
split_string = = string_c.split(',')
print(split_string) # ['a', 'b', 'c']
```
#### 리스트
`list = [1, 2, 3, 4, 5]`
```Python
list_ = ['a', 'b', 'c', 'd']
print(list_[0])    # a
print(list_[1])    # b
print(list_[2])    # c
print(list_)       # ['a', 'b', 'c', 'd']

list_.append('f')
print(list_)       # ['a', 'b', 'c', 'd', 'f']
```
#### 딕셔너리
`dict = {'키':'값', 'key':'value'}`
```Python
dict_ = {'name':'손흥민'}
print(dict_)    # {'name':'손흥민'}

dict_ = {'name':'paul','phone':'01012341234','birth':'0714'}

print(dict_['name'])
print(dict_.get('name'))
```

### 조건문, 반복문
#### 조건문
```
if 조건:
    조건이 참일 경우 실행
else:
    조건이 거짓일 경우 실행
```
```Python
my_age = 100

if my_age == 100:
	print("저는 100살 입니다!")
else:
	print("거짓말!")

# 저는 100살 입니다!
```
비교연산자<br>
`x < y --> x가 y보다 크다`<br>
`x > y --> x가 y보다 작다`<br>
`x == y --> x가 y보다 같다`<br>
`x != y --> x가 y보다 같지 않다`<br>
`x <= y --> x가 y보다 크거나 같다`<br>
`x <= y --> x가 y보다 작거나 같다`<br>


#### 반복문
```
for 변수 in 리스트:
    실행 할 문장
```
```Python
jumsu_list = [90,100,25,35,40]

for jumsu in jumsu_list:
	print(jumsu)
'''
90
100
25
35
40
'''
```

### 함수, 클래스
#### 함수
```
def 함수명('매개변수'):
    실행 할 문장들
```
```Python
def my_sum_func(a,b):
	result = a + b
	return result

my_sum = my_sum_func(10,20)
print(my_sum)   # 30
```

#### 클래스
```
class class명:
    실행할 함수들
```
```Python
class myBakery:
    title = ''
    time = ''
    taste = ''


cookie = myBakery()
cookie.title = '머핀'
cookie.time = '1h'
cookie.taste = '초콜릿'

print(cookie)
'''
머핀
1h
초콜릿
'''
```

## Python Web Framework
프레임워크 : 개발을 도와주는 하나의 틀

#### 종류
구분 | 최소한의 기능만 제공하는 형태 | 이미 많은 기능들을 제공하고 있는 형태
프레임워크 | Flask, Pyramid | Django
|---|---|---|
1 | 경량 프레임워크 | 거대한 프레임워크
2 | 최소한의 기능들만 제공한다. | 많은 유틸(기능)들이 이미 만들어져있다.
3 | 로그인, DB 등의 관리와 관리자 페이지 구축을 직접해 주어야 한다. | DB, 로그인, Admin, 패스워드 암호와 등 이미 제공한다.

### Django
![Django_MVT](./Image/Django%20MVT.png)
- M(model)
    - 데이베이스의 모델(ORM)
    - 저장되고 사용되는 데이터의 형태
- T(Template)
    - 사용자에게 보여지는 부분
    - 화면
- V(View)
    - 실적으로 프로그램이 동작하는 부분
    - url을 요청하고 응답하는 그 사이에 일어나는 '서비스'들이 존재하는 곳

#### ORM
Django의 ORM은 Python으로 데이터베이스 모델(class)을 만들고, <br>
만든 모델을 바탕으로 자동으로 데이터베이스를 다룰 수 있도록 도와준다.<br>
'쿼리(데이터베이스를 다루기 위해 사용하는 언어)'를 작성하지 않아도 됨<br>
ex)
```Python
class Post:
    id = IntegerField()
    title = CharField()
    author = CharField()
    context = TextField()
```
