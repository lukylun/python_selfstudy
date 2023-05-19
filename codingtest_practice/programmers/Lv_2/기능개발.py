from collections import deque
def solution(progresses, speeds):
    answer = []
    
    # progresses가 0일 때까지 반복
    while len(progresses):
        # 한번 for문 돌려서 진행률 더하기
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0 
        # progresses[0]이 0이 넘으면
        if progresses and progresses[0] >= 100:
            # cnt +1 하고 idx하나씩 빼기
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
            # 다시 for문 돌려서 다음 idx가 100이 넘는지 검사
            for i in range(len(progresses)):
                # 넘으면 cnt 더하고 뽑기
                if progresses and progresses[0] >= 100:
                    cnt +=1
                    progresses.pop(0)
                    speeds.pop(0)
                # 없으면 탈출
                else:
                    break
        # cnt가 0보다 크면 answer에 append
        if cnt > 0:
            answer.append(cnt)
    return answer

    # 시간 복잡도 줄이기
    # time = 0
    # cnt = 0
    # while len(progresses):
    #     if (progresses[0] + speeds[0] * time) >= 100:
    #         progresses.pop(0)
    #         speeds.pop(0)
    #         cnt += 1
    #     else:
    #         if cnt > 0:
    #             answer.append(cnt)
    #         time += 1
    # answer.append(cnt)
