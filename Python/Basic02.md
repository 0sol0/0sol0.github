## Python 활용
### 자료형 활용하기
#### 사칙연산
`/(나누기)` : 소수점이 붙어서 나온다 = float이 나온다
`//(몫)` : 나머지를 버리고 정수로 나온다 = integer이 나온다
`%(나머지)` : 나머지가 나온다 -> 배수를 구할 때, 짝수/홀수 구할 때 사용
* 나누기와 몫이 뭐가 다른지 잘 몰랏는데 알게 되었다

- string
```Python
a = 'hello'
b = a*3
print(b)
'''
hello hello hello
'''
sample_string = 'hello'
for i in sample_string:
    print(i)
'''
h
e
l
l
o
'''
```
- 모든 것은 string으로 바꿀 수 있다.

### f-string
텍스트에 변수를 포함할 때 사용한다
```Python
n1 = 5
n2 = 10
print('n1 : %s, n2 : %s, sum : %s %{n1, n2, n1+n2}) python 2.0 ~ 3.0
print('n1 : {}, n2 : {}, sum : {}'.fomat(n1, n2, n1+n2)) python 3.0 ~ 3.5
print(f'n1 : {n1}, n2 : {n2}, sum : {n1+n2}') python 3.6 ~
```

```Python
PIE = 3.1315926535879
print(f'pie : {PIE}')   '''3.14159265358709'''
print(f'pie : {PIE:.2f}')   '''3.14'''
```
* 소수점 아래 2자까지 

list = []
index : list의 요소가 몇번째 있는지 표시하는 번호
* python의 index는 0으로 시작한다
index slicing
print(a[0:4]) : 0 <= x < 4

* 다양한 자료형을 사용할 수 있다
* 자료형을 통일해서 사용한다(=가독성)
추가.append()
삭제.remove()
수정[] = 
변환.pop()
len(길이)

tuple = ()
* 추가, 수정, 삭제를 제외한 것은 list와 동일함
* 추가, 수정, 삭제할 수 없다

set = {}
* 중복 된 값을 포함하지 않고, indexing과 slicing 기능을 지원하지 않는다

```Python
dictionary = {
    'key':'value', 
    'key2':'value',
    'key3':'value'
    }
dict['key']
dictionary.get('key4','value4') 

# 'key4'있으면 해당 value를 출력 / 'key4'가 없으면 'value4'를 출력
# django에서 많이 쓰임

추가['key4'] = 'value4'
수정['key'] = 'value5'
del(삭제['key4'])
```

list = [] / tuple = () / set = {}
list(tuple) / list(set) : list로 바뀜
tuple(list) / tuple(set) : tuple로 바뀜
set(list) / set(tuple) : set으로 바뀜

## 함수
* 모든 로직을 함수에서 수행하는 것을 추천한다(전역변수를 사용하지 마라)
기본
```Python
def funtion():
    print('hello')
funtion()
```

출력 순서(함수 출력 기본 구조)
```Python
def multiply(a, b):
    return a*b

def main():
    num1 = 5
    num2 = 10

    result = multiply(num1, num2)
    return result

r = main()
pritn(r)
```

### from(어디서) import(어떤 것)
* 다른 파일에 있는 코드(변수, 함수, 클래스)를 가져와서 사용하기
import 파일명
파일명.함수()
from 파일명 import 함수
함수()
from 파일명 import *
함수()

from 폴더명 import *
폴더명.파일명.함수()
from 폴더명 immport 파일명
파일명.함수()
from 폴더명.파일명 import *
함수()

' * '을 쓰는 것은 파일의 출처를 알기 어렵기 때문에 권장하지 않는다.
변수를 각각 지정하기 보다 파일을 직접 import해서 쓰는 것을 제일 권장한다
'''
file1.defind1()
folder1.file2.defind1()
folder1.file3.defind1()
folder1.file3.defind2()
'''
' .' 을 기준으로 생각하면 된다

### 비교연산자 = boolean
in 포함하는지(Ture) 포함하지 않는지(False) 출력

```Python
if True and False: 둘다 True 일 때 print
    print(1) if 조건인 True일 때 출력
elif False or True: 둘 중 하나가 True 일 때 print
    print(2) if가 False이고, elif가 True일 때 출력
else:	elif가 False일 때, print
    print(3)
and, or과 if문이 출력되는 순서가 했갈렸는데 오늘 알게 되었다.
empty_list_sting -> False -> Not False -> True
bool()
```
