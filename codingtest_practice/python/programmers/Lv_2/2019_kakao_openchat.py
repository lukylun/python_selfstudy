"""
채팅방에 들어오고 나갈 때 닉네임 변경 가능
닉네임 변경하고 나면 기존 채팅방에 있던 닉네임도 전부 변경됨

최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return
"""

def solution(record):
    answer = []
    ans = []
    nickname = {}

    for rec in record:
        lst = rec.split(" ")
        if lst[0] != "Leave":
            nickname[lst[1]] = lst[2]
        if lst[0] != "Change":
            answer.append((lst[0], lst[1]))

    for state, id in answer:
        if state == "Enter":
            ans.append('{}님이 들어왔습니다.'.format(nickname[id]))
        else:
            ans.append('{}님이 나갔습니다.'.format(nickname[id]))

    return ans


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))