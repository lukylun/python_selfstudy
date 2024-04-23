import heapq

def solution(n, works):
	ans = 0
	heap = [] 	   
	for work in works:
		heapq.heappush(heap, (-work, work))
	
	
	for i in range(n):
		num = heapq.heappop(heap)[1]
		num -= 1
		heapq.heappush(heap, (-num, num))
	
	for h in heap:
		if h[1] > 0:
			ans += h[1] ** 2
	
	return ans

print(solution(3, [1,1]))