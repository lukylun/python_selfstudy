"""
한 명 제외하고 모든 선수 완주
마라톤에 참여한 선수 배열 participant
완주한 선수들의 이름 배열 completion
완주못한 선수 이름 return
"""

def solution(participant, completion):
    player_dict = {}
    for player in participant:
        if player in player_dict:
            player_dict[player] += 1
        else:
            player_dict[player] = 1

    for player in completion:
        player_dict[player] -= 1

    for id, value in player_dict.items():
        if value:
            return id

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
