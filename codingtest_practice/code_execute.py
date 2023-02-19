l_stack = list(input())
r_stack = []
N = int(input())

for i in range(N):
    string = input()
    if string[0] == 'P':
        string = string.split()
        l_stack.append(string[-1])
    elif string == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif string == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif string == 'B' and l_stack:
        l_stack.pop()

print(''.join(l_stack)+''.join(r_stack[::-1]))
