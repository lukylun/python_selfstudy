N = int(input())
lst = sorted(list(map(int, input().split())))

ans = 1
for num in lst:
    if ans < num:
        break

    ans += num

print(ans)