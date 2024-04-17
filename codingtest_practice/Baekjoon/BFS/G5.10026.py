"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""
from collections import deque
# import pprint

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
RGB = [list(input()) for _ in range(N)]
v = [[0] * N for _ in range(N)]
num_r = 1
num_b = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        r, c = q.popleft()
        point = RGB[r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and point == RGB[nr][nc]:
                    v[nr][nc] = v[r][c]
                    q.append((nr, nc))
            # pprint.pprint(v)

for i in range(N):
    for j in range(N):
        if not v[i][j]:
            v[i][j] = num_r
            bfs(i, j)
            num_r += 1

v = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if RGB[i][j] == "G":
            RGB[i][j] = "R"
            
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            v[i][j] = num_b
            bfs(i, j)
            num_b += 1

print(num_r-1, num_b-1)