bingo = [list(map(int, input().split())) for _ in range(5)]
called = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        num = called[i][j]
        for x in range(5):
            for y in range(5):
                if bingo[x][y] == num:
                    bingo[x][y] = 0
                    cnt += 1
                    break

        if cnt > 11:
            bin = cross_t = cross = 0
            bingo_t = list(zip(*bingo))
            for z in range(5):
                if bingo[z].count(0) == 5:
                    bin += 1
                if bingo_t[z].count(0) == 5:
                    bin += 1
                if bingo[z][z] == 0:
                    cross += 1
                if bingo[z][4-z] == 0:
                    cross_t += 1
            if cross == 5:
                bin += 1
            if cross_t == 5:
                bin += 1
            if bin >= 3:
                print(cnt)
                exit(0)

