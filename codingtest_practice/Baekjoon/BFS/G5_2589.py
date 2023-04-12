from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


N, M = map(int, input().split())
maps = []
islands = []
for i in range(N):
    lst = list(input())
    for j in range(M):
        if lst[j] == 'L':
            islands.append((i, j))
    maps.append(lst)

distance = 0
q = deque()
for r, c in islands:
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == "L":
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                distance = max(distance, visited[nr][nc])
print(distance-1)

