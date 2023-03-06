T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))

    total = []
    for i in range(1<<N):
        diff = 0 
        for j in range(N):
            if i & (1<<j):
                diff += nums[j]
        
        if diff >= B:
            total.append(diff - B)
    
    print(f'#{tc} {min(total)}')