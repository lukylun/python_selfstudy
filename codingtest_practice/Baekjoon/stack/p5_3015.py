# N = int(input())
# lst = list(int(input()) for _ in range(N))
# stack = []
# cnt = 1
# ans = 0
#
# for i in range(N):
#     # while이 먼저 와야함 -> if not stack이 처음으로 오면
#     # 첫 번째 시작부터 ans에 1을 추가하고 시작함.
#     # 스택이 비어있지 않고 마지막이 현재 들어올 수보다 작으면
#     while stack and stack[-1][0] < lst[i]:
#         # 스택에서 마지막 제거하고 ans에 더함
#         ans += stack.pop()[1]
#     # 스택이 비어있으면
#     if not stack:
#         # 스택에 쌓음(cnt = 1)
#         stack.append((lst[i], 1))
#         continue
#
#     # 스택이 비어있지 않고 마지막이 현재 들어올 수랑 같으면
#     if stack and stack[-1][0] == lst[i]:
#         # 스택에서 마지막 꺼내고 cnt를 갱신
#         cnt = stack.pop()[1]
#         # ans에 cnt 더함
#         ans += cnt
#
#         # 스택이 비어 있지 않으면
#         if stack:
#             # ans에 +1
#             ans += 1
#         # 스택에 cnt+1해서 쌓기
#         stack.append((lst[i], cnt + 1))
#
#     # 스택이 비어있지 않고 마지막보다 작으면
#     else:
#         stack.append((lst[i], 1))
#         ans += 1
#
# print(ans)
