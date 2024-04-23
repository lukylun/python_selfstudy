N = int(input())

minV = 10000

for i in range(N // 5 + 1):
    ans = 0
    if (N - (5 * i)) % 3 == 0:
        ans += i
        ans += (N - (5 * i)) // 3
        minV = min(ans, minV)
if minV == 10000:
    print(-1)
else: 
    print(minV)
    