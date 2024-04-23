N, M = map(int, input().split())
L = int(input())
r = []
c = []
for _ in range(L):
    a, b = map(int, input().split())
    if a == 0:
        r.append(b)
    else:
        c.append(b)
r.sort()
c.sort()
max_r = 0
max_c = 0
for i in range(len(r)):
    if i == 0:
        max_r = r[i]
    else:
        if r[i] - r[i-1] > max_r:
            max_r = r[i] - r[i-1]
    if M - r[-1] > max_r:
        max_r = M - r[-1]


for i in range(len(c)):
    if i == 0:
        max_c = c[i]
    else:
        if c[i] - c[i-1] > max_c:
            max_c = c[i] - c[i-1]

    if N - c[-1] > max_c:
        max_c = N - c[-1]

if len(c) == 0:
    print(max_r * N)
elif len(r) == 0:
    print(max_c * M)
else:
    print(max_c * max_r)