N = int(input())
lst = list(map(int, input().split()))

d = [0] * (N+1)
d[0] = 1
max_idx = 0
for i in range(1, N):
    d[i] = 1
    for j in range(i):
        if lst[j] < lst[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))