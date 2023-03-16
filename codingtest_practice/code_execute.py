N, M = map(int, input().split())

ans = 1
cnt = 1
for i in range(N, N - M, -1):
    ans *= i
    ans //= (N + 1 - i)

print(ans)