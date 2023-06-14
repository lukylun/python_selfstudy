isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

s = list(input())
stack = []
postfix = ''
for i in s:
    if "A" <= i <= "Z":
        postfix += i
    else:
        while stack:
            chr = stack.pop()
            if chr != '(':
                postfix += chr
            else:
                break
        if stack and isp[stack[-1]] <= icp[i]: