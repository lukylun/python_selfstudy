"""
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
문자열 형식으로 숫자 number
제거할 수의 개수 k

가장 큰 숫자를 문자열 형태로 return
"""

def solution(number, k):
    answer = ''
    number = list(map(int, number))
    now_index = 0
    for i in range(len(number)-k):
        remains = number[now_index : now_index+k+1]
        max_value = -1
        max_index = 0

        for j, v in enumerate(remains):
            if v > max_value:
                max_value = v
                max_index = j
            if max_value == 9: break

        now_index += max_index + 1
        k -= max_index
        answer += str(max_value)
        print(answer, k)
    return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))