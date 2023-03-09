from collections import deque
N, M = map(int, input().split())
maps = []
shark = deque()
v = [[0] * M for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    maps.append(lst)
    for j in range(M):
        if lst[j] == 1:
            shark.append((i, j))


while shark:
    r, c = shark.popleft()
    for d in ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1), (-1, 0)):
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < N and 0 <= nc < M and not maps[nr][nc]:
            maps[nr][nc] = maps[r][c] + 1
            shark.append((nr, nc))

ans = 0
for i in range(N):
    if max(maps[i]) > ans:
        ans = max(maps[i])
print(ans - 1)