n=int(input())
m=int(input())

graph=[[]*n for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    i,j=map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
cnt=0
def virus(start_v):
    global cnt
    visited[start_v]=True
    for w in graph[start_v]:
        if visited[w]==False:
            cnt+=1
            virus(w)
    return cnt
print(virus(1))

