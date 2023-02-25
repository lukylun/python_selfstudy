dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

from collections import deque
N =  int(input())
RGB = [list(input()) for _ in range(N)]
q = deque()
v = [[0] * N for _ in range(N)]

cnt_r = 0
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            q.append((i, j))
            v[i][j] = 1
            color = RGB[i][j]

            while q:
                r, c = q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < N and\
                         not v[nr][nc] and RGB[nr][nc] == color:
                        v[nr][nc] = v[r][c]
                        q.append((nr, nc))
            cnt_r += 1

for i in range(N):
    for j in range(N):
        if RGB[i][j] == "G":
            RGB[i][j] = "R"

v_2 = [[0] * N for _ in range(N)]

cnt_b = 0
for i in range(N):
    for j in range(N):
        if not v_2[i][j]:
            q.append((i, j))
            v_2[i][j] = 1
            color = RGB[i][j]
            while q:
                r, c = q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < N and\
                         not v_2[nr][nc] and RGB[nr][nc] == color:
                        v_2[nr][nc] = v_2[r][c]
                        q.append((nr, nc))

            cnt_b += 1
print(cnt_r, cnt_b)