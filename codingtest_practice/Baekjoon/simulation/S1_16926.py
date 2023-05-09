# 남동북서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def rotation(a, b):
    global direction
    r, c = a, b
    while True:
        nr = r + dr[direction]
        nc = c + dc[direction]
        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
            v[nr][nc] = maps[r][c]
            r, c = nr, nc
        else:
            direction += 1
        if direction >= 4:
            break
        
N, M, R = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    
    v = [[0] * M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            direction = 0
            if not v[n][m]:
                rotation(n, m)
    maps = v
print(maps)

