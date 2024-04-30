"""
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
N = 스테이지의 개수
stages = 사용자가 멈춰있는 스테이지의 번호의 배열
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
"""

def solution(N, stages):
    # ans = []
    # total = len(stages)
    # for stage in range(1, N+1):
    #     if total != 0:
    #         cnt = stages.count(stage)
    #         rate = cnt / total
    #         res = stage, rate
    #         total -= cnt
    #         ans.append(res)
    #     else:
    #         res = stage, 0
    #         ans.append(res)
    #
    # ans = sorted(ans, reverse=True, key=lambda x: x[1])
    # ans = [i[0] for i in ans]

    ans = []
    total = len(stages)
    stage_cnt = [0 for i in range(N)]
    for i in stages:
        if i <= N:
            stage_cnt[i-1] += 1

    for idx, stage in enumerate(stage_cnt):
        if total != 0:
            rate = stage / total
            total -= stage
            res = idx+1, rate
            ans.append(res)
        else:
            res = idx+1, 0
            ans.append(res)

    ans.sort(reverse=True, key=lambda x: x[1])
    ans = [i[0] for i in ans]

    return ans


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))