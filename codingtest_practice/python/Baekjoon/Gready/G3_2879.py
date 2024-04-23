N = int(input())
taps = list(map(int, input().split()))
ans_taps = list(map(int, input().split()))

ans = []
for i in range(N):
    ans.append(taps[i]-ans_taps[i])

now = ans[0]
cnt = 0
for diff in ans[1:]:
    if now > 0 and diff > now:
        now = diff
    elif now > 0 and diff < now and diff > 0:
        cnt += now - diff
        now = diff
    elif now > 0 and diff <= 0:
        cnt += now
        now = diff
    elif now == 0:
        now = diff
    elif now < 0 and diff >= 0:
        cnt += abs(now)
        now = diff
    elif now < 0 and diff < 0 and diff < now:
        now = diff
    elif now < 0 and diff < 0 and diff > now:
        cnt += abs(now - diff)
        now = diff

print(cnt+abs(now))