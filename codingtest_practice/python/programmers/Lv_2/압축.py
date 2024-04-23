def solution(msg):
    answer = []
    alpha = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    res = ""
    
    len_m = len(msg)
    
    if len_m == 1:
        return [alpha.index(msg) + 1]
    
    else:
        m = msg[0]
        cnt = 0
        for i in range(1, len_m):
            m += msg[i]
            if m not in alpha:
                answer.append(alpha.index(m[:-1]) + 1)
                alpha.append(m)
                m = m[-1]
                cnt += 1
                
            
            if i == len_m - 1:
                answer.append(alpha.index(m) + 1)    
    return answer


print(solution("A"))