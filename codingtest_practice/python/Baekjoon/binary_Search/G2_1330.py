K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
start = 1
end = max(lst)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lst:
        if l >= mid:
            cnt += l // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid

    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 10

print(end)
