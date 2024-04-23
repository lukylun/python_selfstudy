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
q.append((r, c, '0'))
v = [[0] * M for _ in range(N)]
cnt = 0
result = 0

while q:
    r, c, k = q.popleft()
    k = int(k, 2)
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<N and 0<=nc<M:
            if not v[nr][nc][k] and mazes[nr][nc] == '.':
                v[nr][nc][k] = 1
                q.append((nr, nc, str(bin(k)[2:])))
            if not v[nr][nc][k] and mazes[nr][nc] in keys:
                v[nr][nc][k] = 1
                num = ord('a') - ord(mazes[nr][nc])
                k = '000000'
                k[num] = '1'
                q.append((nr, nc, k))
            if not v[nr][nc][k] and mazes[nr][nc] in doors:
                v[nr][nc][k] = 1
                k = str(bin(k)[2:])
                if k[ord('A') - ord(mazes[nr][nc])] == '1':
                    q.append((nr, nc, k))





