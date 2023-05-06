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
        for i in range(num):
            if i == 0 and switches[num] == 0:
                switches[num] = 1
            elif i == 0 and switches[num] == 1:
                switches[num] = 0
            elif i != 0 and num-i >= 0 and (num+i) <= (N-1) and switches[num-i] == switches[num+i]:
                if switches[num-i] == 0:
                    switches[num-i] = switches[num+i] = 1
                else:
                    switches[num-i] = switches[num+i] = 0
            else:
                break

share = (N+1)// 20
rest = (N+1) % 20
for i in range(share):
    print(switches[(i*20+1): ((i+1)*20+1)])

if rest != 0:
    print(switches[(20*share + 1):])
