# 11654 아스키 코드
n = input()
aski = ord(n)
print(aski)

# 11720 숫자의 합
# before
n = int(input())
numbers = input()
numbers = list(numbers)
sum_numbers = sum([int(x) for x in numbers])
print(sum_numbers)
# split()으로 나누려고 했지만 잘 되지 않아, 검색해보니 list()가 있어서 list()로 사용했다.

# 10809 알파벳찾기
# before
string_ = str(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_array = [0]*26
for i, s in enumerate(string_):
    alphabet_find =  s.find(s[i])
    
print(alphabet_find)
# after
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)))
# 아스키 코드를 활용할 생각을 하지 못했다. 좀더 넓게 사고할 필요가 있다고 느꼈다.
# chr()은 아스키 숫자를 문자로 반환시켜준다.

# 2675 문자열 반복
# befor
T = int(input())
count = 0
while True:
    number, word = map(str, input().split())
    count += 1 
    word = list(word)
    words = word*int(number)
    answer  = ''.join(words)
    print(answer)
    if count == T:
        break
# after
n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김
# 생각하는 과정과 관점이 다른 것 같다.
# 생각하는 방법이 따로 있는 것일까? 