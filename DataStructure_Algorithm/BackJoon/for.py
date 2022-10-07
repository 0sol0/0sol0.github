# # 2739 구구단
# n = int(input())
# for i in range(1, 10):
#     print(f'{n} * {i} =', n*i)

# # 10950 A+B-3
# # before
# count = 0
# t = int(input())
# num1 = list(map(int, input().split(' ')))
# num2 = list(map(int, input().split(' ')))
# for n1 in num1:
#     for n2 in num2:
#         count += 1
#         if count == t:
#             print(n1+n2)
# # after
# t = int(input())
# for n in range(t):
#     a, b = map(int, input().split())
#     print(a+b)
# 테스트 개수(t)대로 출력하는 방법을 몰라서 어려웠고, 또 한 번에 테스트 개수(t)만큼 입력을 받으려고 생각한 것이 실수였던 것 같다
# 이건 검색해보고 약간 허탈한 문제였다. 조금만 다르게 생각했어도 풀었을 문제였을텐데, 생각에 갖혀서 시간이 많이 걸렸다.

# 8393 합
# before
n = int(input())
num = []

for x in range(1, n):
    num.append(x)
    ans = sum(num)
    
print(ans+n)
# after
a = int(input())
sum = 0
for i in range(a+1):
    sum = sum + i
print(sum)
# range()에 +1 넣기
# 변수 하나 더 만들어 주기