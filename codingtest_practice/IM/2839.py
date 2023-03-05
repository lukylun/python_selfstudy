N = int(input())

ans = 0
for i in range(N // 5 + 1):
    if (N - (5 * i)) % 3 == 0:
        ans += 1
        ans += (N - (5 * i)) // 3
    