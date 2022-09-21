# Python 4일차
## 숫자 야구 게임 해설
### 사용자의 입력을 받아 n개의 중복되지 않는 랜덤한 숫자를 생성한다.
#### Case 1
```Python
length = input()
length = random.randrange(0, 10)

length = 5
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
rabdin. suffle(number_list)

random_numbers = number_list[0:length]

print(random_number)
```

#### Case 2
```Python
length = input()
number_list = [x for x in range(10)]
random_numbers = []
for _ in range(length):
    random_numbers.append(number_list.pop(random.randrange(0, len(number_list))))

print(random_numbers)
```

#### Case 3
```Python
import random
import time
from datetime import datetime

def main()
    length = int(input())
    random_numbers = set()
    while len(random_numbers) < length:
        random_numers.add(random.randint(0.9))
        random_numbers = list(random_numbers)
        random.suffle(random_numbers)
        # print(random_numbers)
```

### 프로그램이 시작 된 시작을 기록한다.
```Python
    start_time = time.time()
    try_count = 0
```

### 사용자의 입력을 받고, 입력을 받을 때마다  try count를 1씩 더해준다.
```Python
    while True:
        input_number = input()
        if input_number == 'exit':
            return
        try_count += 1

        out_count = 0
        ball_count = 0
        strike_count = 0

        for i, v in enumerate(input_number):
            v = int(v)
            if v not in random_numbers:
                out_count += 1
            else:
                if ramdom_numbers[i] == v:
                    strike_count += 1
                else:
                    ball_count += 1
```

### 사용자의 입력이 1번에서 생성한 숫자와 일치할 경우 필요ㅛ한 정보를 출력하고 프로그램을 종료한다.
```Python
	    if strike_count == length:
            print('##########')
            print(f'시도 횟수 : {try_count}')
            print(f'소요 시간 : {time.time() - start_time:.2f}')
            print(f'클리어 날짜 : {datetime.now()}')
            print('##########')
            return
    
     print(ball_count, strike_count, out_count)

main()
```

숫자야구게임을 만들 때 너무 어렵게 생각햇던 것 같다. 특히 input_nummber에 0 < input_number < 10에 너무 매여있었던 것 같다. 그래서 함수가 더 복잡해지고 제대로 되지 않았던 것 같다.

### return
- 함수를 실행했을 때 원하는 값을 받아서 보여준다.
- 함수를 끝낸다 종료한다.

logic = 수식
```Python
import loging
DEBUG = True
def log(mesage)
    if DEBUG:
        print(f'[DEBUG]{message}')
        log('디버그 상태에서만 출력된다.')
```

LOG LEVEL

## Python 심화
### Class - Python 초급에서 중급으로 갈 때
- class에 대해서 배우면서 instance가 이해가 안되서 어려웟었다.
- 'self = class 내에서 쓸 수 있는 전역변수' 이 말을 듣고, 여러개 함수를 작성할 때 함수 내에서 사용한 변수가 다른 하마수에서 필요할 때 어덯게 사용해야될지 고민됐는데, ㄱㅡ 대 사용할 수 있겠다는 생각이 들었다.
1. 기본구조
```Python
class CookieFrame():
    def __init__(self, name):		# 인스턴스를 만듦 initialize
        print('인스턴스가 생성됐습니다')
    def set_cookie_name(self, name): # 메소드, 클래스 함수
        self.name = name

cookie1 = CookieFrame('cookie1')
cookie2 = CookieFrame('cookie2')

# 인스턴스.메소드
cookie1.set_cookie_name('cookie1')
cookie2.set_cookie_name('cookie2')

# 인스턴스.인자
print(cookie.name)
print(cookie.name)
```

2. class 내 전역변수
```Python
class Test():
    def fun1(self):     # self는 class 내에서 전역변수로 쓸 수 있다. class 한정 global
        self.number = 10
    def fun2(self):
        print(self.number)
```
- 인스턴스(instance)
- 메소드(Methode)

3. class 활용
```Python
from pprint import pprint

class Profile(): # 1
    def __init__(self): # 3
        self.profile = {
            'name': '-',
            'gender': '-',
            'birthday': '-',
            'age': '-',
            'phone': '-',
            'email': '-'
        }
    def set_profile(self, profile): # 5
        self.profle = profile   # 6
    
    def get_profile(self, profile):
        return self.profile

profile1 = profile() # 2
profile2 = profile()

profile1.set_profile({  # 4
    'name': 'lee',
    'gender': 'man',
    'birthday': '01/01',
    'age' : 32,
    'phone': '010-1234-5678',
    'email': 'abcdef@gmamil.com'
})

pprint(profile1.profile) # 7
```

### mutable & immutable
- 완전히 이해가 되지 않지만 하다보면 이해가 되지 않을까 생각한다.
```Python
immutable = 'string is immutable'
mutable = 'list is mitable'

string = immupable
list_ = mutable[stat:end:index]

string += 'immutable string'
list_.append('mutable list')

print(immutable)	# 여기까진 메모리주소가 바뀌지 않음
print(mutable)		# 여기까진 메모리주소가 바뀌지 않음
print(string)       # 새로운 메모리리 주소가 생긴다.
print(list_)		# 전의 변수와 같은 메모리 주소를 공유한다.
```

#### mutable - 값이 변한다.
list, dict

#### immutable - 값이 변하지 않는다.
int, float, str, tuple
