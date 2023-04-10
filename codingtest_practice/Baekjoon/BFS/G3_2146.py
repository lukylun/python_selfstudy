from collections import deque
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
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] != maps[r][c] and not maps[nr][nc]:
                if not v[nr][nc]:
                    v[nr][nc] = v[r][c] + 1
                    q.append((nr, nc))
                elif v[nr][nc] > v[r][c] + 1:
                    v[nr][nc] = v[r][c] + 1
                    q.append((nr, nc))

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(N):
        if not v[i][j] and maps[i][j] == 1:
            bfs(i, j)
            cnt += 1

for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            for d in range(4):
                ni = i + dr[d]
                nj = j + dc[d]
                if 0 <= ni < N and 0 <= nj < N and not maps[ni][nj]:
                    bfs_2(ni, nj)
                    break
