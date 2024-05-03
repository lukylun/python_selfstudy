"""
A번 참가자와 B번 참가자 몇번째 라운드에서 만나는지

N 게임 참가자 수
A 참가자 번호
B 경쟁자 번호

몇번째 라운지인지 return
부전승은 없음
"""
def solution(n, a, b):
    answer = 0

    while True:
        answer += 1

        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)

        if a == b:
            break

    return answer

print(solution(8, 4, 3))
print(solution(16, 1, 8))
