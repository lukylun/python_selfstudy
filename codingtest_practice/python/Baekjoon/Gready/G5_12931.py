N = int(input())
A = [0] * N
B = list(map(int, input().split()))

cnt = 0
temp = [0] * N
maxV = 0
for i in range(N):
    while B[i] > 0:
        if B[i] > 1 and B[i] % 2:
            B[i] -= 1
            cnt += 1
        elif B[i] > 1 and B[i] % 2 == 0:
            temp[i] += 1
            B[i] //= 2
        elif B[i] == 1:
            cnt += 1
            B[i] = 0
        else:
            break
    
print(cnt+max(temp))