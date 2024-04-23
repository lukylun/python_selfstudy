# 롤 케이크 길이
L = int(input())
# 방청객 수
N = int(input())

cake = [0] * (L+1)
max_idx = 0
max_val = 0
for i in range(1, N+1):
    P, K = map(int, input().split())
    for j in range(P, K+1):
        if K - P + 1 > max_val:
            max_val = K- P + 1
            max_idx = i
        if cake[j] == 0:
            cake[j] = i

ans = [0] * (N+1)
for i in cake:
    ans[i] += 1
ans = ans[1:]
print(max_idx)
print(ans.index(max(ans))+1)