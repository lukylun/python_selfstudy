from collections import deque

N = int(input())
maps = []
shark = []
fishes = []

shark_size = 2
for i in range(N):
    lst = map(int, input().split())
    for j in range(N):
        if lst[j] == 9:
            shark.append((i, j))
        elif 1 <= lst[j] <= 6:
            fishes.append((i, j, lst[j]))

