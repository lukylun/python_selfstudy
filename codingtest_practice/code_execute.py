from collections import deque

N, M, K = map(int, input().split())
maps = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]
q = deque()

for _ in range(K):
    a, b, x, y = map(int, input().split())
    for r in range(b, y):
        for c in range(a, x):
            maps[r][c] = 1

ans = []
for i in range(N):
    for j in range(M):
        cnt = 1
        if maps[i][j] == 0:
            q.append((i, j))
            while q:
                r, c = q.popleft()
                maps[r][c] = 1
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and not maps[nr][nc]:
                        q.append((nr, nc))
                        v[nr][nc] = 1
                        cnt += 1
            ans.append(cnt)
ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))
