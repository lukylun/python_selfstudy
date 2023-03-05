#상우하좌
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 가로 R, 세로 C
C, R = map(int, input().split())
K = int(input())
v = [[0] * C for _ in range(R)]
r = 0
c = 0
direct = 0
if C * R < K:
    print(0)
else:
    for i in range(1, C * R + 1):
        v[r][c] = i
        if v[r][c] == K:
            print(c+1, r+1)
        r += dx[direct]
        c += dy[direct]

        if 0 > r or r >= R or 0 > c or c >= C or v[r][c] != 0:
            r -= dx[direct]
            c -= dy[direct]
            direct = (direct + 1) % 4
            r += dx[direct]
            c += dy[direct]
