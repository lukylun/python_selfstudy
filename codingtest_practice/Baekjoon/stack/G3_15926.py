# 반례
# 5
# ()(()
# ans 4
# 정답은 2
# 12
# (()(()()(()(
# 정답 4

N = int(input())
lst = list(input())
stack = []
# stack으로 cnt 계산하고
# 이전에 계산했던 값과 괄호가 남았는지 확인하기 위해서
# 리스트 하나 더 생성
ans = []
# 괄호 합
cnt = 0
# 여는 괄호 카운트, 나중에 닫는 괄호일 때 stack에
# 여는 괄호가 있는지 count하기 위해서
open_cnt = 0
for i in range(N):
    if lst[i] == "(":
        stack.append(lst[i])
        # 여는 괄호 +1
        open_cnt += 1

    # 스택이 비어있고 닫는 괄호면
    elif stack and lst[i] == ")":
        while stack:
            # 여는 괄호 없으면
            if open_cnt == 0:
                # 그냥 닫는괄호 stack넣고 종료
                stack.append(lst[i])
                break
            # open_cnt가 0이 아니면 스택에서 하나 뺌
            num = stack.pop()
            # 그게 여는 괄호면 하고 종료
            if num == "(":
                # cnt +2 open_cnt -1
                cnt += 2
                open_cnt -= 1
                break
            # 여는 괄호가 아니면 cnt += num
            else:
                cnt += num
        # stack에 cnt 쌓아
        stack.append(cnt)
        # cnt 초기화
        cnt = 0

# print(stack)
n = 0
# 스택에 숫자 뿐 아니라 여는 괄호, 닫는 괄호가 있을 수 있음
for i in range(len(stack)):
    # 괄호가 아니면
    if stack[i] != "(" and stack[i] != ")":
        # n에 stack값 더해
        n += stack[i]
    # 아니면 n 초기화하고
    # ans에 n 쌓기
    else:
        ans.append(n)
        n = 0
# 마지막에 나온 n값도 추가
ans.append(n)

# max값 호출
print(max(ans))
