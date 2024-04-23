def comb(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in comb(rest_arr, n-1):
            result.append([elem] + c)
    
    return result 


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
comb_lst = [(r, c) for r in range(1, N-1) for c in range(1, N-1)]

comb_arr = comb(comb_lst, 3)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

ans = 1e9

for i in comb_arr:
    visited = []
    result = 0
    total = 0
    for r, c in i:
        total += maps[r][c]
        visited.append((r, c))
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                total += maps[nr][nc]
            else:
                result = 1
                break
        if result:
            break
    if result:
        continue
    else:
        ans = min(ans, total)
            
print(ans)