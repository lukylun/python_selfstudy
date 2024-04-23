'''
n = 진법
t = 구할 숫자의 개수
m = 참가 인원
p = 튜브의 순서
'''

def solution(n, t, m, p):
    answer = '0'
    alpha = '0123456789ABCDEF'

    for i in range(1, m * t):
        res = ''

        while i > 0:
            remainder = i % n
            i = i // n
            
            res += alpha[remainder]
        answer += res[::-1]
    
    ans = ''
    for i in range(p-1, len(answer), m):
        ans += answer[i]

    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))

