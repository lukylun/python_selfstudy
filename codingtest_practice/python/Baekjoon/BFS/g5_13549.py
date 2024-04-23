from collections import deque
N, K = map(int, input().split())
q = deque()
q.append(N)
visited = [-1 for _ in range(100001)]
visited[N] = 0

while q:
    num = q.popleft()
    if num == K:
        print(visited[num])

    if 0 <= num -1 <= 100000 and visited[num-1] == -1:
        visited[num-1] = visited[num] + 1
        q.append(num-1)
    if 0 < num *2 <= 100000 and visited[num * 2] == -1:
        visited[num * 2] = visited[num]
        q.appendleft(num*2)
    if 0 <= num + 1 <= 100000 and visited[num+1] == -1:
        visited[num+1] = visited[num] + 1
        q.append(num+1)