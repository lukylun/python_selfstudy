N = int(input())
arr = [[0] * 1001 for _ in range(1001)]

for k in range(1, N+1):
    a, b, l, h = map(int, input().split())
    for i in range(a, a+l):
        for j in range(b, b+h):
            arr[i][j] = k

ans = [0] * (N + 1)
for x in range(1001):
    for y in range(1001):
        ans[arr[x][y]] += 1

for i in ans[1:]:
    print(i)