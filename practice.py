n, m = map(int, input().split())
nums = list(map(int, input().split()))


# for i in range(m):
#     total = 0 
#     a, b = map(int, input().split())
#     for j in range(a-1, b):
#         total += nums[j]
#     print(total)


total_tmp = [0]
total = 0
for i in nums:
    total += i
    total_tmp.append(total)

for i in range(m):
    a, b = map(int, input().split())

    print(total_tmp[b] - total_tmp[a-1])