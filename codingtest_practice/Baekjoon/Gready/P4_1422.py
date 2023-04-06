'''
3 4
9
910
901
ans : 9910910901

4 5
823
9
8
7
ans: 9882388237
'''

K, N = map(int, input().split())
lst = [input() for _ in range(K)]

for i in range(K-1):
    idx = i
    num = lst[i]
    for j in range(i+1, K):
        if int(num + lst[j]) < int(lst[j] + num):
            idx = j
            num = lst[j]
    lst[i], lst[idx] = lst[idx], lst[i]

N -= len(lst)
nums = ''.join(lst)
lst.sort(key=lambda x:(len(x), x), reverse=True)
if N:
    if int(nums+lst[0]) < int(lst[0] + nums):
        nums = (lst[0] * N) + nums
    else:
        nums += (lst[0] * N)

print(nums)