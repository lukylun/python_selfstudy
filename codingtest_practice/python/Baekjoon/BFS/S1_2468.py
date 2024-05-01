"""
장마철에 물에 잠기지 않는 안전한 영역의 최대 개수
"""
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(i, j, h):
    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and maps[nr][nc] > h:
                v[nr][nc] = 1
                q.append((nr, nc))

def solve(h):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not v[i][j] and maps[i][j] > h:
                bfs(i, j, h)
                cnt += 1

    return cnt


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(100):
    v = [[0] * N for _ in range(N)]
    ans = max(ans, solve(i))

print(ans)
