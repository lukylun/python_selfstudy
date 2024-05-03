"""
n 양의 정수
k진수로 n을 바꿨을 때
소수가 몇 개인지 찾으려고함
소수의 조건
1) 0과 0사이에 소수가 존재 ex) 0110 -> 11이 소수
2) 소수 왼쪽이나 오른쪽에 0이 있을 때 ex) 110, 110 -> 11이 소수
3) 양쪽에 아무것도 없을 때 ex) 11 -> 소수
4) 소수에는 0이 포함되지 않아야 함
소수의 개수 return
"""

def solution(n, k):
    answer = 0
    num = ''

    while n > 0:
        remainder = n % k
        n //= k
        num += str(remainder)

    num = num[::-1]
    chk = ''
    for i in range(len(num)):
        if int(num[i]):
            chk += num[i]
        if int(num[i]) == 0 or i == len(num)-1:
            if chk != '' and chk != '1':
                cnt = 0
                for j in range(2, int(int(chk) ** 0.5 + 1)):
                    if int(chk) % j == 0:
                        cnt += 1
                if cnt == 0:
                    answer += 1

            chk = ''


    return answer

print(solution(437674, 3))
print(solution(110011, 10))