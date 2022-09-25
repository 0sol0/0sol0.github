import random
import time
from datetime import datetime

# 랜덤 수 생성(중복 x)
def gen_num(n):
    num_list = []
    while len(num_list) < n:
        num = random.randint(1, 9)
        if num not in num_list:
            num_list.append(num)
        elif num in num_list:
            continue
        number = ''.join(map(str, num_list))
    return number

# 입력된 숫자 검사
def test_num(check_num, ran_num):
    s = 0
    b = 0
    for i in range(n):
        for j in range(n):
            if (i == j)&(check_num[i] == ran_num[j]):
                s += 1
            elif check_num[i] == ran_num[j]:
                b += 1
    print(f'{s}S {b}B')
    return s, b

# 자릿 수 입력
while True:
    n = int(input())
    start_time = time.time()
    if n < 10:
        break
    else:
        continue
    
cnt = 0
ran_num = gen_num(n)

# 예측 시행
while True:
    check_num = input()
    if check_num == "exit":
        break
    elif len(check_num) != len(ran_num):
        print('다시입력해주세요')
        continue
    else:
        cnt += 1
        result = test_num(check_num, ran_num)
        if  result != (n, 0):
            continue
        else:
            end_time = time.time()
            print(f'횟수 {cnt}회')
            print(f'시간 {end_time-start_time:.2f}초')
            now = datetime.now()
            string_datetime = datetime.strftime(now, '%y/%m/%d %H:%M:%S')
            print(f'날짜 {string_datetime}')
            break