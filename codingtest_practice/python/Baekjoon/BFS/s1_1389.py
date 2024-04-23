from collections import deque

N, M = map(int, input().split())
arr = [[] * (N+1) for _ in range(M+1)]
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


for i in range(1, N + 1):
    q.append(i)
    cnt = 0
    while q:
        idx = q.popleft()
