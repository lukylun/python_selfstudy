N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

def dfs():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return

    for i in lst:
        if len(ans) == 0 or i >= ans[-1]:
            ans.append(i)
            dfs()
            ans.pop()

dfs()