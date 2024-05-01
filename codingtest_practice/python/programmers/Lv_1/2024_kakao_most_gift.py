"""
다음 달에 누가 선물을 많이 받을지 예측

조건
1) 두 사람이 선물을 주고받은 기록이 있다면,
    이번 달까지 두 사람 사이에 더 많이 선물을 준 사람이 다음 달에 선물을 하나 받음.
2) 주고 받은 기록이 없거나 같으면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받음
3) 선물 지수 = 자신이 선물을 준 수 - 받은 선물의 수
4) 선물 지수도 같다면 다음 달에 선물을 주고 받지 않음

친구들의 이름을 담은 1차원 배열 friends
선물 기록 1차원 문자 배열 gifts
가장 많은 선물을 받는 친구가 받을 선물의 수 return
"""

def solution(friends, gifts):
    gift_record = [[0] * len(friends) for _ in range(len(friends))]
    gift_index = [0] * len(friends)
    most_gift = [0] * len(friends)

    for gift in gifts:
        A, B = gift.split(" ")
        gift_record[friends.index(A)][friends.index(B)] += 1

    for idx in range(len(friends)):
        gift_index[idx] += sum(gift_record[idx])
        for col in range(len(friends)):
            gift_index[idx] -= gift_record[col][idx]

    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            if gift_record[i][j] > gift_record[j][i]:
                most_gift[i] += 1
            elif gift_record[i][j] == gift_record[j][i]:
                if gift_index[i] > gift_index[j]:
                    most_gift[i] += 1
                elif gift_index[i] < gift_index[j]:
                    most_gift[j] += 1
            else:
                most_gift[j] += 1

    return max(most_gift)

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))