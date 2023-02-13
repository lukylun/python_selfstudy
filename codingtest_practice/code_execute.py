string = input()
stack = []
answer = 0
cnt = 0 
for s in string:
    if s == "(" or s == "[":
        stack.append(s)
    elif s == ")" or s == "]":
        if len(stack) == 0:
            break
        if s == ")" and stack[-1] == "(":
            answer += 2
            stack.pop()