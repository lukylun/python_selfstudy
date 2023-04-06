def solution(M, S, D):
    answer = 0
    maps = [[0] * len(M[0]) for _ in range(len(M))]
    maps[S[1]][S[0]] = 1

    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == 0 and j == 0:
                continue
            if M[i][j] == 1:
                maps[i][j] = 0
            else:
                maps[i][j] += maps[i - 1][j] + maps[i][j - 1]

    answer = maps[D[1]][D[0]]
    print(maps)
    return answer

M = [[0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0],[0,0,0,1,0,1,0,0],[0,1,1,0,0,1,0,0],[0,0,0,1,0,0,1,0],[0,0,0,0,0,0,0,1]]
S = [0, 0]
D = [6, 3]

print(solution(M, S, D))