import heapq
from queue import PriorityQueue

# q = PriorityQueue()
q = []

N = int(input())
maxV = 0
for i in range(N):
    a, b = map(int, input().split())
    heapq.heappush(q, (-b, a))
    maxV = max(a, maxV)

V = [0] * (maxV+1)
ans = 0
while q:
    x, y = heapq.heappop(q)
    for j in range(y, 0, -1):
        if not V[j]:
            V[j] = 1
            ans += x
            break

print(-ans)