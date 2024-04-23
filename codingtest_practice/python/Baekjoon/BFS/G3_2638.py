from collections import deque
import sys
import pprint

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    v = [[0] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    v[0][0] = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
                if cheeze[nr][nc]:
                    cheeze[nr][nc] += 1
                else:
                    q.append((nr, nc))
                    v[nr][nc] = 1
def solve():
    for hour in range(1, 100000):
        bfs()
        cnt = 0
        for i in range(N):
            for j in range(M):
                if cheeze[i][j] >= 3:
                    cheeze[i][j] = 0
                    cnt += 1
                elif cheeze[i][j] == 2:
                    cheeze[i][j] = 1
        if cnt == 0:
            return hour - 1

N, M = map(int, input().split())
cheeze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = solve()
print(ans)