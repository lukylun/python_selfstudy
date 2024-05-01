import pprint
from collections import deque
import sys
# 북동남서
dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(s, e, d):
    cnt = 1
    q = deque()
    q.append((s, e, d))
    v[s][e] = 1

    while q:
        r, c, direct = q.popleft()
        nr = r + dr[direct][0]
        nc = c + dr[direct][1]

        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and not rooms[nr][nc]:
            q.append((nr, nc, direct))
            v[nr][nc] = 1
            rooms[nr][nc] = 1
            cnt += 1
        elif 0 <= nr < N and 0 <= nc < M and rooms[nr][nc]:
            if not v[nr][nc]:
                v[nr][nc] = 1
            direct -= 1
            if direct < 0:
                direct = 3
            q.append((r, c, direct))
        elif 0 > nr or nr > N or 0 > nc or nc > M:
            direct -= 1
            if direct < 0:
                direct = 3
            q.append((r, c, direct))
    pprint.pprint(v)

    return cnt

N, M = map(int, input().split())
s, e, d = map(int, input().split())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]

print(bfs(s, e, d))

