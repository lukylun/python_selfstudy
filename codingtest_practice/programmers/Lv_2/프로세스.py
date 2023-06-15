from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    
    for i,v in enumerate(priorities):
        q.append((i,v))
    
    priorities.sort(reverse=True)
    cnt = 1
    idx = 0
    
    while q:
        i, v = q.popleft()
        print(i, v)
        if priorities[idx] == v:
            if i == location:
                break
            else:
                cnt += 1
                idx += 1
        else:
            q.append((i,v))
            
    return cnt

priorities = [2, 1, 3, 2]	
print(solution(priorities, 2))