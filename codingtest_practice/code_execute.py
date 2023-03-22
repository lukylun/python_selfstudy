def solution(number, limit, power):
    ans = []
    for i in range(1, number + 1):
        cnt = []
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt.append(j)
            if i % j == 0 and i // j not in cnt:
                cnt.append(i // j)
        if len(cnt) > limit:
            ans.append(power)
        else:
            ans.append(len(cnt))

    return sum(ans)