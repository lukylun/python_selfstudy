# N, M = map(int, input().split())
# lst = sorted(list(map(int, input().split())))
# ans = set()
# s = []
# def dfs():
#     if len(s) == M:
#         ans.add(' '.join(map(str, s)))
#         return
#
#     for i in lst:
#         if lst.count(i) > s.count(i):
#             s.append(i)
#             dfs()
#             s.pop()
# dfs()
# ans = list(ans)
# for i in range(len(ans)):
#     ans[i] = list(map(int, ans[i].split()))
#
# ans = sorted(ans)
# for i in ans:
#     print(' '.join(map(str, i)))

