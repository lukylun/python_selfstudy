from collections import deque

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(y, x):
    q = deque()
    q.append((y, x))
    v[y][x] = 1
    
    while q:
        h, w = q.popleft()
        for d in range(8):
            nr = h + dr[d]
            nc = w + dc[d]
            if 0 <= nr < r and 0 <= nc < c and not v[nr][nc] and maps[nr][nc]:
                q.append((nr, nc))
                v[nr][nc] = 1

while True:
    c, r = map(int, input().split())
    
    if not r and not c:
        break
    
    maps = [list(map(int, input().split())) for _ in range(r)]
    v = [[0] * c for _ in range(r)]
    cnt = 0 

    for i in range(r):
        for j in range(c):
            if maps[i][j] and not v[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
    
    

