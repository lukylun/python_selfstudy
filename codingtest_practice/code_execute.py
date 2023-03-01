# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     maps = [list(map(int, input().split())) for _ in range(N)]
#     vector = 1e11
#     if N != 2:
#         for i in range(N):
#             for j in range(i+1, N):
#                 for k in range(j+1, N):
#                     for l in range(k+1, N):
#                         # if i != j and i != k and i != l and j != k and j != l and k != l:
#                         a, b = maps[i]
#                         c, d = maps[j]
#                         e, f = maps[k]
#                         g, h = maps[l]
#                         x = (a - c) + (e - g)
#                         y = (b - d) + (f - h)
#                         vec = x * x + y * y
#                         if vec < vector:
#                             vector = vec
#     elif N == 2:
#         for i in range(N):
#             for j in range(N):
#                 if i != j:
#                     a, b = maps[i]
#                     c, d = maps[j]
#                     x = a - c
#                     y = b - d
#                     vec = x ** 2 + y ** 2
#                     vector = min(vector, vec)
#
#     print(f'#{tc} {vector}')


from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    num = [tuple(map(int, input().split())) for _ in range(n)]
    t1 = [i for i in range(n)]

    test = list(combinations(t1, n // 2))
    print(test)
    print(len(test),'-----')