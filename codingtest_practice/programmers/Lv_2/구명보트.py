def solution(people, limit):
    people.sort()
    cnt = 0
    
    idx = 0
    max_idx = len(people) - 1
    
    while idx <= max_idx:
        if people[idx] + people[max_idx] > limit:
            cnt += 1
            max_idx -= 1
        else:
            cnt += 1
            idx += 1
            max_idx -= 1
    return cnt