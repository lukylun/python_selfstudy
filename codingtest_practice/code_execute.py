T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    bread = [0] * 11112
    people = sorted(list(map(int, input().split())))

    ans = 0
    for i in range(11112):
        bread[i] += i // M * K

    for i in people:
        if bread[i] == 0:
            ans = 1
            break

        for j in range(i, 11112):
            bread[j] -= 1

    if ans == 1:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    answer = "Possible"
    for i in range(N):
        arrival = customers[i]
        if arrival // M * K - (i + 1) < 0:
            answer = "Impossible"
            break
    print(f"#{tc} {answer}")