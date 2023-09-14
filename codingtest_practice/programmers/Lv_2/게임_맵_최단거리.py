from collections import deque

def solution(maps):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    answer = 0
    q = deque()
    q.append([0, 0])
    v = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    v[0][0] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and maps[nr][nc] and v[nr][nc] >= 0:
                if v[nr][nc] == 0:
                    v[nr][nc] = v[r][c] + 1
                    q.append([nr, nc])
                elif v[nr][nc] >= v[r][c] + 1:
                    v[nr][nc] = v[r][c] + 1

    if v[-1][-1]:
        return v[-1][-1]
    else:
        return -1


