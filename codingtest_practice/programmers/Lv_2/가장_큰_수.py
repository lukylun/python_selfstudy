def solution(numbers):
    answer = ''
    lst = list(map(str, numbers))
    
    lst.sort(key=lambda x: (x*4)[:4], reverse=True)
    
    answer = str(int("".join(lst)))

    return answer


print(solution([6, 67, 66, 65, 61, 10, 2]))