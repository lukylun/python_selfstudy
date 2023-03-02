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

<<<<<<< HEAD
    test = list(combinations(t1, n // 2))
    print(test)
    print(len(test),'-----')
=======
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    bread = [0] * 11112
    people = sorted(list(map(int, input().split())))

    ans = 0
    for i in range(11112):
        bread[i] += i // M * K

    for i in people:
        if bread[i] == 0:
            ans = 1
            break

        for j in range(i, 11112):
            bread[j] -= 1

    if ans == 1:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    answer = "Possible"
    for i in range(N):
        arrival = customers[i]
        if arrival // M * K - (i + 1) < 0:
            answer = "Impossible"
            break
    print(f"#{tc} {answer}")
>>>>>>> 23f01b129cfd8a5160c2800554ef2d0f3fee90d8
