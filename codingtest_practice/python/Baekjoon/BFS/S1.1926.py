from collections import deque
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(r, c):
    q = deque()
    q.append([r,c])
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny] and maps[nx][ny]:
                q.append([nx, ny])
                cnt += 1
                v[nx][ny] = 1
    
    return cnt 
        

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = []

for r in range(N):
    for c in range(M):
        if maps[r][c] == 1 and not v[r][c]:
            v[r][c] = 1
            draws = bfs(r, c)
            ans.append(draws)
if len(ans) == 0:
    print(len(ans))
    print(0)
else:
    print(len(ans))
    print(max(ans))