from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    N, M, O, F, Sr, Sc, Dr, Dc = map(int, input().split())
    maps = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    for i in range(O):
        x, y, o = map(int, input().split())
        maps[x-1][y-1] = o
    # print(ma ps)
    q = deque()
    q.append((Sr-1,Sc-1, F))
    v[Sr-1][Sc-1] = 1
    result = 0
    while q:
        r, c, f = q.popleft()
        if r == Dr-1 and c == Dc-1:
            result = 1
            break
        if f == 0:
            continue
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
                if (maps[nr][nc] - maps[r][c]) <= f:
                    q.append((nr, nc, f-1))
                    v[nr][nc] = 1
    if result:
        print("잘했어!!")
    else:
        print("인성 문제있어??")