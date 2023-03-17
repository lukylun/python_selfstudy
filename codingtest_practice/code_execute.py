N, M = map(int, input().split())
s = []
def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        # print(s)
        return

    for i in range(1, N+1):
        if len(s) == 0 or s[-1] <= i:
            s.append(i)
            dfs()
            s.pop()
dfs()