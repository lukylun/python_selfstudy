def dfs(start, adj):
    stack = [(start)]
    visited = [0] * (N + 1)
    visited[start] = 1

    while stack:
        n = stack.pop()
        print(n, end=' ')

        for i in adj[n]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                break

def bfs(start, adj):
    q = [(start)]
    visited = [0] * (N + 1)
    visited[start] = 1

    while q:
        n = q.pop(0)
        print(n, end=' ')

        for i in adj[n]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


# N: 정점 개수, M: 간선 개수, V: 탐색 시작할 정점 번호
N, M, V = map(int, input().split())
# 인접 리스트
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    # 양방향
    adj[s].append(e)
    adj[e].append(s)

# 정점 여러 개인 경우, 정점 번호 작은 것부터 방문
# 인접 리스트 내 정점들 정렬
for s in adj:
    s.sort()

dfs(V, adj)
print()
bfs(V, adj)