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

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

comb_lst = comb(chickens, M)
ans = 1e9
for i in comb_lst:
    distance = 0
    for a, b in homes:
        tmp = 1e9
        for j in range(M):
            tmp = min(tmp, abs(a-i[j][0]) + abs(b-i[j][1]))
        distance += tmp
    ans = min(ans, distance)

print(ans)