
T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = [0] + lst
    cnt = N
    v = [0] * (N+1)
    ans = []
    for i in range(1, N+1):
        if not v[i] and i == arr[i]:
            cnt -= 1
        elif not v[i]:
            idx = arr[i]
            ans.append(arr[i])
            while True:
                if not v[idx] and arr[idx] == idx:
                    cnt -= 1
                    v[idx] = 1
                    break
                elif arr[idx] not in ans:
                    ans.append(arr[idx])
                    v[idx] = 1
                    idx = arr[idx]
                else:
                    break
            if i in ans:
                cnt -= len(ans)
            ans = []

    print(cnt)
