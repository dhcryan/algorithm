from collections import deque
n=int(input())
graph=[list(input()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count_answer=[]

def bfs(a,b):
    cnt = 1
    queue=deque()
    queue.append((a,b))
    visited[a][b]=1 #방문했으니까
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==0 and graph[nx][ny] == '1': #방문하지 않았고 갈 수 있는 길이면
                    queue.append((nx,ny))
                    visited[nx][ny]=1 #방문했으니까 1표시함으로써 다시는 못 가도록(중복 제거)
                    cnt+=1
    return cnt

for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and graph[i][j]=='1':
            count_answer.append(bfs(i,j))
count_answer.sort()
print(len(count_answer))
for i in range(len(count_answer)):
    print(count_answer[i])
