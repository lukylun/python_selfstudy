T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(M)]
    lst.sort(key=lambda x:(x[1], x[0]))
    dp = [0] * (N+1)
    cnt = 0
    for a, b in lst:
        for i in range(a, b+1):
            if dp[i] == 0:
                dp[i] = 1
                cnt += 1
                break

    print(cnt)

