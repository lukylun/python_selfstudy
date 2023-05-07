N = int(input())
switches = [0] + list(map(int, input().split()))

P = int(input())
students = [list(map(int, input().split())) for _ in range(P)]

for gender, num in students:
    # 남학생이면
    if gender == 1:
        # 1부터 N까지 배수인 것 체크
        for i in range(1, N+1):
            if i % num == 0:
                # 0이면 1로
                if switches[i] == 0:
                    switches[i] = 1
                # 1이면 0으로
                else:
                    switches[i] = 0
    
    # 여학생이면     
    elif gender == 2:
        # num부터 -1, +1 하나씩 같은지 체크
        for i in range(N//2 + 1):
            # num은 반대로 바꾸고
            if i == 0 and switches[num] == 0:
                switches[num] = 1
            elif i == 0 and switches[num] == 1:
                switches[num] = 0
            # num으로부터 i만큼 떨어진 값들이 같은지 체크, 유효성 검사까지
            elif i != 0 and num-i >= 1 and num + i <= N and switches[num-i] == switches[num+i]: 
                if switches[num-i] == 1:
                    switches[num-i] = switches[num+i] = 0
                else:
                    switches[num-i] = switches[num+i] = 1
            # 같지 않으면 탈출(더이상 확인할 필요 없음) => 좌우대칭이 아님
            else:
                break

# 출력하기 위해서 switches[0] 제거
switches = switches[1:]
# 20개씩 끊어서 출력하기 위해 몫을 구한다.
divide = N//20

# 몫이 0보다 크면
if divide > 0:
    # 20개씩 끊어서 출력하고
    for i in range(divide):
        print(*switches[i*20: (i+1)*20])
    # 나머지 출력
    print(*switches[divide*20:])

# 0보다 작으면 그대로 다 출력
else: 
    print(*switches)
