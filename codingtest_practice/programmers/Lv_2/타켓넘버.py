# from collections import deque
# def solution(numbers, target):
#     q = deque()
#     q.append((0, 0))
#     cnt = 0
#     while q:
#         ttl, idx = q.popleft()
#         if idx > len(numbers):
#             break
#         elif idx == len(numbers) and ttl == target:
#             cnt += 1
#         q.append((ttl + numbers[idx-1], idx + 1))
#         q.append((ttl - numbers[idx-1], idx + 1))
#
#
#     return cnt

from collections import deque

def solution(numbers, target):
    q = deque()
    q.append((0, 0))
    cnt = 0

    while q:
        ttl, idx = q.popleft()

        if idx > len(numbers):
            break

        elif idx == len(numbers) and ttl == target:
            cnt += 1

        print(idx-1)
        q.append((ttl + numbers[idx-1], idx + 1))
        q.append((ttl - numbers[idx-1], idx + 1))

    return cnt

print(solution([1,1,1,1,1],3))