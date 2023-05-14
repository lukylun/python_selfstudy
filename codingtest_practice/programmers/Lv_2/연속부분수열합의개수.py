 
# 시간 줄일 방법? 고민       
def solution(elements):
    answer = 0
    temp = set(elements)
    temp.add(sum(elements))
    for p in range(2, len(elements)):
        for i in range(len(elements)):
            if i <= len(elements) - p:
                cnt = sum(elements[i:i+p])
                temps.add(cnt)
            else:
                cnt = sum(elements[i:]) + sum(elements[:(p-len(elements)+i)])
                temp.add(cnt)
    print(temp)
    return len(temp)

print(solution([7,9,1,1,4]))