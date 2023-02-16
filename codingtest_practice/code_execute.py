n = int(input())
postfix = input()
nums = [int(input()) for _ in range(n)]
stack = []
isp = {'+': 1, '-': 1, '*': 2, '/': 2}
string = [chr(ord('A') + i) for i in range(n)]
str_dict= dict(zip(string, nums))
print(str_dict)

for d in postfix:
    if "A" <= d <= "Z":
        stack.append(str_dict[d])
    else:
        r = stack.pop()
        l = stack.pop()

        if d == '+':
            stack.append(r + l)
        elif d == '-':
            stack.append(l - r)
        elif d == '*':
            stack.append(l * r)
        else:
            stack.append(l / r)
print('{:.2f}'.format(stack.pop()))