## Sort(정렬)
- 데이터를 순서대로 나열하는 것
### Bubble Sort(버블 정렬)
```Python
input = [4, 6, 2, 9, 1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j  in range(n - 1 - i)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return array

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
```
### Selection Sort(선택 정렬)
```Python
input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]
    return array


selection_sort(input)
print(input)
```

### Insertion Sort(삽입 정렬)
```Python
input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

insertion_sort(input)
print(input)
```

### Merge Sort(병합 정렬)
#### Merge(병합)
```Python
array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge(array_a, array_b))
```

#### Merge Sort(병합 정렬)
분할 정복(Divide and Conquer)
 : 문제를 작은 2개의 문제로 분할해서 각각을 해결한 다음 결과를 모아 원래의 문제를 해결하는 것
```Python
array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    return merge(merge_sort(left_array), merge_sort(right_array))
```

## Stack(스택)
LIFO = Last In First Out
- push(data) : 맨 위에 데이터 넣기
- pop() : 맨 위에 데이터 뽑기
- peek() : 맨 위에 데이터 보기
- isEmpty() : 스택이 비어있는지 여부 반환

```Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

	def push(self, value):              # 현재 [4] 밖에 없다면
        new_head = Node(value)          # [3] 을 만들고!
        new_head.next = self.head       # [3] -> [4] 로 만든다음에
        self.head = new_head            # 현재 head의 값을 [3] 으로 바꿔준다.

    # pop 기능 구현
	def pop(self):
        if self.is_empty():                  # 만약 비어있다면 에러!
            return "Stack is empty!"
        delete_head = self.head              # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next           # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head                   # 그리고 제거할 node 반환
    
	def peek(self):
        if self.is_empty():
            return "Stack is empty!"

        return self.head.data

    # isEmpty 기능 구현
	def is_empty(self):
        return self.head is None
```

#### 탑
```Python
top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, -1, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
```

## Queue(큐)
FIFO : First In First Out
- enque(data) : 맨 뒤에 데이터 추가하기
- deque() : 맨 앞에 데이터 뽑기
- peek() : 맨 앞에 있는 데이터 보기
- isEmpty(): 큐가 비어있는지 여부 반환

```Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

	def enqueue(self, value):              # 현재 [4] -> [2] 인 상태에서
        new_node = Node(value)             # [3] 을 만들고
        if self.is_empty():                # 만약 비어있다면,
            self.head = new_node           # head 에 new_node를
            self.tail = new_node           # tail 에 new_node를 넣어준다.
            return
        self.tail.next = new_node          # 현재 tail 인 [2] 의 다음을 [3] 으로 지정합니다.
        self.tail = new_node		           # 그리고 tail을 [3] 으로 지정합니다.

	def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"        # 만약 비어있다면 에러!

        delete_head = self.head             # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next          # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.

        return delete_head.data             # 그리고 제거할 node 반환

	def peek(self):
        if self.is_empty():
            return "Queue is empty!"
    
        return self.head.data

	def is_empty(self):
        return self.list.head is None
```

## Hash Table(해쉬 테이블)
Hash Table = Dictionary = Array
해쉬 함수 : 임의의 길이를 갖는 메시지를 입력하여 고정된 길이의 해쉬 값을 출력하는 함수
- put(key, value) : key에 value 저장하기
- get(key) : key에 해당하는 value 가져오기

```Python
class Dict:
    def __init__(self):
        self.items = [None] * 8

	def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

	def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!
``` 

### 충돌(Collision)
**해쉬 테이블에서 나온 충돌을 링크드리스트로 해결하는 방법**
- 체이닝(Chaining) : 연결지어 해결 = 링크드리스트를 사용하는 방식
```Python
class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):       
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

# 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
# 현재 self.items[2] 가 [("slow", "느린")] 이었다!
# 그렇다면 새로 넣는 key, value 값을 뒤에 붙여주자!
# self.items[2] == [("slow", "느린") -> ("fast", "빠른")] 이렇게! 
	def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

# 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
# 현재 self.items[2] 가 [("slow", "느린") -> ("fast", "빠른")] 이었다!
# 그렇다면 그 리스트를 돌면서 key 가 일치하는 튜플을 찾아준다.
# ("fast", "빠른") 이 일치하므로 "빠른" 이란 값을 돌려주자!
```
- 개방주소법(Opening Addreessing) : 배열의 남는 공간에 넣는 것

```Python
all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}
    for key in all_array:
        dict[key] = True  # 아무 값이나 넣어도 상관 없습니다! 여기서는 키가 중요한거니까요

    for key in present_array:  # dict에서 key 를 하나씩 없앱니다
        del dict[key]

    for key in dict.keys():  # key 중에 하나를 바로 반환합니다! 한 명 밖에 없으니 이렇게 해도 괜찮습니다.
        return key

print(get_absent_student(all_students, present_students))
```
- 시간은 극대화 시킬 수 있되 공간을 사용하는 자료구조
