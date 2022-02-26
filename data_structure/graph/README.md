- graph: dfs and bfs

### dfs(깊이 우선 탐색)
1. 재귀 구조로 구현
```python
 #파이썬의 dictionary 자료형 활용
graph={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}
#재귀적 활용
def recursive_dfs(v,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered=recursive_dfs(w,discovered)
    return discovered
discovered=[]
recursive_dfs(1,discovered)
for i in discovered:
    print(i)
```
2. 반복 구조로 구현
- 스택을 활용하여 dfs구현
```python 
graph={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}
def iterative_dfs(start_v,discovered=[]):
    stack=[start_v]
    while stack:
        v=stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
discovered=[]
iterative_dfs(1,discovered)
for i in discovered:
    print(i)
```

### bfs
- 다익스트라 알고리즘에 유용하게 쓰임
- 큐를 이용한 반복 구조
```python
#큐를 활용한 반복구조
#파이썬의 dictionary 자료형 활용
graph={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}
#재귀적 활용
def iterative_bfs(start_v):
    discovered=[start_v]
    queue=[start_v]
    while queue:
        v=queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
print(f'iterative_bfs: {iterative_bfs(1)}')
```
### Backtracking
- 한 번 방문 후 가능성이 없는 경우에 즉시 후보를 포기

