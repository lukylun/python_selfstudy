from collections import deque
import heapq
N, K = map(int, input().split())
jewelry = [list(map(int, input().split())) for _ in range(N)]
bags = sorted([int(input()) for _ in range(K)])

q = []
ans = 0

for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(q, -jewelry[0][1])
        heapq.heappop(jewelry)

    if q:
        ans += heapq.heappop(q)
    elif not jewelry:
        break

print(-ans)