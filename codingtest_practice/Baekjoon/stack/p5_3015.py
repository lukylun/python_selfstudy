N = int(input())
lst = list(int(input()) for _ in range(N))
stack = []
cnt = 1
ans = 0
for i in range(N):
    while stack and stack[-1][0] < lst[i]:
        ans += stack.pop()[cnt]
        print(ans, stack, 'while')
    if not stack:
        stack.append((lst[i], 1))
        continue

    if stack[-1][0] == lst[i]:
        cnt = stack.pop()[1]
        ans += cnt
        print(ans, cnt, stack, 'stack')

        if stack:
            ans += 1

        stack.append((lst[i], cnt+1))
        print(ans, stack, 'stack1')
    else:
        stack.append((lst[i], 1))
        ans += 1
        print(ans, stack, 'stack2')


print(ans)
#
# N = int(input())
# lst = list(int(input()) for _ in range(N))
# stack = []
# cnt = 1
# ans = 0
#
# for i in range(N):
#     # while이 먼저 와야함 -> if not stack이 처음으로 오면
#     # 첫 번째 시작부터 ans에 1을 추가하고 시작함.
#     while stack and stack[-1][0] < lst[i]:
#         ans += stack.pop()[1]
#
#     if not stack:
#         stack.append((lst[i], 1))
#         continue
#
#     if stack and stack[-1][0] == lst[i]:
#         cnt = stack.pop()[0]
#
#     else:
#         stack.append((lst[i], 1))
#         ans += 1
#
# print(ans)