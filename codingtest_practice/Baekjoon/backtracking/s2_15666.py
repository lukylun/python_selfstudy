N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

def dfs():
    if len(ans) == M:
        print(*ans)
        return
    num = 0
    for i in range(N): # for i in range(s) dfs(s) start=s로 설정
        if num != lst[i] and (len(ans) == 0 or ans[-1] <= lst[i]):
            ans.append(lst[i])
            num = lst[i]
            dfs()
            ans.pop()


dfs()