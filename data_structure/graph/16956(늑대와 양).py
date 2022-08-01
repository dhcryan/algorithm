r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
check = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for x in range(r):
    for y in range(c):
        if graph[x][y] == 'W':
            for k in range(4):  # 늑대면 주위 돌면서 양이 있는지 확인해야함
                nx = x+dx[k]
                ny = y+dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == 'S':
                        check = True
        elif graph[x][y] == 'S':
            continue
        else:
            graph[x][y] = 'D'  # 양이나 울프가 아닌것은 울타리를 채운다.
if check == True:
    print('0')
else:
    print('1')
    for i in range(r):
        print(''.join(graph[i]))
