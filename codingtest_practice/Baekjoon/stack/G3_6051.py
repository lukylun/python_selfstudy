N = int(input())
stack = []
t_stack = [[]]

for i in range(N):
    lst = input().split()
    if len(lst) == 2:
        x = lst[0]
        y = int(lst[1])
        if x == 'a':
            stack.append(y)
            t_stack.append(stack[:])
        elif x == 't':
            stack = t_stack[y-1]
            t_stack.append(stack[:])
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        if stack:
            stack.pop()
        if stack:
            print(stack[-1])
            t_stack.append(stack[:])
        else:
            print(-1)
            t_stack.append(stack[:])
