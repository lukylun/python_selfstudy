import pprint
import sys
# 북동남서
dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(r, c, direct):
    cnt = 0

    while 1:
        chk = 1
        rooms[r][c] = 2
        cnt += 1

        while chk == 1:
            for i in ((direct+3)%4, (direct+2)%4, (direct+1)%4, direct):
                nr = r + dr[i][0]
                nc = c + dr[i][1]

                if not rooms[nr][nc]:
                    chk = 0
                    r, c, direct = nr, nc, i
                    break

            else:
                sr = r - dr[direct][0]
                sc = c - dr[direct][1]
                if rooms[sr][sc] == 1:
                    return cnt
                else:
                    r, c = sr, sc
    return -1

N, M = map(int, input().split())
s, e, d = map(int, input().split())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = bfs(s,e,d)
print(ans)



