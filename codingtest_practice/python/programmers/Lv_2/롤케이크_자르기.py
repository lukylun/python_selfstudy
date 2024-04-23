

def solution(topping):
    answer = 0
    big_set = set()

    if len(topping) % 2:
        return 0

    for i in range(len(topping)):
        big_set.add(topping[i])
        sm_set = set(topping[i+1:])
        if len(big_set) == len(sm_set):
            answer += 1

    return answer

print(solution([1, 2, 3, 1, 4]))
