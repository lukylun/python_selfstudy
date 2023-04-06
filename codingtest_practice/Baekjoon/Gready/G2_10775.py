G = int(input())
P = int(input())
cnt = 0
dp = [0] * (G+1)
num_dict = {i:i for i in range(G+1)}
for _ in range(P):
    plane = int(input())
    # 착륙할 수 없으면 반복문 종료시키기 위함
    dock = False
    for i in range(num_dict[plane], 0, -1):
        if dp[i] == 0:
            dp[i] = 1
            num_dict[plane] -= 1
            cnt += 1
            dock = True
            break
    if not dock:
        break
print(cnt)