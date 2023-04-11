from collections import deque
import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 섬 구분하기
def bfs(i, j):
    global cnt
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    maps[i][j] = cnt
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and maps[nr][nc] == 1:
                q.append((nr, nc))
                v[nr][nc] = 1
                maps[nr][nc] = cnt

def bfs_2(i, j):
    global bridge
    q = deque()
    q.append((i, j))
    nv = copy.deepcopy(v)
    nv[i][j] = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not maps[nr][nc]:
                if not nv[nr][nc]:
                    nv[nr][nc] = nv[r][c] + 1
                    q.append((nr, nc))
                # elif nv[nr][nc] > nv[r][c] + 1:
                #     nv[nr][nc] = nv[r][c] + 1
                #     q.append((nr, nc))
            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] != 0 and maps[i][j] != maps[nr][nc]:
                nv[nr][nc] = nv[r][c]
                bridge = min(bridge, nv[nr][nc])
                # print('#')
    # print(nv)

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(N):
        if not v[i][j] and maps[i][j] == 1:
            bfs(i, j)
            cnt += 1

bridge = 1e9
for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            for d in range(4):
                ni = i + dr[d]
                nj = j + dc[d]
                if 0 <= ni < N and 0 <= nj < N and not maps[ni][nj]:
                    bfs_2(i, j)
                    break
print(bridge-1)
# print(maps)
# print(v)
