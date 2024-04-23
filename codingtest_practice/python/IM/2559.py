N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = sum(lst[:K])
maxV = -1e9
for i in range(K, N):
    ans = ans + lst[i] - lst[i-K]
    if maxV < ans:
        maxV = ans
print(maxV)