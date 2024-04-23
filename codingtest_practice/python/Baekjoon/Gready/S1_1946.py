T = int(input())
for _ in range(T):
    N = int(input())
    lst = sorted([list(map(int, input().split())) for _ in range(N)])

    max1 = 0
    may1 = 0
    max2 = 0
    may2 = 0
    ans = []
    for x, y in lst:
        if not ans:
            ans.append((x, y))
            if x > max1:
                max1 = x
                may1 = y
            if y > may2:
                max2 = x
                may2 = y
        else:
            if x > max1 and y > may2:
                pass
            elif x > max1 and y < may2:
                ans.append((x, y))
                max1 = x
                may2 = y
            elif x < max1 and y > may2:
                ans.append((x, y))
                max2 = x
                may2 = y

    print(len(ans))
