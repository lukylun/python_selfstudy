"""
두 큐의 합을 같게 만드는 최소 횟수를 return
"""

from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    total = sum(q1) + sum(q2)
    half = total // 2
    q1_sum = sum(q1)

    while q1 and q2:
        if q1_sum < half:
            answer += 1
            num = q2.popleft()
            q1_sum += num
            q1.append(num)
        elif q1_sum > half:
            answer += 1
            q1_sum -= q1.popleft()

        else:
            return answer

    return -1


print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1,2,1,2], [1,10,1,2]))
print(solution([1,1,], [1,5]))