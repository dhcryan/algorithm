from collections import deque
#https://lakelouise.tistory.com/80
dx=[0,0,1,-1]
dy=[1,-1,0,0]
r,c=map(int,input().split())
graph=[list(input()) for _ in range(r)]
total_sheep,total_wolf=0,0 #실질적으로 구해야 하는 솔루션
def bfs(a,b):
    sheep=0
    wolf=0
    queue=deque()
    queue.append((a,b))
    if graph[a][b]=='o': #우선 시작점 기준 양이냐 늑대냐 세야된다.
        sheep+=1
    elif graph[a][b]=='v':
        wolf+=1
    graph[a][b]='#' #세고 나서 그 곳을 제거해버린다.
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #방향별로 좌표 계산
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]!='#':
                #범위 제한
                if graph[nx][ny]=='o':
                    sheep+=1
                elif graph[nx][ny]=='v':
                    wolf+=1
                graph[nx][ny]='#' #방문했음을 표시한다.
                queue.append((nx,ny))#울타리가 아닌것을 추가한다.
    if wolf>=sheep:
        return 0,wolf
    elif sheep>wolf:
        return sheep,0
for i in range(r):
    for j in range(c):
        if graph[i][j] in 'ov': #o랑 v를 만난 경우에만 bfs를 한다.
            s,w=bfs(i,j)
            total_wolf+=w
            total_sheep+=s
print(total_sheep,total_wolf)
