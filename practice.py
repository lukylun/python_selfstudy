n = int(input())
nums = [int(input()) for _ in range(n)]
stack = [0]
ans = ''
idx = 0 
for i in range(n):
    if i == 0:
        for j in range(1, nums[i]+1):
            stack.append(j)
            ans += '+'
        stack.pop()       
        ans += '-'

    elif nums[i] > stack[-1]:
        for j in range(nums[idx] + 1, nums[i] + 1):
            stack.append(j)
            ans += '+'
        stack.pop()
        idx = i
        ans += '-'  

    elif nums[i] == stack[-1]:
        stack.pop()
        ans += '-'

if stack == [0]:
    for k in ans:
        print(k)
else:
    print('NO')
    