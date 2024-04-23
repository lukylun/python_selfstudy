from collections import deque
# import pprint

N, M = map(int, input().split())
island = [list(input()) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))
    v = [[0] * M for _ in range(N)]
    v[x][y] = 1
    
    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and island[nr][nc] == "L":
                v[nr][nc] = v[r][c] + 1
                cnt = max(cnt, v[nr][nc])
                q.append((nr, nc))
    
    return cnt-1

res = 0
for i in range(N):
    for j in range(M):
        if island[i][j] == "L":
            res = max(res, bfs(i, j))
            
print(res)