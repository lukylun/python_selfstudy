N, L = map(int, input().split())
waters = sorted(list(map(int, input().split())))

cnt = 0
now = waters[0]
distance = 1
for water in waters[1:]:
    if water - now + distance <= L:
        distance += water-now
        now = water
    elif water - now + distance > L:
        cnt += 1
        distance = 1
        now = water

print(cnt+1)