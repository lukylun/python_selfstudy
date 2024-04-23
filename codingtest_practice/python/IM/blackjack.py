N, M = map(int, input().split())
nums = list(map(int, input().split()))
lst = set()
for i in range(N):
    for j in range(N):
        if j != i:
            for k in range(N):
                if j != k and i != k:
                    if nums[i]+nums[j]+nums[k] <= M:
                        lst.add(nums[i]+nums[j]+nums[k])
print(max(lst))