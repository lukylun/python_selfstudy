from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(M, S, D):
    ans = 0

    q = deque()
    q.append(S)
    v = [[0] * len(M[0]) for _ in range(len(M))]
    while q:
        r, c = q.leftpop()
        if r == D[0] and c == D[1]:
            break
        else:
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < len(M) and 0 <= nc < len(M[0]) and not v[nr][nc] and not M[nr][nc]:
                    q.append((nr, nc))
                    v[nr][nc] = v[r][c] + 1
   
    if v[D[0]][D[1]] != 0:
        ans = v[D[0][D[1]]
    else:
        ans = -1
    
    return ans

M = [[0, 0, 0], [0,1,0],[0,0,0]]
S = [0,0]
D = [2,2]
print(solution(M,S,D))