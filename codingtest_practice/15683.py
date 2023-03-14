d = [(0,1), (0,-1), (1,0), (-1, 0)]

N, M = map(int, input().split())
cctv = []
office = []
v = [[0] * M for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    office.append(lst)
    for j in range(M):
        if lst[j] != 0 and lst[j] != 6:
            cctv.append((i, j))
            v[i][j] = 1
            if lst[j] == 5:
                for nr, nc in d:
                    while True:
                        r = i + nr
                        c = j + nc

for r, c in cctv:
    if office[r][c] == 1:



# print(v)
# print(cctv)

