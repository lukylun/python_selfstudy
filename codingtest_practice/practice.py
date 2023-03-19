def f(start, cnt):
    print(stack)
    if cnt == n//2:
        stack2.append(stack)
        return
    # print(stack2)


    for k in range(start, n):
        stack.append(k)
        f(start+1, cnt + 1)
        stack.pop()


import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


mi = 1000000000
stack = []
stack2 = []
f(0, 0)

print(stack2,'fffff')