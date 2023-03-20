from collections import deque
N, M = map(int, input().split())
visited = [[0, -1] for _ in range(100001)]
q = deque()
q.append(N)
visited[N][1] = 0
visited[N][0] = 1
while q:
    num = q.popleft()
    for i in (num-1, num+1, num*2):
        if 0 <= i <= 10000:
            if visited[i][1] == -1:
                visited[i][0] = visited[num][0]
                visited[i][1] = visited[num][1] + 1
                q.append(i)
            elif visited[i][1] == visited[num][1] + 1:
                visited[i][0] += visited[num][0]

print(visited[M][1])
print(visited[M][0])

