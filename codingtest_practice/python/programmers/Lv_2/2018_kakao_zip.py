"""
LZW 압축
과정
1) 길이가 1인 모든 단어를 포함하도록 사전을 초기화
2) 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾는다
3) w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거
4) 입력에서 처리되지 않은 다음 글자가 남아있다면 c, w+c에 해당하는 단어를 사전에 등록한다.
5) 단계 2로 돌아간다.

주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.
"""

def solution(msg):
    answer = []
    alpha = {id: idx+1 for idx, id in enumerate(list(chr(i) for i in range(ord("A"), ord("Z")+1)))}
    next_num = len(alpha) + 1

    if len(msg) == 1:
        answer.append(alpha[msg])
        return answer

    now_letter = msg[0]

    for i in range(1, len(msg)):
        now_letter += msg[i]

        if now_letter not in alpha:
            alpha[now_letter] = next_num
            answer.append(alpha[now_letter[:-1]])
            next_num += 1
            now_letter = msg[i]

        if i == len(msg) - 1:
            answer.append(alpha[now_letter])

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
print(solution("A"))