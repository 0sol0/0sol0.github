# 15596 정수 N개의 합
# before
a = [int(x) for x in input()]
def solve(a):
    ans = 0
    ans = sum([x for x in a])
    return ans
# after
def solve(a):
    total = 0
    for x in a:
        total += x
    return total
# 제출 페이지에 함수가 이미 있어서 당황했다.
# 원래는 간단하게 sum()메소드로 끝내려고 했는데, 함수가 있어서 거기에 맞추려다보니 시간이 걸렸다.
def solve(a):
    return sum(a)
# 근데 다른 분들의 풀이를 보니 상관없이 그냥했어도 돼는 것 같다;;