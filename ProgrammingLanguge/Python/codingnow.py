
# 숫자열 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print('나비')
print('ㅋㅋㅋㅋㅋㅋ')
print('ㅋ'*9)

# boolea 자료형 # 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
print(not (5 < 10))



# 변수
# 애완동물을 소개해주세요
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '에요')
print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 아주 좋아해요')
print(name + '는 어른일까요>' + str(is_adult))

station = '사당'
print(station + '행 열차가 들어오고 있습니다.')
station = '신도림'
print(station + '행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station + '행 열차가 들어오고 있습니다')



# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5%3)
print(10%3)
print(5//3)

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3+4 == 7)

print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 2
print(number)



# 숫자처리 함수
print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(print(4.99))

from math import *
print(floor(5.99))
print(ceil(3.14))
print(sqrt(16))

# 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

day = (randint(4, 28))
print('오프라인 스터디 모임 날짜는 매월' + str(day) + '일로 선정되었습니다.')



# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = sentence+sentence2
# 나는 소년이고,
# 파이썬은 쉬워요

print(sentence3)



# 슬라이싱
jumin = '990120-1234567'
print('성별 : ' + jumin[7])
print('연 : ' + jumin[0:2] )
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])
print('생년월일 : ' + jumin[:6])
print('뒤 7자리 : ' + jumin[7:])
print(jumin[-7:])


# 문자열 처리 함수
python = 'python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('python', 'java'))

index = python.index('n')
print(index)
index = python.index('n', index + 1)
print(index)

print(python.find('java'))
print(python.count('n'))