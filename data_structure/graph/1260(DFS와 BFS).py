n,m,v=map(int,input().split())

graph=[[]*n for _ in range(n+1)]
discovered_dfs=[]*(n+1)


for _ in range(m):
    i,j=map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i].sort()
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
