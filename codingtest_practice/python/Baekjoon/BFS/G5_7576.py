from collections import deque
# import pprint

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
tomato = deque()

for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            tomato.append((i, j))
            v[i][j] = 1
        elif boxes[i][j] == -1:
            v[i][j] = -1

if tomato != []:
    while tomato:
        r, c = tomato.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and not boxes[nr][nc]:
                tomato.append((nr, nc))
                v[nr][nc] = v[r][c] + 1
                

minV = 0
maxV = 0
for i in range(N):
    if 0 in v[i]:
        minV = -1
        break
    elif max(v[i]) > maxV:
        maxV = max(v[i])

if minV == -1:
    print(minV)
else:
    print(maxV-1)
# pprint.pprint(v)