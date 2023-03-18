# dfs 백트래킹
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []
def dfs():
    if len(ans) == M:
        print(' '.join(map(str, ans)))

    for i in lst:
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()

dfs()