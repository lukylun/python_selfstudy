from collections import deque
import copy
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

def virus(arr):
    global maxV
    virus_map = copy.deepcopy(maps)
    cnt = 0
    q = deque()

    for i in range(len(arr)):
        x, y = arr[i]
        virus_map[x][y] = 1


    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 2:
                q.append([i,j])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <=nc < M and virus_map[nr][nc] == 0:
                virus_map[nr][nc] = 2
                q.append((nr, nc))


    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 0:
                cnt += 1

    maxV = max(maxV, cnt)

    return

N, M = map(int, input().split())
maps = []
arr_zero = []
arr_two = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 0:
            arr_zero.append([i, j])

    maps.append(lst)

comb_list = comb(arr_zero, 3)
maxV = 0
for i in range(len(comb_list)):
    virus(comb_list[i])
print(maxV)