from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def comb(arr, m):
    result = []
    if m > len(arr):
        return result

    if m == 1:
        for i in arr:
            result.append([i])

    elif m > 1:
        for i in range(len(arr) - m + 1):
            for j in comb(arr[i+1:], m-1):
                result.append([arr[i]] + j)
    return result

def facility(arr):
    global minV, ans
    q = deque(arr)
    v = [[0] * N for _ in range(N)]
    maps = [[0] * N for _ in range(N)]
    for r, c in virus:
        maps[r][c] = '*'
        v[r][c] = '*'

    for r, c in walls:
        maps[r][c] = 1

    for r, c in arr:
        maps[r][c] = 2
        v[r][c] = 1
    # print(maps)
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and not maps[nr][nc]:
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + 1
                maps[nr][nc] = 2

    total = 0
    fail = 0
    for i in range(N):
        if 0 in maps[i]:
            fail = 1
        elif fail != 1:
            total = max(total, max(v[i]))
    if fail == 1:
        ans.add(-1)
        return
    else:
        minV = min(total, minV)
        ans.add(minV)
        return

N, M = map(int, input().split())
virus = []
walls = []
minV = 1e9
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 2:
            virus.append((i, j))
        elif lst[j] == 1:
            walls.append((i, j))

comb_list = comb(virus, M)
ans = set()
for i in range(len(comb_list)):
    facility(comb_list[i])

if len(ans) == 1 and -1 in ans:
    print(-1)
elif -1 in ans:
    ans.remove(-1)
    print(min(ans)-1)
else:
    print(min(ans)-1)
