# N, M = map(int, input().split())
# lst = sorted(list(map(int, input().split())))
# ans = set()
# s = []
#
# def dfs():
#     if len(s) == M:
#         ans.add(' '.join(map(str, s)))
#         return
#
#     for i in lst:
#         s.append(i)
#         dfs()
#         s.pop()
# dfs()
# ans = list(ans)
# for i in range(len(ans)):
#     ans[i] = list(map(int, ans[i].split()))
# ans.sort()
# for i in range(len(ans)):
#     print(' '.join(map(str, ans[i])))
#

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

def dfs():
    if len(ans) == M:
        print(*ans)
        return

    num = 0
    for i in range(N):
        if num != lst[i]:
            ans.append(lst[i])
            num = lst[i]
            dfs()
            ans.pop()

dfs()