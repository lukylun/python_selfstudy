'''
3 5
1 1 1 1 2
3 9
1 2 3 4 1 1 1 1 3
'''

N, K = map(int, input().split())
lst = list(map(int, input().split()))

ans = set()
cnt = 0
idx = 0
result = 0
for i in range(K):
    if len(ans) != N:
        ans.add(lst[i])
    elif len(ans) == N:
        idx = i
        break

print(cnt)