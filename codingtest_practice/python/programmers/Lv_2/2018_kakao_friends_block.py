"""
2*2 형태로 4개가 붙어있으면 사라지면서 점수를 얻는 게임
블록이 지워지면 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 됨

위를 반복
지워지는 블록의 개수를 return
"""
dr = [0, 1, 1]
dc = [1, 0, 1]

import pprint
def combo(r, c, arr):
    char_set = set()

    for i in range(r-1):
        for j in range(c-1):
            chk = 0
            chk_set = set()
            if arr[i][j] != '':
                for d in range(3):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] == arr[i][j]:
                        chk += 1
                        chk_set.add((ni, nj))
                if chk == 3:
                    char_set.add((i, j))
                    for x, y in chk_set:
                        char_set.add((x, y))

    for a, b in char_set:
        arr[a][b] = ''

    return len(char_set), arr

def solution(m, n, board):
    answer = 0
    arr = [[[] for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            arr[i][j] = board[i][j]

    for i in range(100):
        cnt, arr = combo(m, n, arr)
        answer += cnt
        while True:
            move = 0
            for row in range(m-1):
                for col in range(n):
                    if arr[row][col] and arr[row+1][col] == '':
                        arr[row][col], arr[row+1][col] = arr[row+1][col], arr[row][col]
                        move = 1
            if move == 0:
                break
        if cnt == 0:
            break

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"] ))
print(solution(6,6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(2, 3,["AAB", "ABA"]))
print(solution(2, 3,["AAA","AAA"]))
print(solution(5,6,["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))
print(solution(4,4, ["ABCD", "BACE", "BCDD", "BCDD"]))