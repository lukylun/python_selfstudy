

R, C, T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]
airs = []

for i in range(R):
    if maps[i][0] == -1:
        airs.append(i)

def dust():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    v = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if maps[r][c] != 0 and maps[r][c] != -1:
                cnt = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != -1:
                        v[nr][nc] += maps[r][c] // 5
                        cnt += maps[r][c] // 5
                maps[r][c] -= cnt

    for r in range(R):
        for c in range(C):
            maps[r][c] += v[r][c]

# 공청기 반시계
def declock():
    
    # 동북서남
    ar = [0, -1, 0, 1]
    ac = [1, 0, -1, 0]     
    direct = 0
    now = 0
    r, c = airs[0], 1
    while True:
        nr = r + ar[direct]
        nc = c + ac[direct]
        if r == airs[0] and c == 0:
            break
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            direct += 1
            continue
        maps[r][c], now = now, maps[r][c]
        r, c = nr, nc

# 공청기 시계
def clock():
    # 동남서북
    br = [0, 1, 0, -1]
    bc = [1, 0, -1, 0]
    direct = 0
    now = 0
    r, c = airs[1], 1
    while True:
        nr = r + br[direct]
        nc = c + bc[direct]
        if r == airs[1] and c == 0:
            break
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            direct += 1
            continue
        maps[r][c], now = now, maps[r][c]
        r, c = nr, nc

for t in range(T):
    dust()
    declock()
    clock()

total = 0
for r in range(R):
    for c in range(C):
        if maps[r][c] > 0:
            total += maps[r][c]

print(total)