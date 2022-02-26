- graph: dfs and bfs

> dfs(깊이 우선 탐색)
> > 재귀 구조로 구현
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
>> 반복 구조로 구현
>> 스택을 활용하여 dfs구현
