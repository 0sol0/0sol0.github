## Python 언어의 특징
### 컴파일된 언어(C, java)
= 컴퓨터가 이해할 수 있도록 기계어로 변역하는 과정인 컴파일이 실행됨
### 인터프리티 언어(Python)
= 컴파일하지 않고 한 줄씩 실행됨

### 동적 타입 언어(Python)
= 자료형을 선언해주지 않아도 됨
### 정적 타입 언어(C, Java)
= 자료형을 선언해 줌

* Python = 생산성, 가독성이 좋음

## 코드 컨벤션(PEP-8)
- 어떤 코드인지 알아보기 위한 서로를 위한 약속

- pascal(class) = PascalPython
- snake(변수/함수) = snake_python
- camel = camelPython
- 상수(모두 대문자로 표현) = 한번 선언하면 바뀌지 않음
PIE = 2.14

* list는 numbers or number_list로 쓴다.
* 함수 이름 = 함수의 역할로 정하는 것이 좋다
```Python
funtion add(a, b):
    return a+b
```
* 헷갈릴만한 변수를 사용하지 않는다

## python의 기초
* 변수를 2개 이상의 변수를 선언할 수 있다.
```Python
a, b, c = [1, 2, 3]
for k, v in dictionary.items():
    print(f"key:{k}, value:{v}")
```

* float은조심해서 사용해야 한다(컴퓨터는 숫자를 이진수로 인식해서 소수는 수식 에러가 난다.)
* "",''는 구분하진 않지만 일정하게 사용
"""
docstring과 
문장을 저장할 때,
사용된다.
\"특수 문자\"도 잘 출력된다.
"""

## 자료형
list = []
tuple = ('수정, 삭제가 어렵다')
set = {'중복된 데이터를 담을 수 없다'}
dict = {'key':'value', 'key2':'value2', 'key3':'value3'}
bool
flag = True
flag = false

## 변수 유효 범위(variable scope)
- 지역 변수(local variable) : 함수 안에서 선언한 변수
- 전역 변수(global variable) : 함수 밖에서 선언한 변수
* 전역변수를 사용하면 코드 관리가 어렵다
* 에러가 났을 때 원인을 추적하기 어렵다
* 문제가 생겼을 때 디버깅을 하기 어렵다

*전역변수 != 전역상수

**전역상수(변하지 않는 값)**
* 상수를 선언하고 마지막까지 변할일이 없기 때문에 사용해도 괜찮다

### 우선순위
1. 가독성 좋고 기능이 좋은 코드
2. 가독성 좋고 기능 별로인 코드
3. 가독성 안 좋고 기능도 안 좋은 기능

추천
```Python
def fun1(num):
    return num + 5
def fun2(num):
    return num + 10
def main():
    num = 10
    print(num)
    num = fun1(num)
    print(num)
    num = fun2(num)
    print(num)

main()
```
