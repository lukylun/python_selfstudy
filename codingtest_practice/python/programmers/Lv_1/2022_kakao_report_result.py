"""
신고 조건
1) 한 번에 한 명만 신고 가능
2) 횟수 제한 없음
3) 동일한 유저에 대한 신고 횟수는 1회로 처리
4) k번 이상 신고되면 게시판 이용 정지, 신고한 모든 유저에게 정지 사실을 메일로 전달

이용자의 ID가 담긴 배열 id_list
각 이용자가 신고한 이용자의 ID 정보가 담긴 report
정지 기준이 되는 신고 횟수 k

각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return
"""

def solution(id_list, report, k):
    answer = []
    report_cnt_dict = {}
    mail_user = {}
    for id in id_list:
        report_cnt_dict[id] = set()
        mail_user[id] = 0

    for rep in set(report):
        rep = rep.split(' ')
        report_cnt_dict[rep[1]].add(rep[0])

    for cnt in report_cnt_dict.values():
        if len(cnt) >= k:
            for i in cnt:
                mail_user[i] += 1

    for cnt in mail_user.values():
        answer.append(cnt)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))