# for i in range(n-1, -1, -1):
#     for j in range(0, i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]

# 카운팅 정렬
# n = int(input())
# arr = list(map(int, input().split()))
# cnt = [0 for _ in range(n)]
# ans = [0 for _ in range(n)]

# for i in arr:
#     cnt[i] += 1

# for i in range(1, len(cnt)):
#     cnt[i] += cnt[i-1]

# for i in arr:
#     cnt[i] -= 1
#     ans[cnt[i]] = i

# print(ans)

# baby-gin
n = 123457
c = [0] * 12  # i+2까지 가야함
for i in range(6):
    c[n % 10] += 1
    n //= 10

i = 0
tri = run = 0

while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >=1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print('baby gin')
else:
    print(0)