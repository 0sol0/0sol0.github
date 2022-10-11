# 숫자야구 게임 만들기
주말동안 숫자야구 게임 만들기를 했다.
하지만 완성하지 못했다.
로직이 뭔가 잘못된 것 같은데 뭔지 모르겠다.

## 게임실행순서
먼저 게임이 실행되는 순서대로 작성해봤다.

1. 자릿수 입력 함수
	- 0 < 입력 숫자 < 10
	- 게임시작시간 저장
2. 랜덤한 숫자 생성 함수
	- 중복되지 않는 숫자가 생성될 때까지 계속 생성
	- 0 < 생성된 숫자 < 10
	
3. 예측 숫자 입력 함수
	- 생성된 숫자와 입력한 숫자가 일치할 때까지 계속 입력
	- 'exit'를 입력하면 게임 종료
	- 0 < 입력 숫자 < 10
	- 자릿수가 맞지 않으면 다시 입력
	- 시도 횟수 저장

4. 생성된 숫자와 입력한 숫자 비교 함수
	- 입력한 숫자가 생성된 숫자에 포함되지 않으면 out
	- 입력한 숫자가 생성된 숫자에 포함되지만, 자리가 같지 않으면 ball
	- 입력한 숫자가 생성된 숫자에 포함되고, 자리도 같으면 strike

5. 결과 출력 함수
	- 시도 횟수
	- 게임 실행 시간
	- 실행한 날짜와 시각

---

## 함수작성순서
다음으로 함수를 작성하는 순서대로 바꿔보았다.

1. 랜덤한 숫자 생성 함수
	- 중복되지 않는 숫자가 생성될 때까지 계속 생성
	- 0 < 생성된 숫자 < 10

2. 생성된 숫자와 입력한 숫자 비교 함수
	- 입력한 숫자가 생성된 숫자에 포함되지 않으면 out
	- 입력한 숫자가 생성된 숫자에 포함되지만, 자리가 같지 않으면 ball
	- 입력한 숫자가 생선되 숫자에 포함되고, 자리가 같으면 strike

3. 자릿수 입력 함수
	- 0 < 입력 숫자 < 10
	- 제임 시작시간 저장

4. 예측 숫자 입력 함수
	- 생성된 숫자와 입력한 숫자가 일치할 때까지 계속 생성
	- 'exit'를 입력하면 게임 종료
	- 자릿수가 맞지 않으면 다시 입력
	- 0 < 입력 숫자 < 10
	- 시도횟수 저장
	- 게임 종료시간 저장

5. 결과 출력 함수
	- 시도 횟수
	- 게임 실행 시간
	- 실행한 날짜와 시각

## 함수 작성
위 순서대로 함수를 작성해봤다.
```python
import random	# 랜덤한 숫자 생성
import time	# 게임 실행시간
from datetime import datetime	# 실행한 날짜와 시각

# 1. 랜덤한 숫자 생성 함수
def random_number_generator(n):
	for _ in range(n):
		# 중복되지 않는 숫자
		random_number = set()
		while len(random_number) < n:
			# 0 < 생성된 숫자 < 10
			random_number.add(random.randint(1, 9)
			rng = list(random_number)
		break

# 2. 생성된 숫자와 입력한 숫자 비교 함수
out_count = 0
ball_count = 0
strike_count = 0

def checking_number(k, v):
	for i, k, v enumerate(k, v):
		# 입력한 숫자가 생성된 숫자에 포함되지 않으면 out
		if v[i] not in k:
			out_count += 1
			continue
		# 입력한 숫자가 생성된 숫자에 포함되고,
		elif v[i] in k:
			# 자리가 일치하지 않으면 ball
			if v[i] != k[i]:
				ball_count += 1
				continue
			# 자리가 일치하면 strike
			elif v[i] == k[i]:
				strike_count += 1
				continue

# 3. 자릿수 입력 함수
while True:
	n = int(input('숫자를 입력하세요'))
	k = random_number_generator(n)
	# 0 < 입력 숫자 < 10
	if n < 1:
		print('1 이상의 숫자를 입력하세요.')
		continue
	elif n > 9:
		print('9 이하의 숫자를 입력하세요.')
		continue
	else:
		print('게임을 시작합니다')
		# 게임 시작시잔 저장
		start_time = time.time()
break

# 4. 예측 숫자 입력 함수 
try_count = 0

while strike_count < 3:
	value = list(map(str, intput('숫자를 입력하세요.')))
	for i, v in enumerate(value):
		# 'exit'를 입력하면 게임 종료
		if 'exit' == v:
			print('게임을 종료합니다.')
			break
		# 자릿수가 맞지 않으면 다시 입력
		elif len(k) != len(v):
			print('자릿수가 맞지 않습니다. 다시 입력해주세요.')
			countinue
		else:
			int(v)
			# 0 < 입력 숫자 < 10
			if v[i] < 1:
				print('1 이상의 숫자를 입력하세요.')
				countinue
			elif v[i] > 9:
				print('9 이하의 숫자를 입력하세요.')
				continue
			# 시도횟수  저장
			else:
				try_count += 1
				continue


# 5. 결과 출력
def end_print():
	if strike_count == 3:
		end_time = time.time()
		print(f'{try_count}회 시도하셨습니다.')
		print(end_time - start_time)
		now = datetime.now()
		datetime_ = datetime.strftime(now, %y/%m/%d %H:%M)
		print(datetime_)

```
아직 제대로 실행되진 않지만 처음으로 로직을 짜고 로직대로 함수를 작성해봤다는데에 의의를 두고 더 연습해서 완성시켜야 겠다는 생각이 들었다.

