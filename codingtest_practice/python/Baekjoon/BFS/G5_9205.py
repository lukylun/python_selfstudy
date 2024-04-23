from collections import deque

def bfs(home):
    global C
    q = deque()
    q.append(home)
    
    while q:
        r, c = q.popleft()
        print(r, c, festival[0][0], festival[0][1])
        if abs(r - festival[0][0]) + abs(c - festival[0][1]) <= 1000:
            return
        
        for i in range(C):
            x, y = c_arr[i]
            if not v[i] and ((abs(r - x) + abs(c - y)) <= 1000):
                q.append((x, y))
                v[i] = 1
    
    print("sad")
    return 
                
        
T = int(input())
# 편의점 개수
for i in range(T):
    C = int(input())
    home = []
    c_arr = []
    festival = []
    r, c = map(int, input().split())
    home.append((r, c))
    for c in range(C):
        r, c = map(int, input().split())
        c_arr.append((r, c))
    r, c = map(int, input().split())
    festival.append((r, c))
    v = [0 for _ in range(C)]
    
    bfs(home[0])
    
    
    