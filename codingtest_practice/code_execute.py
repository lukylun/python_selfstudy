from collections import deque

def bfs(V):
    q = deque()
    q.append(V)
    visited1[V] = 1
    while q:
        chr = q.popleft()
        print(chr, end=" ")
        for i in range(1, N + 1):
            if not visited1[i] and adj[chr][i]:
                q.append(i)
                visited1[i] = 1

def dfs(s):
    visited2[s] = 1
    print(s, end=" ")
    for i in range(1, N + 1):
        if not visited2[i] and adj[s][i]:
            dfs(i)

N, M, V = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    start, to = map(int, input().split())
    adj[start][to] = 1
    adj[to][start] = 1

visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)
dfs(V)
print()
bfs(V)