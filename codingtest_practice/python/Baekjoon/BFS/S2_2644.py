from collections import deque

N = int(input())
s, e = map(int, input().split())
m = int(input())
cnt = -1

arr = [[] for _ in range(N+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

v = [0 for _ in range(N+1)]
v[s] = 1
q = deque()
q.append(s)

while q:
    start = q.popleft()

    for i in arr[start]:
        if i == e:
            cnt = v[start]
            break

        if not v[i]:
            q.append(i)
            v[i] += v[start] + 1

print(cnt)