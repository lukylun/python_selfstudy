from collections import deque

dr = [(-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1), (2, -1), (1, -2)]

def bfs():
    q = deque()
    q.append((r, c))

    while q:
        i, j = q.popleft()
        if i == nr and j == nc:
            return maps[i][j] - 1
        
        for d in range(8):
            ni = i + dr[d][0]
            nj = j + dr[d][1]
        
            if 0 <= ni < m and 0 <= nj < m and not maps[ni][nj]:
                maps[ni][nj] = maps[i][j] + 1
                q.append((ni, nj))

T = int(input())

for _ in range(T):
    # 한 변의 길이
    m = int(input())
    # 맵
    maps = [[0] * m for _ in range(m)]
    # 출발지
    r, c = map(int, input().split())
    # 목적지
    nr, nc = map(int, input().split())
    maps[r][c] = 1

    print(bfs())
 
 