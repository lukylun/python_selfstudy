"""
모든 음식의 스코빌 지수를 K이상으로 만들기
가장 낮은 두 개의 음식을 섞어 새로운 음식으로 만듦
1) 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

모든 음식의 스코빌 지수가 K이상이 될 때까지 반복하여 섞는다.
음식의 스코빌 지수를 담은 배열 scoville
원하는 스코빌 지수 K
최소 횟수 return
"""
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        s_index = heapq.heappop(scoville)
        if s_index < K:
            min_s = heapq.heappop(scoville)
            heapq.heappush(scoville, s_index + 2 * min_s)
            answer += 1
        else:
            return answer

    if scoville[0] < K:
        return -1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))