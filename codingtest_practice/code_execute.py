# 방향 그래프일때
def dfs(s, V, adj):
    visited[s] = 1
    if len[adj[s]] > 0:
        for a in adj[s]:
            if visited[a] != 1:
                dfs(a, V, adj)
    else:
        return 99

# 무방향 그래프
def dfs_non(s, V):
    visited = [0] * (V + 1)
    stack = []
    i = s
    visited[i] = 1
    while True:
        for w in adj_list[i]:
            if visited[w] == 0:
                stack.append(w)
                i = w
                visited[w] = 1
                print(i)
                # ans.append(i)
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return visited

V = int(input())
n = int(input())
visited = [0] * (V + 1)
adj_list = [[] for _ in range(V + 1)]
for i in range(n):
    start, to = map(int, input().split())
    adj_list[start].append(to)
    adj_list[to].append(start)
print(dfs_non(1, V))

# print(9ans)
    


