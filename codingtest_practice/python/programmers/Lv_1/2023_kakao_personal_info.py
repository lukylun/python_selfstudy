"""
개인정보 n개
유효기간 지나면 폐기

조건
1) 모든 달은 28일까지 있다고 가정

오늘 날짜를 의미하는 문자열 today
약관의 유효기간을 담은 1차원 문자열 배열 terms
개인정보를 담은 문자열 배열 privacies

파기해야할 개인정보의 번호를 오름차순으로 정수 배열에 담아 return
"""

def solution(today, terms, privacies):
    answer = []
    new_term = {}
    for term in terms:
        term = term.split(" ")
        new_term[term[0]] = int(term[1])

    privacy_split = []
    for privacy in privacies:
        privacy = privacy.split(" ")
        privacy[0] = privacy[0].split(".")
        add_month = int(privacy[0][1]) + int(new_term[privacy[1]])
        if add_month >= 13:
            y = (add_month-1) // 12
            m = (add_month-(y*12)) % 13
            privacy[0][0] = str(int(privacy[0][0]) + y)
            privacy[0][1] = str(m).rjust(2, "0")

        else:
            privacy[0][1] = str(add_month).rjust(2, "0")
        privacy_split.append(".".join(privacy[0]))

    for idx, privacy in enumerate(privacy_split):
        if today >= privacy:
            answer.append(idx+1)

    return answer

print(solution("2009.12.28", ["A 13"], ["2008.11.03 A"]))
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))