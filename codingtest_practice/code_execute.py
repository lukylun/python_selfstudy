a = list(input())
b = list(input())
d = [0] * 1001

for i in range(len(a)):
    cnt = 0
    for j in range(len(b)):
        if cnt < d[j]:
            cnt = d[j]
        elif a[i] == b[j]:
            d[j] = cnt + 1

print(max(d))