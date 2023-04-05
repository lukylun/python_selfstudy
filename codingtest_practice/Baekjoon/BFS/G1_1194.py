# 방문 3차배열 (32층까지)
# A~F 방키 => 비트마스킹 1 << j 식으로 표현

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
mazes = []
keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']
get_key = []
r, c = 0, 0
for _ in range(N):
    lst = list(input())
    for i in range(M):
        if lst[i] == '0':
            r, c = _, i
    mazes.append(lst)

q = deque()
q.append((r, c, keys))
v = [[0] * M for _ in range(N)]
cnt = 0
result = 0
while q:
    r, c = q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if not v[nr][nc] and mazes[nr][nc] == '.' or mazes[nr][nc] == '0':
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + 1

            elif not v[nr][nc] and mazes[nr][nc] in keys:
                q.append((nr, nc))
                get_key.append(mazes[nr][nc])
                mazes[nr][nc] = '.'
                cnt += v[r][c] + 1
                v = [[0] * M for _ in range(N)]
                v[nr][nc] = cnt

            elif not v[nr][nc] and mazes[nr][nc] in doors and mazes[nr][nc].lower() in get_key:
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + 1

            elif mazes[nr][nc] == '1':
                result = 1
                cnt += v[r][c]
                break

    if result == 1:
        break
    # cnt += 1
print(v)
print(cnt)

