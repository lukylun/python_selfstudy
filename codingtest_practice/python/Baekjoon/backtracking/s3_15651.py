# dfs 백트래킹
N, M = map(int, input().split())
ans = []

def dfs():
    # ans 길이가 M이면
    if len(ans) == M:
        # 출력하고
        print(' '.join(map(str, ans)))
        # dfs 리턴시킴, return 안 하면 무한 루프에 빠짐
        return

    for i in range(1, N+1):
        ans.append(i)
        # 재귀
        dfs()
        ans.pop()

dfs()