N, L = map(int, input().split())
cnt = 0
road = 0
for _ in range(N):
    D, R, G = map(int, input().split())
    cnt += D - road
    road = D
    if cnt % (R+G) < R:
        cnt += R - (cnt % (R+G))

if road < L:
    cnt += L - road
print(cnt)
