T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]

    cnt = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                cnt += 1
                for k in range(1, N):
                    if j + k < N and omok[i][j + k] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            ans = 1
                            break
                    elif j + k < N and omok[i][j + k] == '.':
                        cnt = 0

                if cnt < 5:
                    cnt = 0

    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                cnt += 1
                for k in range(1, N):
                    if i + k < N and omok[i + k][j] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            ans = 1
                            break
                    elif i + k < N and omok[i + k][j] == '.':
                        cnt = 0

                if cnt < 5:
                    cnt = 0

    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                cnt += 1
                for k in range(1, N):
                    if i + k < N and j + k < N and omok[i + k][j + k] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            ans = 1
                            break
                    elif i + k < N and j + k < N and omok[i + k][j + k] == '.':
                        cnt = 0

                if cnt < 5:
                    cnt = 0

    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                cnt += 1
                for k in range(1, N):
                    if i + k < N and j - k < N and omok[i + k][j - k] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            ans = 1
                            break
                    elif i + k < N and j - k < N and omok[i + k][j - k] == '.':
                        cnt = 0

                if cnt < 5:
                    cnt = 0

    if ans == 0:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')