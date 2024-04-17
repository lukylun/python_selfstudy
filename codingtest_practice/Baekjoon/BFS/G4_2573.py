from collections import deque
import pprint
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, v):
    q = deque()
    q.append((r, c))
    v[r][c] = 1
    
    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if not v[nr][nc] and iceburg[nr][nc]:
                q.append((nr, nc))
                v[nr][nc] = 1

def solve():
    for year in range(1, 900000):
        melt_cnt = [[0] * M for _ in range(N)]
        
        for r in range(1, N-1):
            for c in range(1, M-1):
                if not iceburg[r][c]:
                    continue
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not iceburg[nr][nc]:
                        melt_cnt[r][c] += 1

        for r in range(1, N-1):
            for c in range(1, M-1):
                if melt_cnt[r][c]:
                    iceburg[r][c] = max(0, iceburg[r][c] - melt_cnt[r][c])
        
        cnt = 0
        v = [[0] * M for _ in range(N)]
        for r in range(1, N-1):
            for c in range(1, M-1):
                if not v[r][c] and iceburg[r][c]:
                    bfs(r, c, v)
                    cnt += 1
                if cnt > 1:
                    return year
        
        if cnt == 0:
            return 0 
    

N, M = map(int, input().split())
iceburg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = solve()
print(ans)