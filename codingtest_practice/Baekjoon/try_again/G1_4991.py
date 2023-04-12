M, N = map(int, input().split())
maps = []
dirty = []
furniture = []
start = []
for i in range(N):
    lst = list(input())
    for j in range(M):
        if lst[j] == '*':
            dirty.append((i, j))
        elif lst[j] == 'o':
            start.append((i, j))
        elif lst[j] == 'x':
            furniture.append((i, j))

    maps.append(lst)
