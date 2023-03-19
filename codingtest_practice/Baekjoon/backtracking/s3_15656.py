import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
lst = sorted(list(map(int, input().rstrip().split())))
ans = []

def dfs():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return

    for i in lst:
        ans.append(i)
        dfs()
        ans.pop()

dfs()