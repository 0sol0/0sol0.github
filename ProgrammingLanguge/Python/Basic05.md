## try - except

1. 기본 구조
```Python
number = 'num'

try:
    number = int(number)
except:
    print(f'{number}은(느는 숫자가 아닙니다.')
    pass
```
- try에서 error가 발생햇을 때 except가 실행된다.
- pass는 아무것도 안하고 넘어가는 것
- countinue는 반복문에서 다음 반복문으로 넘어가는 것
- if/else랑 비슷하다

2. error 종류
```Python
try:
    number = (int(number))
    print(10 / number)

except ValueError:      # int로 변환하는 과정에서 에러가 발생 
    print(f'{number}은(는) 숫자가 아닙니다.')

except ZeroDivisionError:		# 0으로 나누면서 에러가 발생했을 때
	print('0으로 나눌 수 없습니다.')

except Exception as e:		# 위에서 정의하지 않은 에러가 발생했을 때(권장하지 않음)
	print(f'예상하지 못한 에러가 말생햇씁니다. error : {e}')

```
- 프로그램에 에러가 나지 않도록 해줄 수 있겠다.

## stacktrace
- 알고리즘할 대는 몰라도 되지만 큰 프로젝트를 할 때 필요한 것
- 에러가 발생한 위치를 찾아내기 위해 호출된 함수의 목록을 보여주고 개발자는 stacktrace를 따라가면 에러가 발생한 위치를 추적할 수 있음

## Comprehension(축약식)
### list[], tuple(), set{}
```Python
list_ = [x for x in range(5)]
```

1. Case 1
```Python
sum_age = 0
for i in people:
    sum_age +=i[1]
average_age = sum_age / len(people)
```

2. Case 2
```Python
ages = [x[i] for x in people]
sum_ages = sum(ages)
aberage_age = sum_ages / len(people)
```

3. Case 3
```Python
average_age = sum([x[1] for x in people]) / len(people)
```
### dictionary
```Python
dictionary = {name: 
            {'age':age, 
            'gender':gender} 
            for name, age, gender in people}
```

### list -> dictionary
```Python
dictionary = {{'name': name 
            'age':age, 
            'gender':gender} 
            for name, age, gender in people}
```
- 익숙해지면 코드를 정말 간단하게 쓸 수 있을 것 같다.

## lambda / map / filter / sort
### lambda(익명 함수)
```Python
lambda x, y: x + y
```
- 혼자 사용하지 않는다(map, filter, sort와 같이 쓴다)

### map
```Python
map(int, iniput().split(' '))
```

1. case 1
```Python
integer_numbers = []
for i in string_numbers:
    integer_numbers.appeind(int[i])
```

2. case 2
```Python
integer_numbers = list(map(int, string_numbers))
```

3. case 3
```Python
integer_numbers = [int(x) for x in strin_numbers]       # list 축약식
```

- 2의 배수
1. case 1
```Python
double_numbers = list(map(lambda x: x*2, numbers))
```

2. case 2
```Python
double_numbers = [x*2 for x in numbers]     # list 축약식
```

### filter
1. case 1
```Python
even_numbers = list(filter(lambda x: x%2 == 0, numbers))    # True인 값만 담을 때
```

2. case 2
```Python
even_numbers = [x for in bynbers if x%2 == 0]
```

### sort - list 축약식으로 대체 못함
1. case 1
```Python
numbers.sort()
numbers.sort(revers=True)
```

2. case 2
```Python
people.sort(key=lambda x: x[1])
people.sort(key=lambda x: x[1], reverse=True)
```

3. case 3
```Python
people.sort(key=lambda x: (x[0], x[1]))
people.sort(key=lambda x: (x[0], x[1]), reverse=True)
```