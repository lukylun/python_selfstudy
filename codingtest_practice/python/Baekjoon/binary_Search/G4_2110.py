N, C = map(int, input().split())
lst = sorted([int(input()) for _ in range(N)])
ans = [0] * N

left = 0
right = N-1
if C % 2:
    ans.append(lst[left])
    ans.append(lst[right])
    C -= 2
    while True:
        mid = (left + right) // 2
        ans.append(lst[mid])
        C -= 1
        


