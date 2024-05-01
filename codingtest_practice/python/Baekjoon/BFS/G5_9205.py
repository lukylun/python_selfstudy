from collections import deque

def bfs(s, e, N):
    q = deque()
    q.append((s, e))

    while q:
        s, e = q.popleft()

        if abs(s - festival[0]) + abs(e - festival[1]) <= 1000:
            return "happy"

        else:
            for i in range(N):
                r, c = cv[i]
                if abs(s - r) + abs(e - c) <= 1000 and not v[i]:
                    q.append((r, c))
                    v[i] = 1

    return "sad"


T = int(input())
for tc in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    cv = []
    beer = 1000
    for _ in range(N):
        x, y = map(int, input().split())
        cv.append((x, y))
    festival = list(map(int, input().split()))
    v = [0 for _ in range(N)]
    ans = bfs(home[0], home[1], N)

    print(ans)


# def bfs(home):
#     global C
#     q = deque()
#     q.append(home)
#
#     while q:
#         r, c = q.popleft()
#         print(r, c, festival[0][0], festival[0][1])
#         if abs(r - festival[0][0]) + abs(c - festival[0][1]) <= 1000:
#             return
#
#         for i in range(C):
#             x, y = c_arr[i]
#             if not v[i] and ((abs(r - x) + abs(c - y)) <= 1000):
#                 q.append((x, y))
#                 v[i] = 1
#
#     print("sad")
#     return
#
#
# T = int(input())
# # 편의점 개수
# for i in range(T):
#     C = int(input())
#     home = []
#     c_arr = []
#     festival = []
#     r, c = map(int, input().split())
#     home.append((r, c))
#     for c in range(C):
#         r, c = map(int, input().split())
#         c_arr.append((r, c))
#     r, c = map(int, input().split())
#     festival.append((r, c))
#     v = [0 for _ in range(C)]
#
#     bfs(home[0])
    

    