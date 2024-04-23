def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(1, len(lst)):
            if lst[i-1] != lst[i]:
                cnt += 1
    return cnt

N = int(input())
arr = [[0] * 102 for _ in range(102)]
cnt = 0
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] = 1

arr_t = list(zip(*arr))
ans = count(arr) + count(arr_t)
print(ans)


