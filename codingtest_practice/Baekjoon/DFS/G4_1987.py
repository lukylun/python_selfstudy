# dr = [-1, 1, 0 ,0]
# dc = [0, 0, -1, 1]
#
# def dfs(r, c, count):
#     global cnt
#     cnt = max(cnt, count)
#
#     for d in range(4):
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] not in ans:
#             ans.add(lst[nr][nc])
#             dfs(nr, nc, count + 1)
#             ans.remove(lst[nr][nc])
#
#
# N, M = map(int, input().split())
# lst = [list(input()) for _ in range(N)]
# ans = set()
# ans.add(lst[0][0])
# cnt = 0
#
# dfs(0, 0, 1)
#
# print(cnt)
#

dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
ans = set([(0, 0, lst[0][0])])
# print(ans)
cnt = 0

# 알파벳 총 개수는 26, 26이되면 뒤에 더 볼 필요가 없음
while ans and cnt < 26:
    r, c, alpha = ans.pop()
    cnt = max(cnt, len(alpha))
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] not in alpha:
            ans.add((nr, nc, alpha+lst[nr][nc]))
print(cnt)

