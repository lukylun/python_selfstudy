def perm(arr, n):
    
    result = []
    
    if n == 0:
        return [[]]
    
    for i, e in enumerate(arr):
        for p in perm(arr[:i] + arr[i+1:], n-1):
            result += [[e] + p]
    
    return result

def solution(k, dungeons):
    answer = -1
    
    arr = perm(dungeons, len(dungeons))
    
    for i in arr:
        a = k
        cnt = 0
        for j in range(len(i)):
            if a >= i[j][0]:
                a -= i[j][1]    
                cnt += 1
                continue
            else:
                break
        
        if cnt > answer:
            answer = cnt

    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))