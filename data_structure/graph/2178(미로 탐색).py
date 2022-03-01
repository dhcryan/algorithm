from collections import deque
n,m=map(int,input().split())
graph=[list(input()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited[0][0]=True
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        if x==n-1 and y==m-1:
            return visited[n-1][m-1]
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
print(bfs(0,0))
