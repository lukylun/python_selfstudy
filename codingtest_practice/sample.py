N = int(input())
stack = []
t_stack = []

for i in range(N):
    lst = input().split()
    if len(lst) == 2:
        x = lst[0]
        y = lst[1]
        if x == 'a':
            stack.append(y)
            t_stack.append(stack[:])
            if stack:
                print(stack[-1])
            else:
                print(-1)

        elif x == 't':
            stack = t_stack[int(y) - 2]
            t_stack.append(stack[:])
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        x = lst[0]
        if x == 's':
            if stack:
                stack.pop()
                t_stack.append(stack[:])
                if stack:
                    print(stack[-1])
                else:
                    print(-1)
            else:
                t_stack.append(stack[:])
                if stack:
                    print(stack[-1])
                else:
                    print(-1)

print('')



