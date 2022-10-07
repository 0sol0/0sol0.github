# 10818 최소, 최대
# before O
n = int(input())
numbers = list(map(int, input().split(' ')))
max_num = numbers[0]
min_num = numbers[0]
    
for num in numbers:
    if max_num < num:
        max_num = num
        
    elif min_num > num:
        min_num = num
    
print(min_num, max_num)
# after
cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))
# before처럼 써도 정답이지만, min, mix 메소드를 처음봐서 가져와봤다.

# 2562 최댓값
# before X
numbers = list(map(int, input().split(' ')))
max_num = max(numbers)
index = 0

for i, num in enumerate(numbers):
  index = i-1
        
print(max_num)
print(index)
# after
numbers = []
for _ in range(9):
    numbers.append(int(input()))
    
print(max(numbers))
print(numbers.index(max(numbers))+1)
# index라는 메소드를 알지 못해서 enumerate를 사용했는데 결과 값은 잘 나왔지만, 오답이라고 떴다.
# index를 사용하는 문제였던 것 같다.
# numbers = list(map(int, input().split(' '))) 대신 numbers = []와 numbers.append(int(input()))으로 입력값을 받는 방법이 있는 것도 알게 되었다.

# 3052 나머지
# before O
numbers = []
div = []

for _ in range(10):
    numbers.append(int(input()))
    for num in numbers:
        div.append(num%42)

print(len(set(div)))
# after
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))
# 다른 분의 풀이를 보니 변수가 1개만 있어도 됐던 것 같다.

# 1546 평균
# before O
n = int(input())
numbers = list(map(int, input().split(' ')))
max_num = max(numbers)
i = []

for num in numbers:    
    i.append(num/max_num*100)
    k = sum(i)/n

print(k)

# 8958 OX퀴즈
# befor
t = int(input())
score = 0

for _ in range(t):
    string = str(input())
    
    if 'O' in string:
        score += 1

print(score)
# after
T = int(input())

for _ in range(T):
    answers = input()
    total_score = 0
    point = 1
    
    for answer in answers:
        if answer == 'O':
            total_score += point
            point += 1
        else:
            point = 1

    print(total_score)
# for문을 한번 더 써서 돌렸어야 됐다는 걸 해석영상을 보고 알앗다.
# 또 point를 추가하는 방법도 알게 되었다.
