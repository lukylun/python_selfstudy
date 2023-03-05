T = int(input())
for tc in range(T):
    lst = list(map(int, input().split()))
    N = lst[0]
    cnt = 0
    for i in range(len(lst) - 1):
        for j in range(1, len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                cnt += 1

    print(lst[0], cnt)