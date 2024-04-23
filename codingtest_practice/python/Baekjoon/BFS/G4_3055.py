from collections import deque
import pprint
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(w, g):
    q = deque()
    cnt = 0
    for si, sj in w:
        q.append((si, sj))
    for si, sj in g:
        q.append((si, sj))

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if maps[r][c] == "*":
                if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == ".":
                    q.append((nr, nc))
                    maps[nr][nc] = "*"

            elif maps[r][c] == "S":
                if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == "D":
                    v[nr][nc] = v[r][c] + 1
                    return
                elif 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == "." and not v[nr][nc]:
                    q.append((nr, nc))
                    v[nr][nc] = v[r][c] + 1
                    maps[nr][nc] = "S"

R, C = map(int, input().split())
maps = []
gosum = []
bx, by = 0, 0
water = []
v = [[0] * C for _ in range(R)]

for i in range(R):
    lst = list(sys.stdin.readline().strip())
    maps.append(lst)
    for j in range(C):
        if lst[j] == "S":
            gosum.append((i, j))
            v[i][j] = 1
        elif lst[j] == "D":
            bx, by = i, j
        elif lst[j] == "*":
            water.append((i, j))

bfs(water, gosum)

if v[bx][by]:
    print(v[bx][by] - 1)
else:
    print("KAKTUS")
