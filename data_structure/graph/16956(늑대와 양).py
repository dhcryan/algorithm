R, C = map(int, input().split())

MAP = [list(input()) for _ in range(R)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

ck = False

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'W':
            for k in range(4):
                ii, jj = i + dx[k], j + dy[k]
                if ii < 0 or ii == R or jj <0 or jj == C:
                    continue
                if MAP[ii][jj] =='S':
                    ck = True

if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if MAP[i][j] not in 'SW':
                MAP[i][j] = 'D'
    for i in MAP:
        print(''.join(i))