N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
dp[0] = lst[0]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1] + lst[i][j], dp[i-1][2] + lst[i][j])
        elif j == 1:
            dp[i][j] = min(dp[i-1][0] + lst[i][j], dp[i-1][2] + lst[i][j])
        else:
            dp[i][j] = min(dp[i-1][1] + lst[i][j], dp[i-1][0] + lst[i][j])

print(min(dp[-1]))