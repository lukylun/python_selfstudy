# from pprint import pprint
# from collections import deque

# # 방향 체크
# dr = [1, -1, 0, 0]
# dc = [0, 0, -1, 1]


# def bfs():
#     q = deque()
#     # 외부 공기부터 체크
#     # 안쪽 고립된 공기는 체크하지 않기 위해서
#     q.append((0, 0))
    
#     # 녹일 치즈 리스트
#     melt = []
#     while q:
#         r, c = q.popleft()
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
#                 # 방향체크
#                 v[nr][nc] = 1
#                 # 공기면 q에 추가
#                 if not cheeze[nr][nc]:
#                     q.append((nr, nc))
#                 # 치즈면 melt에 추가
#                 elif cheeze[nr][nc]:
#                     melt.append((nr, nc))
    
#     # 치즈 녹여            
#     for i, j in melt:
#         cheeze[i][j] = 0
    
#     return len(melt)

# N, M = map(int, input().split())

# # 치즈 리스트
# cheeze = []

# # 치즈 갯수
# cnt = 0
# for i in range(N):
#     lst = list(map(int, input().split()))
#     cheeze.append(lst)
#     # 치즈 갯수
#     cnt += sum(lst)

# # print(cnt)

# # 치즈 녹이는데 걸린 시간
# hours = 0
# # 치즈를 다 녹이기 직전에 녹인 치즈 갯수
# last = 0 
# while True:
#     # 방문체크
#     v = [[0] * M for _ in range(N)]
#     # 치즈 녹일 갯수
#     res = bfs()
#     # 총 치즈에서 녹일 치즈 갯수 빼줌
#     cnt -= res
#     # 1시간 추가
#     hours += 1
    
#     if cnt == 0:
#         last = res
#         break
    
# print(hours)
# print(last)


from collections import deque
import pprint
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    melt = []
    
    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
                v[nr][nc] = 1
                if not cheeze[nr][nc]:
                    q.append((nr, nc))
                else:
                    melt.append((nr, nc))
        
    for i, j in melt:
        cheeze[i][j] = 0
    
    return len(melt)
                

N, M = map(int, input().split())
cheeze = []
cnt = 0

for i in range(N):
    lst = list(map(int, sys.stdin.readline().strip()))
    cnt += sum(lst)
    cheeze.append(lst)
    
res = 0
hour = 0

while True:
    v = [[0] * M for _ in range(N)]
    
    last = bfs()
    cnt -= last
    hour += 1
    
    if cnt == 0:
        res = last
        break

print(hour)
print(res)