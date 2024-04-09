from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
q = deque()
q.append([0, 0])
v = [[0] * (M + 1) for _ in range(N + 1)]
v[0][0] = 1

while q:
    r, c = q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and miro[nr][nc]:
            v[nr][nc] = v[r][c] + 1
            q.append([nr, nc])
        if nr == N and nc == M:
            break

print(v[N-1][M-1])
