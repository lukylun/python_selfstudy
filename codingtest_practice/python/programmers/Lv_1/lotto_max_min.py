"""
6개 다 맞추면 1등
2개 맞추면 5등

일부가 지워짐 0으로 표기

순서와 상관없이 당첨 번호가 일치하면 맞힌 걸로 인정
당첨 가능한 최고 순위와 최저 순위를 차례로 배열에 담아서 return

lottos = 구매한 로또 번호를 담은 배열
win_nums = 당첨번호를 담은 배열

"""

def solution(lottos, win_nums):
    answer = []
    win_cnt = 0
    zero_cnt = 0

    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
        elif lotto in win_nums:
            win_cnt += 1

    answer.append(min(7 - win_cnt - zero_cnt, 6))
    answer.append(min(7 - win_cnt, 6))

    return answer


# def solution(lottos, win_nums):
#     win_count = 0
#     zero_count = 0
#     for lotto in lottos:
#         if lotto == 0:
#             zero_count += 1
#
#         else:
#             for win_num in win_nums:
#                 if lotto == win_num:
#                     win_count += 1
#
#     max_rank = min(7 - win_count - zero_count, 6)
#     min_rank = min(7 - win_count, 6)
#
#     return max_rank, min_rank


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))