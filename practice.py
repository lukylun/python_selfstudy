# n = int(input())
# nums = list(map(int, input().split()))
# stack = []
# ans = [0 for _ in range(n)]
# idx = 0

# for i in range(n):
#     while stack:
#         if stack[-1][1] > nums[i]:
#             ans[i] = stack[-1][0] + 1

#             break
#         else:
#             stack.pop()
#     stack.append((i, nums[i]))

# print(ans)


n = int(input())
nums = list(map(int, input().split()))
stack = []
ans = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if stack[-1][1] > nums[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    
    stack.append((i, nums[i]))

print(' '.join(map(str, ans)))

# 0, 6
# 1, 9
