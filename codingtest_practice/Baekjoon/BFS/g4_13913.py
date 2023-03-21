from collections import deque
N, M = map(int, input().split())
q = deque()
q.append(N)
visited = [-1 for _ in range(100001)]
visited[N] = 0

while q:
    num = q.popleft()

    if num == M:
        ans.ap