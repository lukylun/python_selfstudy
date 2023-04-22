N = int(input())
taps = list(map(int, input().split()))
ans_taps = list(map(int, input().split()))

ans = []
for i in range(N):
    ans.append(taps[i]-ans_taps[i])

cnt = 0
now = ans[i]
result = 0
for i in range(1, N):
    if ans[i] > 0 and now < 0:
        cnt += abs(now)
        now = ans[i]
    elif ans[i] < 0 and now >= 0:
        cnt += now
        now = ans[i]
    elif ans[i] > 0 and now > 0 and ans[i] > now and result != -1:
        now = ans[i]
        result = 1
    elif ans[i] > 0 and now > 0 and ans[i] > now and result == -1:
        cnt += ans[i] - now
        result = 1
    elif ans[i] > 0 and now > 0 and ans[i] < now and result != 1:
        result = -1
        cnt += now - ans[i]
        now = ans[i]
    elif ans[i] > 0 and now > 0 and ans[i] < now and result == -1:
        result = -1
        cnt += now - ans[i]
        now = ans[i]
    elif ans[i]





print(ans)