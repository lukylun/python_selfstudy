N = int(input())
lst = list(map(int, input().split()))

d = [0] * N
d[0] = 1


for i in range(1, N):
    d[i] = 1
    for j in range(i):
        if lst[j] < lst[i]:
            d[i] = max(d[i], d[j] + 1)

max_idx = max(d)
print(max_idx)

ans = []

for i in range(N-1, -1, -1):
    if d[i] == max_idx:
        ans.append(lst[i])
        max_idx -= 1

print(*ans[::-1])