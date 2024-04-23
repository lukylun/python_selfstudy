from pprint import pprint

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        x = i // n + 1
        rx = i % n + 1
        
        answer.append(max(x, rx))
    
            
    return answer


n = 4
left = 7
right = 14

print(solution(n, left, right))