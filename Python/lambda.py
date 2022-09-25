people = list(map(int, input().split()))

# 20살 미만 제외
# adult_people = list(filter(lambda x: x >= 20, people))

adult_people = [x for x in people if x >= 20]

# 나이순으로 정렬
adult_people.sort(key=lambda x: x[2])