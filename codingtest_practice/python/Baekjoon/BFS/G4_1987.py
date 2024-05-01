from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

R, C = map(int, input().split())
maps = list(input() for _ in range(R))
print(maps)
v = [[set() for _ in range(C)] for _ in range(R)]

q = deque()
q.append((0, 0, maps[0][0]))
v[0][0].add(maps[0][0])

cnt = 1

while q and cnt < 26:
    r, c, alpha = q.popleft()
    cnt = max(cnt, len(alpha))
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] not in alpha and alpha + maps[nr][nc] not in v[nr][nc]:
            q.append((nr, nc, alpha + maps[nr][nc]))
            v[nr][nc].add(alpha + maps[nr][nc])

print(cnt)
