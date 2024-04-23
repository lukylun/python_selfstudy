from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and trashes[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

N, M, K = map(int, input().split())
trashes = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    trashes[r-1][c-1] = 1

ans = []
for r in range(N):
    for c in range(M):
        if trashes[r][c] == 1 and not visited[r][c]:
            visited[r][c] = 1
            size = bfs(r, c)
            ans.append(size)

print(ans)