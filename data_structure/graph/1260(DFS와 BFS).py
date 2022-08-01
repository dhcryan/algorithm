n,m,v=map(int,input().split())

graph=[[]*n for _ in range(n+1)]
discovered_dfs=[]*(n+1)
#단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

for _ in range(m):
    i,j=map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i].sort() #정점번호가 작은 걸 먼저 방문하니까~
    graph[j].sort()
def dfs(start_v,discovered_dfs):
    discovered_dfs.append(start_v)
    print(start_v,end=' ')
    for w in graph[start_v]:
        if w not in discovered_dfs:
            discovered_dfs=dfs(w,discovered_dfs)
    return discovered_dfs
def bfs(start_v):
    queue=[start_v]
    discovered_bfs=[start_v]
    while queue:
        v=queue.pop(0)
        print(v, end=' ')
        for w in graph[v]:
            if w not in discovered_bfs:
                discovered_bfs.append(w)
                queue.append(w)
    return discovered_bfs
dfs(v,discovered_dfs)
print()
bfs(v)
