# 1330 두 수 비교하기
#befor
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('=')
#after
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')    
# '=='이 아니라 '='을 써서 계속 헤맸다

# 9498 시험 성적
# before
score = int(input())
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')
# after
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
# if 90 <= score <= 100 으로 했는데 결과가 틀렸다고 나와서 고민해보다가 뒤에 <=100은 굳이 필요없을 것 같아 보여서 제거하고 if score >= 90으로 했더니 결과가 맞다고 나왔다.

# 2753 윤년
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)
# 배수를 구하는 식을 어떻게 만들어야 할지 모르겠어서 헤메다가 구글링을 해보니 %(나머지)를 쓴다고 나왔다.
# %(나머지)가 0인 숫자면 y와 나눴을 때 0이 나오는 숫자들이고, 곧 배수를 뜻한다.
# 이것을 알고 적용하니 바로 해결됐다.

# 14681 사분면 고르기
# before
x, y = map(int, input().split(' '))
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
# after
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
# 여기선 잘 실행 됐는데 백준에선 런타임에러(value)라고 뜬다
# 처음에 map함수를 썼었는데 찾아보니 여기선 map함수를 쓰지않고 x, y 각각 인수를 받아서 쓴다.
# 아직도 이유는 잘 모르겠다.

# 2884 알람시계
# before
h = int(input())
m = int(input())
if h == 0 and m < 45:
   print(23, m+15) 
elif h > 0 and m < 45:
    print(h-1, m+15)
else:
    print(h, m-45)
# after
h, m = map(int, input().split(' '))

if h == 0 and m < 45:
   print(23, m+15) 
elif h > 0 and m < 45:
    print(h-1, m+15)
else:
    print(h, m-45)
# 시계의 규칙으로 식을 세우기 어려웠는데, 하나씩 하다보니 되었다.
# 이건 위의 문제와 반대로 map을 사용하지 않아서 런타임에러(value error)가 떴다.
# 백준에서 원하는 value가 있는 것 같다.

# 2525 오븐 시계
# after
h, m = map(int, input().split(' '))
n = int(input())
mn = m+n
if mn < 60:
    print(h, mn)
elif h + (mn//60) < 23 and mn >= 60:
    print(h + (mn//60), mn % 60)
else:
    h = -1
    print(h + (mn//60), mn % 60)
#befor
h, m = map(int, input().split(' '))
n = int(input())
h += n // 60
m += n % 60
if m >= 60:
    h+=1
    m-=60
if h >= 24:
    h -= 24
print(h, m)
# 너무 풀리지 않아서 튜터님의 영상을 보고 문제를 풀었다
# after에 써있는데로 해도 값은 제대로 나오지만 아래 코드가 훨씬 더 깔끔해 보인다.
# divmod(n, 60) 몫과 나머지를 한번에 출력

# 2480 주사위 3개
a, b, c = map(int, input().split(' '))
m = a
if a == b and b == c and a == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    if a == b:
        m = a
    if b == c:
        m = b
    if c == a:
        m = c
    print(1000 + m * 100)
else:    
    if b > m:
        m = b
    if c > m:
        m = c
    print(m * 100)
# 최댓값을 구하는 방법을 몰라서 어려웠었다.
# 구글링해서 찾은 방법인 if b > m : m = b if c > m : m = c 를 사용해서 최댓값을 구했다
# 근데도 백준에서 틀렸다고 나와서 elif부분을 최댓값 부분을 조금 응용해서 바꿔보았더니 정답이라고 나왔다.