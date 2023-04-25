dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 동북서남
ar = [0, -1, 0, 1]
ac = [1, 0, -1, 0]
direct = 0

R, C, T = map(int, input().split())
maps = []
airs = []

for r in range(R):
    lst = list(map(int, input().split()))
    for c in range(C):
        if lst[c] == -1:
            airs.append(r)

    maps.append(lst)

for t in range(T):
    v = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if maps[r][c] != 0 and maps[r][c] != -1:
                total = maps[r][c]
                cnt = 1
                dust = []
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != -1:
                        v[nr][nc] += maps[r][c] // 5
                        total -= maps[r][c] // 5
                v[r][c] += total

    # 반시계 이동
    # 0행
    new_v = [[0] * C for _ in range(R)]
    for j in range(C-1):
        if maps[0][j] != -1:
            new_v[0][j] = v[0][j+1]

    if airs[0] != 0:
        for j in range(1, C):
            if maps[airs[0]][j-1] != -1:
                new_v[airs[0]][j] = v[airs[0]][j-1]
            elif maps[airs[0]][j-1] == -1:
                new_v[airs[0]][j] = 0

    for j in range(airs[0]):
        if maps[j][0] != -1 and maps[j+1][0] != -1:
            new_v[j+1][0] = v[j][0]

    for j in range(1, airs[0]+1):
        new_v[j-1][-1] = v[j][-1]

    # 시계 방향
    for j in range(C-1):
        if maps[-1][j] != -1:
            new_v[-1][j] = v[-1][j+1]

    if airs[1] != R-1:
        for j in range(1, C):
            if maps[airs[1]][j-1] != -1:
                new_v[airs[1]][j] = v[airs[1]][j-1]
            elif maps[airs[1]][j-1] == -1:
                new_v[airs[1]][j] = 0

    for j in range(airs[1], R-2):
        if maps[j][0] != -1 and maps[j+1][0] != -1:
            new_v[j+1][0] = v[j][0]

    for j in range(airs[1], R-2):
        new_v[j+1][-1] = v[j][-1]

    for i in range(R):
        for j in (0, -1):
            v[i][j] = new_v[i][j]
    for i in (0, airs[0], -1, airs[1]):
        for j in range(C):
            v[i][j] = new_v[i][j]

    cnt = 0
    for i in range(R):
        for j in range(C):
            if maps[i][j] != -1:
                maps[i][j] = v[i][j]
                cnt += v[i][j]


print(cnt)

print(maps)



