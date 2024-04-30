"""
각 지표에서 두 유형 중 하나로 결정
1번 지표: R, T
2번 지표: C, F
3번 지표: J, M
4번 지표: A, N

n개의 질문
7개의 선택지
1번: 매우 비동의(3점)
2번: 비동의(2점)
3번: 약간 비동의(1점)
4번: 모르겠음
5번: 약간 동의(1점)
6번: 동의(2점)
7번: 매우 동의(3점)

유형의 점수가 같으면 사전 순으로 빠른 성격의 유형을 검사자의 성격 유형이라 판단

판단하는 지표를 담은 문자열 배열 survey
검사자가 선택한 선택지 정수 배열 choices

"""

def solution(survey, choices):
    total_score = {"R": 0, "T": 0, "C": 0, "F": 0,
             "J": 0, "M": 0, "A": 0, "N": 0}
    score = {7: 3, 6: 2, 5: 1, 4: 0, 3: 1, 2: 2, 1: 3}
    ch_type = ["RT", "CF", "JM", "AN"]
    answer = ''

    for i in range(len(survey)):
        if choices[i] in (1,2,3):
            total_score[survey[i][0]] += score[choices[i]]
        elif choices[i] in (5,6,7):
            total_score[survey[i][1]] += score[choices[i]]

    for i in range(len(ch_type)):
        if total_score[ch_type[i][0]] >= total_score[ch_type[i][1]]:
            answer += ch_type[i][0]
        else:
            answer += ch_type[i][1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5] ))
print(solution(["TR", "RT", "TR"], [7,1,3]))