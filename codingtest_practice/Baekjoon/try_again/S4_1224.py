N = int(input())
switches = [0] + list(map(int, input().split()))

P = int(input())
students = [list(map(int, input().split())) for _ in range(P)]

for gender, num in students:
    if gender == 1:
        for i in range(1, N+1):
            if i % num == 0:
                if switches[i] == 0:
                    switches[i] = 1
                else:
                    switches[i] = 0
    elif gender == 2:
        for i in range(N//2 + 1):
            if i == 0 and switches[num] == 0:
                switches[num] = 1
            elif i == 0 and switches[num] == 1:
                switches[num] = 0
            elif i != 0 and num-i >= 1 and num + i <= N and switches[num-i] == switches[num+i]: 
                if switches[num-i] == 1:
                    switches[num-i] = switches[num+i] = 0
                else:
                    switches[num-i] = switches[num+i] = 1 
                
switches = switches[1:]
divide = N//20

if divide > 0:
    for i in range(divide):
        print(*switches[i*20: (i+1)*20])
    print(*switches[divide*20:])
else: 
    print(*switches)
    
