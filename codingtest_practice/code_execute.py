<<<<<<< HEAD
def backtracking(row, remain):
    
    # 1. 종료 조건
    if row == n and remain == 0:
        cnt += 1
        print(cnt)
        return
    # 2. 재귀 호출

    # 현재행 row에서 i번째 열에 퀸을 놓을 수 있는가?
    for i in range(n):
        can_place = True

        # 세로에 퀸이 있는지 검사
        for j in range(row):
            if board[j][i] == 1:
                can_place = False
                break

        # 대각선에 퀸이 있는지 검사
        for j in range(1, row + 1):
            # 좌상
            if row - j >= 0 and i - j >= 0 and board[row-j][i-j] == 1:
                can_place = False
                break                
            # 우상
            if row - j >= 0 and i + j < n and board[row - j][i + j] == 1:
                can_place = False
                break
    
        # 놓을 수 있는지 검사
        if can_place:
            # 놓을 수 있으면 현재 위치에 놓고 다음 위치로 이동
            board[row][i] = 1
            backtracking(row + 1, remain - 1)
            # 다시 되돌려놓고 진행할 수 있도록 해준다.
            board[row][i] = 0

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

# 경우의 수 구하기
    cnt = 0

 # 보드 만들기
    board = [[0] * n for _ in range(n)]
    backtracking(0, n)
    
    print(f'#{tc} {cnt}')



# # 스택 밖에 있을 시 우선 순위 (토큰의 우선순위)
# icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

# # 스택 안에 있을 시 우선 순위
# isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

# # infix => 중위표기식
# # n => 식의 길이
# def get_postfix(infix, n):
#     stack = []
#     postfix = "" # 결과로 출력할 후위 표기식

# # infix 안에 있는 문자들을 하나씩 떼와서 처리
#     for i in range(n):
#     # 피연산자인 경우
#         if '0' <= infix[i] <= '9':
#             postfix += infix[i]
#     # 연산자인 경우
#         else:
#         # 닫는 괄호가 나오는경우
#             if infix[i] == ')':
#             # 여는 괄호가 나올 때까지 pop해서 결과에 출력
#                 while True:
#                     chr = stack.pop()
#                     if chr == '(':
#                         break
#                     else:
#                         postfix += chr
#         # 다른 연산자가 나오는경우
#             else:
#             # 현재 토큰(연산자)의 우선순위보다
#             # stack[top]의 우선순위가 같거나 높으면 계속 pop
#                 while stack and icp[infix[i]] < isp[stack[-1]]:
#                     postfix += stack.pop()
#             # 그게 아니면 push
#                 stack.append(infix[i])
# # 남아있는 연산자를 출력
#     while stack:
#         postfix += stack.pop()
    
#     return postfix

# # 후위표기식 결과 계산
# def get_result(postfix):
#     stack = []

#     for i in postfix:
#     # 피연산자를 만나면 스택에 쌓기
#         if '0' <= i <= '9':
#             stack.append(int(i))
#     # 연산자를 만나면 피연산자를 두개 꺼내서 계산
#         else:
#         # 오른쪽이 먼저
#             right = stack.pop()
#         # 왼쪽이 먼저
#             left = stack.pop()

#         # 연산
#             if i == '+':
#                 stack.append(right+left)
#             elif i == '-':
#                 stack.append(left-right)
#             elif i == '*':
#                 stack.append(right*left)
#             elif i == '/':
#                 stack.append(left/right)
#         # 스택에 계산 결과 넣기(다음 연산을 위해서)
#     return stack.pop()


# string = "2+3*4/5"
# n = len(string)
# postfix = get_postfix(string, n)
# print(get_result(postfix))
=======
n = 5
maze = [list(input()) for _ in range(n)]
print(maze.find('2'))
>>>>>>> 6243f2069bf08903dca6fe2e7c8a37f7478013af
