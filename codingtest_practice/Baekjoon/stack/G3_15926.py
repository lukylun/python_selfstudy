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
ans = []
cnt = 0
open_cnt = 0
for i in range(N):
    if lst[i] == "(":
        stack.append(lst[i])
        open_cnt += 1
        if cnt != 0:
            ans.append(cnt)
    elif stack and lst[i] == ")":
        while stack:
            if open_cnt == 0:
                stack.append(lst[i])
                break
            num = stack.pop()
            if num == "(":
                cnt += 2
                open_cnt -= 1
                break
            else:
                cnt += num
        stack.append(cnt)
        cnt = 0

n = 0
for i in range(len(stack)):
    if stack[i] != "(" and stack[i] != ")":
        n += stack[i]
    else:
        ans.append(n)
        n = 0
ans.append(n)

print(max(ans))
