from collections import deque
from pprint import pprint
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

N, M, T = map(int, input().split())

v = [[0] * M for _ in range(N)]
maps = [list(map(int, input().split())) for _ in range(N)]
q = deque()
q.append((0,0))
v[0][0] = 1
distance = 1e9
ans = 0 
while q:
    r, c = q.popleft()
    if maps[r][c] == 2:
        distance = N- 1 - r + M - 1 - c  + v[r][c] -1
    
    if (r == M -1 and c == N -1):
        ans = min(v[r][c]-1, distance)
        break
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and maps[nr][nc] != 1:
            v[nr][nc] = v[r][c] + 1
            q.append((nr, nc))

print('Fail' if distance > T else ans)

