## Array(배열)
```Python
rooms = ['태연', '티파니', '써니', '유리', '효연', '서현', '수영', '윤아']
```
- 크기가 정해진 데이터의 공간
- 각 원소에 즉시 접근 가능 = O(1)
- 원소 중간에 삽입/삭제 하려면 모든 원소를 다 옮겨야 한다. = O(N)
- 원소를 새로 추가하려면 새로운 공간을 할당해야 한다. = 비효율적인 자료구조

## LinkedList(링크드리스트)
```Python
train_compartments = ['기관실'] -> ['시멘트'] -> ['자갈'] -> ['밀가루'] -> ['우편']
```
- 크기가 정해지지 않은 데이터의 공간
- 특정 원소를 검색하려면 연결고리를 따라 검색해야한다. = O(N)
연결고리 = 포인터
각 원소 = 노드
- 원소 중간에 삽입/삭제 하려면 앞 뒤에 포인터만 변경하면 된다. = O(1)
- 원소를 새로 추가할 때 노드를 추가하기만 하면 된다.

경우 | Array | LinkedList
---|---|---
특정 원소의 조회 | O(1) | O(N)
중간에 삽입/삭제 | O(N) | O(1)
데이터 추가 | 데이터의 추가 시 모든 공간이 다 차버렸다면 새로운 메모리 공간을 할당받아야 한다. | 모든 공간이 다 찼어도 맨 뒤의 노드만 추가하면 된다. 
정리 | 데이터에 접근하는 경우가 빈번하다면 Array를 사용하자 | 삽입과 삭제가 빈번하다면 LinkedList를 사용하자

- Python = Array로도 쓸 수 있고, LinkedList로도 쓸 수 있는 자료구조다.

### LinkedList 구현
#### 원소 추가, 원소 출력
```Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
node = Node(3) # 현재는 next 가 없이 하나의 노드만 있습니다. [3]
first_node = Node(5) # 현재는 next 가 없이 하나의 노드만 있습니다. [5]
second_node = Node(12) # [12] 를 들고 있는 노드를 만듭니다.
first_node.next = second_node # 그리고, [5]의 next 를 [12]로 지정합니다. [5] -> [12]

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

linked_list = LinkedList(5)
print(linked_list.head.data) # 5가 출력됩니다!
# 현재 LinkedList 는 (5) 만 존재합니다!

    def append(self, value):     # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        cur = self.head         
        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다. 
            cur = cur.next          
        cur.next = Node(value)


linked_list = LinkedList(5)
linked_list.append(12)
# 이렇게 되면 5 -> 12 형태로 노드를 연결한 겁니다!
linked_list.append(8)
# 이렇게 되면 5 -> 12 -> 8 형태로 노드를 연결한 겁니다!

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()

# 찾기/추가/삭제
	def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node
linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!

	def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()

	def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()
```

### LinkedList 합
```Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


    def get_linked_list_sum(linked_list_1, linked_list_2):
        sum_1 = _get_linked_list_sum(linked_list_1)
        sum_2 = _get_linked_list_sum(linked_list_2)

        return sum_1 + sum_2


    def _get_linked_list_sum(linked_list):
        sum = 0
        head = linked_list.head
        while head is not None:
            sum = sum * 10 + head.data
            head = head.next
        return sum

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
```

## 이진탐색
### 순차탐색
```Python
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_sequential(target, array):
    for number in array:
        if target == number:
            return True

    return False

result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True
```
### 이진탐색
```Python
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
```
순차탐색 = O(N)
이진탐색 = O(logN)

## 재귀함수
재귀 : 어떤 것을 정의할 때 자기 자신을 참조하는 것
재귀 함수 : 자기 자신을 호출 하는 함수
- 자기 자신을 호출함으로 코드를 더 간결하게 만들 수 있다.
- 빠져나가는 지점을 명확하게 정해줘야 한다.
RecursionError

```Python
def count_down(number):
    if number < 0:         # 만약 숫자가 0보다 작다면, 빠져나가자!
        return

    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!

count_down(60)
```

### 팩토리얼
```Python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(60))
```
### 회문 검사
#### 반복문
```Python
input = "abcba"

def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i - 1]:
            return False
    return True

print(is_palindrome(input))
```
#### 재귀 함수
```Python
input = "abcba"

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))
```

- 특정구조가 반복되는 양상
- 문제가 축소되는 특징
- 탈출조건 반드시 작성!
