'''
3 5
1 1 1 1 2
3 9
1 2 3 4 1 1 1 1 3
'''

N, K = map(int, input().split())
lst = list(map(int, input().split()))

ans = set()
num_dict = {}

for i in lst:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

cnt = 0
for i in lst:
    ans.add(i)
    num_dict[i] -= 1
    if len(ans) > N:
        for j in lst:
            if num_dict[i] == 0 and i in ans:
                ans.remove(i)
                break
        else:
            ans.remove
        cnt += 1
