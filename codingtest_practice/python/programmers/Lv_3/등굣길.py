"""
물에 잠기지 않은 지역을 통해 학교 갈거야
가로 m
세로 n
물이 잠긴 지역 좌표 배열 puddles

오른쪽과 아래로만 움직여 집에서 학교까지 갈 수 있는 최단 경로의 개수를
1,000,000,007로 나눈 나머지를 return
"""

d = [(0, 1), (1, 0)]

def solution(m, n, puddles):
    maps = [[0] * (m + 1) for _ in range(n + 1)]
    maps[1][1] = 1
    for i, j in puddles:
        maps[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if maps[i][j] == -1:
                maps[i][j] = 0
                continue

            maps[i][j] += maps[i-1][j] + maps[i][j-1]

    return maps[n][m] % 1000000007

def solution1(m, n, puddles):
    maps = [[0] * (m + 1) for _ in range(n + 1)]
    maps[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                continue

            c1 = maps[i][j-1]
            c2 = maps[i-1][j]
            if [j-1, i] in puddles:
                c1 = 0
            if [j, i-1] in puddles:
                c2 = 0

            maps[i][j] += c1 + c2

    return maps[n][m]


print(solution1(4, 3, [[2,2]]))