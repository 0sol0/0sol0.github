import random
import time
from datetime import datetime

# input01
def number_generator(n):
# 1. 자릿수 입력
    while True:
# 1-1. n < 1
        if n < 1:
            print('1 이상의 숫자를 입력해주세요.')
            continue
# 1-2. 10 < n
        elif n > 10:
            print('10 이하의 숫자를 입력해주세요.')
            continue
        else:
            print('게임을 시작합니다.')
    return n
# 3. 게임 시작시간 저장
    start_time = time.time()
    
n = int(input())
num = number_generator(n)
print(num)
# 1-3. n = int()

# 2. 중복되지 않는 랜덤한 숫자 생성
def random_number(k):
    numbers = []
    for _ in range(n):
        while len(numbers) > n:
# 2-1. 0 < k < 10
            number = numner.add(random.radint(1, 9))
            if number not in numbers:
                numbers.add(number)
            elif number in numbers:
                continue
                num = list(map(str, numbers))
                return num       
                
# input02
def input_number(v):
# 1. 숫자 입력
    while True:
# 1-1. 0 < v
        if 0 < v:
            print('1이상의 숫자를 입력하세요.')
            continue
# 1-2. v < 10
        elif v < 10:
            print('10이하의 숫자를 입력하세요.')
            continue
        else:
# 1-5. exit 종료
            if v == 'exit':
                print('게임을 종료합니다.')
                break
# 1-3. len(k) == len(v)
            elif len(v) != len(key):
                print('자릿수가 다릅니다. 다시 입력하세요.')
                continue
            else:
                break                
# 1-4. 시도횟수 저장

v = list(map(int, input().split()))
value = input_number(v)
print(value)

# 2. 입력한 숫자와 생성된 숫자가 일치하는지 확인
# 2-1. out_count 포함되지 않음
# 2-2. ball_count 포함됨, 일치하지 않음
# 2-3. strike_count 포함됨, 일치함

# 3. 'exit' 입력 or 입력한 숫자와 생성된 숫자가 일치하면 게임 종료
# 4. 게임 종료시간 저장
# 5. 게임결과 출력
