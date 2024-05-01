"""
조이스틱으로 알파벳 완성하기
맨 처음엔 A로만 이루어져 있음
조건 4방향 이동
1) 상: 다음 알파벳
2) 하: 이전 알파벳(A에서 이동하면 Z로)
3) 좌: 커서를 왼쪽으로 이동(첫번째에서 이동하면 마지막 위치로 이동)
4) 우: 커서를 오른쪽으로 이동(마지막에서 이동하면 처음 위치로 이동)

조작 횟수의 최솟값을 return
알파벳은 대문자로만 이루어져 있음
"""

def solution(name):
    answer = 0

    min_move = len(name) - 1
    for idx, i in enumerate(name):
        if i != "A":
            answer += min(ord("Z") - ord(i) + 1, ord(i) - ord("A"))

        maxA = idx + 1
        while maxA < len(name) and name[maxA] == "A":
            maxA += 1

        min_move = min(min_move, 2 * idx + len(name) - maxA, idx + 2 * (len(name) - maxA))

    answer += min_move

    return answer

print(solution("JAN"))
print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("JABBAAAZ"))