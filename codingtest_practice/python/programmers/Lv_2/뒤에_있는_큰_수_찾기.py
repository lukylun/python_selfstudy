def solution(numbers):
    answer = []
    num_list = []
    for i in numbers[::-1]:
        while len(num_list) > 0:
            if num_list[-1] > i:
                answer.append(num_list[-1])
                num_list.append(i)
                break
            else:
                num_list.pop(-1)
        if len(num_list) == 0:
            num_list.append(i)
            answer.append(-1)
    return answer[::-1]

from heapq import heappop, heappush

def solution1(numbers):
    answer = [-1 for _ in range(len(numbers))]
    heap = [(numbers[0], 0)]
    for i, n in enumerate(numbers[1:]):
        while heap and heap[0][0] < n:
            _, idx = heappop(heap)
            answer[idx] = n
        heappush(heap, (n, i+1))
    return answer

print(solution([2, 2, 2, 2]))
print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))