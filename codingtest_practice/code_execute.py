N = int(input())

d = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][1]
        elif 1 <= j <= 8:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
        else:
            d[i][j] = d[i-1][8]

print(sum(d[N]) % 1000000000)

N = int(input())
d = [0] * N
d[0] = 9

for i in range(1, N):
    d[i] = d[i-1] * 2 - i

print(d[N-1])