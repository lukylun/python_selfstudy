T = int(input())
for tc in range(1, T + 1):
    ans = 1
    string = list(input())
    stack = []
    for s in string:
        if s == "{" or s == "(":
            stack.append(s)
        elif s == "}" or s == ")":
            if len(stack) == 0:
                ans = 0
                break
            else:
                a = stack.pop()
                if not ((a == "{" and s == "}") or (a == "(" and s == ")")):
                    ans = 0
                    break
    if len(stack) > 0:
        ans = 0
        
    print(f'#{tc} {ans}')
