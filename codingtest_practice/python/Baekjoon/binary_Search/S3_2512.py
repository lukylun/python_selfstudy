N = int(input())
lst = list(map(int, input().split()))
M = int(input())
maxV = max(lst)
start = 0
cnt = len(lst)
while M >= 1:
    if cnt:
        mid = (start + M) // cnt
    else:
        break
    for i in range(N):
        if lst[i] and lst[i] <= mid:
            M -= lst[i]
            lst[i] = 0
            cnt -= 1

        elif lst[i]:
            M -= mid
            lst[i] -= mid

    if mid == 0:
        break

print(maxV-max(lst))

start = 0
end = max(lst)

if sum(lst) <= M:
    print(max(lst))

else:
    while start <= end:
        mid = (start+end) // 2

        total = 0
        for i in lst:
            total += min(mid, i)

        if total > M:
            end = mid - 1
        else:
            start = mid + 1
    print(end)


