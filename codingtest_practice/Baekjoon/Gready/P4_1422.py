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

N -= K
nums = []
sort_lst = sorted(lst, key=lambda x:(len(x), x), reverse=True)
result = 0
if N:
    for l in range(K):
        if lst[l] == sort_lst[0] and result == 0:
            nums.append(sort_lst[0] * (N+1))
            result = 1
        else:
            nums.append(str(lst[l]))
    print(''.join(nums))
else:
    nums = ''.join(lst)
    print(nums)