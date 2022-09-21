## Tree(트리)
### 선형 구조와 비선형 구조
뿌리와 가지로 구성되어 거꾸로 세워놓은 나무처럼 보이는 계층형 비선형 자료 구조
큐(Queue), 스택(Stack) 은 자료구조에서 선형 구조
선형 구조란 자료를 구성하고 있는 데이터들이 순차적으로 나열시킨 형태를 의미
데이터가 계층적 혹은 망으로 구성
선형구조는 자료를 저장하고 꺼내는 것에 초점이 맞춰져 있고,
비선형구조는 표현에 초점이 맞춰져 있습니다.

### 트리의 용어
- Node: 트리에서 데이터를 저장하는 기본 요소 
- Root Node: 트리 맨 위에 있는 노드
- Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
- Parent Node: 어떤 노드의 상위 레벨에 연결된 노드
- Child Node: 어떤 노드의 하위 레벨에 연결된 노드
- Leaf Node(Terminal Node): Child Node가 하나도 없는 노드
- Sibling: 동일한 Parent Node를 가진 노드
- Depth: 트리에서 Node가 가질 수 있는 최대 Level

### 트리 구조 표현
- class 활용
- 완전 이진 트리일 때만 배열로 표현 가능

### 트리의 종류
- 이진 트리 : 각 노드가 최대 두 개의 자식을 가진다
- 완전 이진 트리 : 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입해야 한다는 것
#### Heep(힙)
- 힙 : 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
    - Max Heep
    - Min Heep

```Python
class MaxHeap:
    def __init__(self):
        self.items = [None]

	def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
                
	def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()
        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]
```
- 최댓값과 최솟값을 빠르게 구할 때 유용한 자료구조

## Graph(그래프)
- 비선형 구조 : 표현에 초점
- 선형구조 : 자료를 저장하고 꺼내는 것에 초점
- 그래프 : 바로 연결 관계에 초점

### 그래프 용어
- 노드(Node): 연결 관계를 가진 각 데이터를 의미합니다. 정점(Vertex)이라고도 합니다.
- 간선(Edge): 노드 간의 관계를 표시한 선.
- 인접 노드(Adjacent Node): 간선으로 직접 연결된 노드(또는 정점)

### 그래프 표현 방법
```
    2 - 3
    |
0 - 1
```
- 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현
```
    0   1   2   3
0   x   O   X   X
1   O   X   O   X
2   X   O   X   O
3   X   X   O   X
```
```Python
graph = [
    [False, True, False, False],
    [True, False, True, False],
    [False, True, False, True],
    [False, False, True, False]
]
```
- 인접 리스트(Adjacnecy List): 링크드 리스트로 그래프의 연결 관계를 표현
```
0 -> 1
1 -> 0 -> 2
2 -> 1 -> 3
3 -> 2
```

```Python
graph = {
    0:[1],
    1:[0, 2],
    2:[1, 3],
    3:[2]
}
```
- 인접 행렬 : 공간 = O(N^2), 시간 = O(1)
- 인접 리스트 : 공간 = O(E), 시간 = O(N+E)

## DFS & BFS
### DFS
- 자료의 검색, 트리나 그래프를 탐색하는 방법

한 노드를 시작으로 인접한 다른 노드를 재귀적으로 탐색해가고 끝까지 탐색하면 다시 위로 와서 다음을 탐색하여 검색한다.<br/>
DFS 는 끝까지 파고드는 것이라, 그래프의 최대 깊이 만큼의 공간을 요구합니다.<br/> 
따라서 공간을 적게 씁니다. 그러나 최단 경로를 탐색하기 쉽지 않습니다.

#### 재귀 함수
```Python
# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
```

#### 스택
```Python
# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited

print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
```

### BFS
- 한 노드를 시작으로 인접한 모든 정점들을 우선 방문하는 방법

더 이상 방문하지 않은 정점이 없을 때까지 방문하지 않은 모든 정점들에 대해서도 넓이 우선 검색을 적용한다.<br/>
BFS 는 최단 경로를 쉽게 찾을 수 있습니다. 모든 분기되는 수를 다 보고 올 수 있으니까요. <br/>
그러나, 모든 분기되는 수를 다 저장하다보니 공간을 많이 써야하고, 모든 걸 다 보고 오다보니 시간이 더 오래걸릴 수 있습니다.

#### Queue(큐)
```Python
# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited

print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
```

## Dynamic Programming(동적 계획법)
 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법을 말한다. <br/>
 이것은 부분 문제 반복과 최적 부분 구조를 가지고 있는 알고리즘을 일반적인 방법에 비해 더욱 적은 시간 내에 풀 때 사용한다.<br/>
 여러 개의 하위 문제를 풀고 그 결과를 기록하고 이용해 문제를 해결하는 알고리즘입니다!<br/>

### Fibonaci Numbers(피보나치 수열) - 재귀함수
재귀 함수 : 문제를 반복해서 해결
```Python
input = 20

def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)

print(fibo_recursion(input))  # 6765
```
- 시간이 오래걸린다.
- 같은 연산이 반복된다.

메모이제이션(Memoization) : 결과를 기록하는 것<br>
 : 이미 실험했던 내용은 기록해두고 쓰면 된다는 것

겹치는 부분 문제(Overlapping Subproblem) : 문제를 쪼갤 수 있는 구조<br> 
 : 각 구간마다의 시간을 계산하면 최적의 시간을 구할 수 있는 것 

### Fibonaci Numbers(피보나치 수열) - 동적 계획법
동적 계획법 : 문제를 반복해서 해결 그 결과를 기록하고 이용한다
 ```Python
input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

print(fibo_dynamic_programming(input, memo))
 ```

### 동적 계획법 종류
- Tob Dawn
- Bottom Up

