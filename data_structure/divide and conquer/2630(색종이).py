import sys
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = []
white, blue = 0, 0


def search(x, y, n):
    global blue, white
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]: #시작하는 지점부터 일정범위까지 중에서 다른 색깔이 나타나면
                search(x, y, n//2)
                search(x, y+n//2, n//2)
                search(x+n//2, y, n//2)
                search(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    elif color == 1:
        blue += 1


search(0, 0, N)
print(white)
print(blue)
