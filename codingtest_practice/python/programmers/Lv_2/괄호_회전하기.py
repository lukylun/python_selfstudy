def solution(s):
    answer = 0
    
    
    for j in range(len(s)):
        stack = []
        for i in s:
            if stack:
                j = stack[-1]
                if (i == "]" and j == "[") or (i=="}" and j=="{") or (i==")" and j == "("):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if len(stack) == 0:
            answer += 1
        s = s[1:] + s[:1]

    return answer

s = "}]()[{"
print(solution(s))