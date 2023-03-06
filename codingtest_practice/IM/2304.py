N = int(input())

height = [0] * 1001
max_idx = 0 
maxh = 0
for _ in range(N):
    L, H = map(int, input().split())
    height[L] = H
    if maxh < H:
        max_idx = L
        maxh = H

ans = 0
h = 0
for i in range(max_idx + 1):
    if height[i] < h:
        ans += h
    elif height[i] >= h:
        h = height[i]
        ans += h
l = 0
max_l = 0
for i in range(1000, max_idx, -1):
    if height[i] < l:
        ans += l
    elif height[i] >= l:
        l = height[i]
        ans += l

print(ans)
