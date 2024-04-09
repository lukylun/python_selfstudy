from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
  M, N, K = map(int, input().split())
  baechu = [[0] * M for _ in range(N)]
  
  q = deque()
  v = [[0] * (M+1) for _ in range(N+1)]
  for _ in range(K):
    a, b = map(int, input().split())
    baechu[b][a] = 1
    
  cnt = 0
  for r in range(N):
    for c in range(M):
      if baechu[r][c]:
        q.append([r,c])
        if not v[r][c]:
          v[r][c] = 1
          while q:
            i, j = q.popleft()
            for d in range(4):
              nr = i + dr[d]
              nc = j + dc[d]
              if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and baechu[nr][nc]:
                q.append([nr, nc])
                v[nr][nc] = 1
          cnt += 1
  
  print(cnt)
                
          
    