import random

my_list = ['가위', '바위', '보']
print(random.choice(my_list))

import modulefinder.goodjob
modulefinder.goodjob.say()
from modulefinder import goodbye
goodbye.bye()
import modulefinder
goodjob.say()
from modulefinder import say
say()

# 여러 값들을 순서대로 관리해야 한다 = 리스트
my_list = ['q','w', 'e', 'r']
# 접근
my_list[0]
# 추가
my_list.append('t')
my_list.insert('y')
my_list.extend('u')
# 삭제
my_list.pop('y')
my_list.remove('u')
my_list.clear('t')

# 값이 바뀔 일이 없거나, 바뀌면 안된다 = 튜플
my_tuple = ('a', 's', 'd', 'f')
# 접근
my_tuple[0]

# 값의 존재 여부가 중요하다, 중복은 안된다 = 세트
my_set = {'z', 'x', 'c', 'v'}
# 추가
my_set.add('b')
my_set.update('n')
# 삭제
my_set.pop('b')
my_set.remove('n')
my_set.discard('v')
my_set.clear('c')

# Key를 통해 효율적으로 데이터를 관리하고 싶다 = 딕셔너리
my_dictionary = {'key':'value'}
# 접근
my_dictionary['key']
my_dictionary.get('key')
# 추가
my_dictionary['key1'] = 'value1'
my_dictionary.update('key2', 'value2')
# 삭제
my_dictionary.pop('key1')
my_dictionary.popitem('value1')
my_dictionary.clear('key2')

# 튜플수정방법 = 튜플 <-> 리스트
you_tuple = ('p', 'o', 'i', 'u')
you_list=list(you_tuple)
you_list.append('y')
you_tuple=tuple(you_list)
# 리스트 순서없이 중복 없애기 = 리스트 <-> 세트
you_set=set(you_list)
you_list=list(you_set)
# 리스트 순서있이 중복 없애기 = 리스트 <-> 딕셔너리
you_dictionary=dict.fromkeys(you_list)
you_list=list(you_dictionary)

# 만약 ~라면, 참이 아니라면(생략가능), 그렇지 않다면(생략가능) = if, elif, else
today = '월요일'
if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
print('공부시작')

# if 중첩
yellow_card=0
foul = False
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴.. 조심해야지')
else:
    print('주의')

# 반복문 for 범위
for x in range(1, 10, 2):
    print(f'l {x}회')

# 반복문 for 대상
ur_list = [1,2,3]
for l in ur_list:
    print(l)
ur_tuple = (1,2,3)
for t in ur_tuple:
    print(t)

ur_dictionary = {'이름':'전다솔', '나이':'26', '키':'150', '몸무게':'50'}
for k in ur_dictionary.keys():
    print(k)
for v in ur_dictionary.values():
    print(v)
for k, v in ur_dictionary.items():
    print(k, v)

# 반복문 while
max = 25
weight = 0
item_weight = 3
while weight+item_weight<=max:
    weight+=item_weight
    print('짐을 추가합니다')
print(f'총 무게는 {weight}입니다')

# 반복문 탈출 break
drama = ['season1', 'season2', 'season3', 'season4', 'season5']
for d in drama:
    if d == 'season3':
        print('재미없대, 그만 보자')
        break
    print(f'{d}시청')

# 반복문 계속 continue
for d in drama:
    if d == 'season3':
        print('재미 없대, 건너뛰자')
        continue
    print(f'{d}시청')

# 함수 def
def show_price(전달값):
    print(f'사랑하는 {전달값} 고객님')
    print('감성 커트 가격은 15,000원입니다.')

customer1='1'
show_price(customer1)

customer2='2'
show_price(customer2)

def get_price(기본값=False):
    if 기본값 == True:
        return 10000
    else:
        return 15000

price = get_price(True)
print(f'커트 가격은 {price}원입니다')

price = get_price()
print(f'커트 가격은 {price}원입니다')

def get_price(키워드값=False, 키워드값1=False, 키워드값2=False, 키워드값3=False, 키워드값4=False, 키워드값5=False):
    if 키워드값 == True:
        return 10000
    else:
        return 15000

price=get_price(키워드값=True)
print(f'커트 가격은 {price}원입니다.')

def visit(today, *가변인자):
    print(today)
    for 전달값 in 가변인자:
        print(전달값)

전역변수 = '어디서든 사용할 수 있는 변수'
print(전역변수)

def 변수():
    지역변수 = ['함수 내에서만 사용할 수 있는 변수']
    print(지역변수)

def 전역변수2():
    global 전역변수
    전역변수 = '전역변수'
전역변수2()
print(전역변수)

f=open('list.txt', 'w', encoding='utf-8')
f.write('김xx\n')
f.write('이xx\n')
f.write('박xx\n')
f.close()

f=open('list.txt', 'r', encoding='utf-8')
contents = f.read()
print(contents)
f.close()

f=open('list.txt', 'r', encoding='utf-8')
for line in f:
    print(line, end='')
f=open('list.txt', 'w', encoding='utf-8')
f.write('김xx\n')
f.write('이xx\n')
f.write('박xx\n')
f.close()

f=open('list.txt', 'r', encoding='utf-8')
contents = f.read()
print(contents)
f.close()

with open('list.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

with open('list.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    print(contents)

with open('list.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

class BlackBox():
    def __int__(self, name, price):
        self.name=name
        self.price=price

class VideoMaker():
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender():
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
    def set_travel_mode(self, min):
        print(str(min) + '분동안 여행모드 ON')

class AdvancedTravelBackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분동안 여행모드 ON')
        self.make()
        self.send()

b1 = TravelBlackBox('하양이', 10000, 64)
b1.set_travel_mode(20)

num1 = 3
num2 = 0
try:
    result = num1/num2
    print('수행문장')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as error :
    print('에러 발생시 수행 문장', error)
else:
    print('정상 동상 시 수행 문장')
finally:
    print('마지막으로 수행할 문장')