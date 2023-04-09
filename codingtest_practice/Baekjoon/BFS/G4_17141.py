from collections import deque
from copy import deepcopy
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
    maps = [[0] * N for _ in range(N)]
    q = deque(arr)
    v = [[0] * N for _ in range(N)]
    for r, c in q:
        v[r][c] = 1
        maps[r][c] = 2
    for r, c in walls:
        maps[r][c] = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and not maps[nr][nc]:
                v[nr][nc] = v[r][c] + 1
                q.append((nr, nc))
                maps[nr][nc] = 2

    cnt = 0
    fail = 0
    for i in range(N):
        cnt = max(max(v[i]), cnt)
        if 0 in maps[i]:
            fail = 1

    if fail == 1:
        ans.add(-1)
        return
    else:
        minV = min(minV, cnt)
        ans.add(minV)
        return


N, M = map(int, input().split())
walls = []
virus = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 2:
            virus.append((i, j))
        elif lst[j] == 1:
            walls.append((i, j))

comb_list = comb(virus, M)
minV = 1e9
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