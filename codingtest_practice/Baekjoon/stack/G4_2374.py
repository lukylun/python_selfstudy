N = int(input())
lst = [int(input()) for _ in range(N)]
stack = []

cnt = 0
for i in range(N):
    minV = 1e9
    while stack:
        if stack[-1] < lst[i]:
            if minV > stack[-1]:
                minV = stack.pop()
                cnt += lst[i] - minV
            else:
                stack.pop()
        else:
            stack.append(lst[i])
            break

    if not stack:
        stack.append(lst[i])

if stack:
    maxV = stack.pop()
    while stack:
        if maxV <= stack[-1]:
            cnt += stack[-1] - maxV
            maxV = stack.pop()
        else:
            break
print(cnt)