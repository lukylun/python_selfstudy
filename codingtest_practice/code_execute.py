N = int(input()) # 빌딩 수
buildings = [int(input().rstrip()) for _ in range(N)]
stack = []
ans = 0

for building in buildings:
    while stack and stack[-1] < building:
        stack.pop()
    stack.append(building)
    ans += len(stack) - 1
    
print(ans)