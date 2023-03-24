import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
lst = list(input().rstrip().split())
stack = []

for i in range(N):
    while stack and stack[-1] < lst[i] and K > 0:
        K -= 1
        stack.pop()
    stack.append(lst[i])

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))
