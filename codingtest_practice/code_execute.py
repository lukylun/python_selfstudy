import sys
from collections import deque

T = int(input())
q = deque()

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if lst[i] < max(lst):
                q.append(i)
            else:
                chr = q.popleft()
                if chr == M:
                    print(cnt)
                    break
                else:                    
                    cnt += 1