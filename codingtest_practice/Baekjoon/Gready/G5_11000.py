import heapq
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
q = []
heapq.heappush(q, lst[0][1])

for i in range(1, N):
    if lst[i][0] < q[0]:
        heapq.heappush(q, lst[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, lst[i][1])

print(len(q))
# for i in lst:
#     q.append(i)
#
# cnt = 0
#
# while q:
#     a, b = q.popleft()
#     for i in range(len(q)-1):
#
#
# print(cnt)


# while q:
#     x, y =
