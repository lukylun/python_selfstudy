T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    dp = [0] * 10
    for i in lst:
        dp[i] += 1

    for i in range(10):
        if dp[i] == 3:
            dp[i] -= 3

        for j in range(i, 8):
            if dp[j] == 1 and dp[j+1] == 1 and dp[j+2] == 1:
                dp[j] -= 1
                dp[j+1] -= 1
                dp[j+2] -= 1
            elif dp[j] == 2 and dp[j+1] == 2 and dp[j+2] == 2:
                dp[j] -= 2
                dp[j+1] -= 2
                dp[j+2] -= 2
    ans = 0
    for i in dp:
        if i != 0:
            ans = 1
            break

    if ans:
        print(f'#{tc} False')
    else:
        print(f'#{tc} baby-gin')
