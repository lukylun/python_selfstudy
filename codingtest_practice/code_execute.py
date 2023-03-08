N, M, B = map(int, input().split())
maps = []
nums = set()
for _ in range(N):
    lst = list(map(int, input().split()))
    maps.append(lst)
    for i in range(M):
        nums.add(lst[i])

print(arr)