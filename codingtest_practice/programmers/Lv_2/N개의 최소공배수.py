def solution(arr):
    answer = 0
    max_num = max(arr)
    idx = 1
    result = 0 
    while True:
        mul_num = max_num * idx
        for num in arr:
            if (mul_num % num) != 0:
                result = 1
        
        if result == 0:
            answer = mul_num
            break
        elif result == 1:
            result = 0
            idx += 1
            
    return answer

arr= [1,2,3]
print(solution(arr))