'''
3 5
1 1 1 1 2
3 9
1 2 3 4 1 1 1 1 3
'''

N, K = map(int, input().split())
lst = list(map(int, input().split()))

ans = []
cnt = 0
for i in range(K):
    if lst[i] in ans:
        continue
    elif len(ans) != N:
        ans.append(lst[i])
        continue
    
    idx = 0
    num = 0
    for an in ans:
        if an not in lst[i:]:
            num = an
            break
        elif lst[i:].index(an) > idx:
            idx = lst[i:].index(an)
            num = an
        
    ans[ans.index(num)] = lst[i]
    cnt += 1

print(cnt)