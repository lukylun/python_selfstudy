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
#         if s.count(i) < lst.count(i) and (len(s) == 0 or s[-1] <= i):
#             s.append(i)
#             dfs()
#             s.pop()
#
# dfs()
# ans = list(ans)
# for i in range(len(ans)):
#     ans[i] = list(map(int, ans[i].split()))
#
# ans.sort()
# for i in ans:
#     print(' '.join(map(str, i)))
#

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(start, n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            print(visited, temp, '***')
            dfs(i + 1)
            visited[i] = False
            temp.pop()

dfs(0)

