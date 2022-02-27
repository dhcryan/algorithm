#11725 트리의 부모찾기
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n=int(input())
tree=[[] for _ in range(n+1)]
parent_answer=[0 for _ in range(n+1)]
visited=[False for _ in range(n+1)]
for _ in range(n-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)
# 이미 방문 체크가 되었다면 부모 노드라는 의미
def dfs(start_v):
    visited[start_v]=True
    for w in tree[start_v]:
        if visited[w]==False:
            parent_answer[w]=start_v
            dfs(w)
dfs(1)
for i in range(2,n+1):
    print(parent_answer[i])