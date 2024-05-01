"""
자기 앞의 선수를 추월할 때 추월한 선수의 이름을 부름

players 선수들의 이름이 현재 등수 순서대로 담긴 배열
callings 해설진이 부른 이름을 담은 문자열 배열

경주가 끝났을 때 1등부터 등수 순서대로 배열에 담아 return
"""

def solution(players, callings):
    answer = []
    # id_rank = {id: idx+1 for idx, id in enumerate(players)}
    # rank_id = {idx+1: id for idx, id in enumerate(players)}
    #
    # for calling in callings:
    #     now_rank = id_rank[calling]
    #     former_player = rank_id[now_rank - 1]
    #
    #     rank_id[now_rank], rank_id[now_rank-1] = rank_id[now_rank-1], calling
    #     id_rank[calling], id_rank[former_player] = id_rank[former_player], now_rank
    #
    # for id in rank_id.values():
    #     answer.append(id)
    id_rank = {id: idx for idx, id in enumerate(players)}
    for calling in callings:
        now = id_rank[calling]
        id_rank[calling] -= 1
        id_rank[players[now-1]] += 1
        players[now], players[now-1] = players[now-1], players[now]

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))