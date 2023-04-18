N = int(input())
K = int(input())
lst = sorted(list(map(int, input().split())))

temp = []
for i in range(N-1):
    temp.append(lst[i+1]-lst[i])

temp.sort()
if K >= N:
    print(0)
else:
    print(sum(temp[:N-K]))
# maxV = max(temp)
#
# result = []
# minV = 0
#
# cnt = 0
# for i in range(N-1):
#     if K > 1:
#         if cnt + lst[i+1] - lst[i] >= maxV:
#             minV += cnt
#             cnt = 0
#             K -= 1
#         elif cnt + lst[i+1] - lst[i] < maxV:
#             cnt += lst[i+1] - lst[i]
#
#     else:
#         cnt += lst[i+1] - lst[i]
#
#     if i == N - 2:
#         minV += cnt
#
#
# print(minV)
