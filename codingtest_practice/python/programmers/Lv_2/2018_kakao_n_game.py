"""
2진법에서 16진법까지 모든 진법으로 게임을 진행
순서대로 1개의 숫자만 말해야함 (8을 이진수로 하면 1000 -> 1, 0, 0, 0)
진법 n
미리 구할 숫자의 개수: t
게임에 참가하는 인원: m
튜브의 순서: p

튜브가 말해야하는 숫자 t개를 공백없이 차례로 문자열으로 return
"""

def solution(n, t, m, p):
    answer = ''
    alpha = '0123456789ABCDEF'

    ttl = '0'
    for i in range(1, m * t):
        res = ''
        num = i
        while num > 0:
            remainder = num % n
            num //= n
            res += alpha[remainder]

        ttl += res[::-1]

    for i in range(p-1, len(ttl), m):
        answer += ttl[i]

    return answer[:t]

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))