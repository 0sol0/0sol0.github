# Python 3일차
print(eval(input())) : 사용자가 입력한 값을 그대로 받아 실행하기 때문에 보안에 취약하다 사용하려면 주의해야 한다.

## 반복문
1. 기본
* 자료형을 for문에 넣으면 돌아가면서 순서대로 값이 담겨서 나온다
* i는 요소 앞에 넘버링을 해주는 거

### list
```Python
numbers = [1, 2, 3, 4]
members = [
    ('lee', 30)
    ('kim', 27)
    ('park', 24)
]
for number in numbers;
    print(number)

for i, member in enumerate(members): # 반복되는 요소가 몇번째인지 확인할 수 있다
    print(i, numbers)

for member, age in members:
    print(member, age)

ages = [
    30,
    20,
    16
]

for i, memberin enumerate(members):
    print(member, ages[i])
```
dictionary
```Python
products = {
    'bread':1000,
    'milk':300,
    'egg':6000,
    'drink':1500
}
for k in products:
    print(k)

for v in products.value():
    print(v)

for k, v in products.items():
    print(k, v)
```

### for 활용
```Python
for i in range(1, 10, 2):
    if i <= 50:     # i가 50이 작거나 같은 경우
        continue    # 아무런 동작도 하지 않고 다음으로 넘어감(print를 하지 않고 elif로 넘어감)
        print(i)
	elif i >= 4:      # i가 4보다 크거나 같은 경우
        break       # 반복문을 중지(elif, else를 건너뛰고 마지막 print로 넘어감)
    else:
        prinnt('error')
    print('break')
```

### while
```Python
while True:
    print('hello')
```
- 무한루프가 될 수 있다.
- 반복횟수가 정해져있지 않을 때 사용

### 기본
```Python
while True:
    user_input = input()
    if user_input == '0'
        break
```
### 응용
```Python
i = 0
a = 1
while a < 5:
    a += 1
    i += 1
    print(i, a)
```

## 자주 사용되는 모듈 및 패턴

`type()`  type(무슨 자료형인지) 알려줌

### 문자형
`split()` split안의 문자를 기준으로 나눠서 list로 변환해줌
`join()`  list를 string으로 변환해줌
`replace('befor', 'after)`  값 중에 before에 있는 값을 찾아서 after로 바꿔줌

```Python
from pprint import pprint	
pprint()      # 한 줄로 들어온 데이터를 깔끔하게 출력해준다(크롤링에 많이 쓴다)
```
- 공백이랑 Tab을 섞어 쓰면 Taberror가 난다
- 공백을 선호하는 컨밴션이다

```Python
import random     # 랜덤한 로직이 필요할 때
random.shuffle()  # 무작위 섞기
random,randint(1, 10)     # 1~10 사이의 무작위 번호 뽑기(10포함)/idex = 0부터 시작하고, length = 1부터 시작하기 때문에 주의할 필요가 있다
random.randrange(1, 10)   # 1~10 사이의 무작위 번호 뽑기(10포함하지 않음)
```

```Python
strings = '12324567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*(){}{}<>,.;:?`'"~=-_+
def random_password_generator(length):
    for _ in range(length):
        password += string[random.randrage(0, len(strings))]
    retrun password
def main()
    length  = 10
    password = random_password_generator(length)
    print(password)
main()
```
* ' _ ' 사용하지 않는다는 뜻

### 시간
```Python
import time
start_time = time.time()    # 현재 시간 저장
time.slepp(1)   1초간 대기
end_time = time.time()
print(end_time-strat_time)  # 실행 시간 출력
```

```Python
from datetime import datime, timedelta  # 날짜
datetime.now()          # 현재 날짜 및 시간
string_datetime = '22/12/25 13:20'		
datetime_ = datetime.strptime(string_datetime, '%y/%m/%d %S:%M')    # string을 datetime으로 변환
three_days_ago = datetime.now() - timedelta(days=3)         # 날짜 계산
datetime_ = datetime.strftime(three_days_ago, '%y-%m-%d')         # datetime을 string으로 변환
print(datetime_)
```

### 이중 반복문(로또 번호 생성기)
```Python
def lotto_number_generator(count):
    result = []
    if count < 1:
        print('1 이상의 값을 입력해 주세요')
        return False

    for _ in range(count):
        lotto_numbers = set()
        while len(lotto) < 8:
            lotto_numbers.add(random.radint(1.45))
        result.append(lotto)numbers)
    
    return resualt

lotto = lotto_number_generator(5)
pprint(lotto_numbers)
```
- GUI(Graphic user Interpace)
- CLI(Code Line Interpace)
- Generator
- Interator
