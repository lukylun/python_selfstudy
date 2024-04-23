N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
stack = []

cnt = 0
for a, b in lst:
    while stack:
        if stack[-1][1] < b:
            stack.append((a,b))
            break
        elif stack[-1][1] > b:
            x, y = stack.pop()
            cnt += 1
            continue
        else:
            break
    if not stack and b != 0:
        stack.append((a,b))

if stack:
    cnt += len(stack)
print(cnt)