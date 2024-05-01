T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    puzzle = [list(map(str, input())) for i in range(n)]
    puzzle_180 = list(map(list, zip(*puzzle)))

    ans = ''
    for i in range(n):
        for j in range(n-m+1):
            r = puzzle[i][j:j+m]
            c = puzzle_180[i][j:j+m]
            if r == r[::-1]:
                ans = r

            if c == c[::-1]:
                ans = c

    if ans:
        print(f'#{tc} {"".join(ans)}')




    # ans = ''
    # for i in range(n):
    #     for j in range(n-m+1):
    #         r = puzzle[i][j:m+j]
    #         if r == r[::-1]:
    #             ans = r
    # if ans:
    #     print(f'#{tc} {"".join(ans)}')
    # else:
    #     puzzle_90 = [[0] * n for _ in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             puzzle_90[i][j] = puzzle[j][i]
    #
    #     for i in range(n):
    #         for j in range(n - m + 1):
    #             r = puzzle_90[i][j:m + j]
    #             if r == r[::-1]:
    #                 ans = r
    #     print(f'#{tc} {"".join(ans)}')
