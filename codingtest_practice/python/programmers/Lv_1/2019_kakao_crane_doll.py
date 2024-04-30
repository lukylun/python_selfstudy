"""
board = 인형이 담긴 배열
moves = 크레인을 작동시킨 위치가 담긴 배열
1~100 까지의 숫자는 다른 각기의 인형을 의미
같은 인형을 연속해서 뽑으면 사라짐
사라진 인형의 개수를 구해야함.
"""
def solution(board, moves):
    answer = 0
    basket = []

    for c in moves:
        for r in range(len(board)):
            if board[r][c-1] != 0:
                if basket and basket[-1] == board[r][c-1]:
                    answer += 2
                    basket.pop()
                    board[r][c-1] = 0
                    break
                else:
                    basket.append(board[r][c-1])
                    board[r][c-1] = 0
                    break

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))