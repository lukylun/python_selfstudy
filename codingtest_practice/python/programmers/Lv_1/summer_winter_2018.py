def solution(d, budget):
    cnt = 0

    d.sort()

    for money in d:
        if budget - money >= 0:
            cnt += 1
            budget -= money
        else:
            break

    return cnt

print(solution([2,2,3,3], 10))