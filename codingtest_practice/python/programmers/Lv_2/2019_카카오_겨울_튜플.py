def solution(S):
    answer = []
    
    answer = S[:-2].replace("{",'').replace(',',' ').split("}")
    
    for i, v in enumerate(answer):
        answer[i] = v.split()
    
    answer = sorted(answer, key=lambda x:len(x))
    result = []
    for i in answer:
        for j in result:
            i.remove(j)
        result.append(i[0])
    
    return [int(_) for _ in result]


S = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(S))