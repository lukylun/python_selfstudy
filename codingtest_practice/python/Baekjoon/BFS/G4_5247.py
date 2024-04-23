from collections import deque
import pprint
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    global escape

    while sg:
        for _ in range(len(fire)):
            fr, fc = fire.popleft()
            for d in range(4):
                fnr = fr + dr[d]
                fnc = fc + dc[d]
                if 0 <= fnr < N and 0 <= fnc < M and building[fnr][fnc] != "#" and building[fnr][fnc] != "*":
                    building[fnr][fnc] = "*"
                    fire.append((fnr, fnc))

        for _ in range(len(sg)):
            r, c = sg.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    if not v[nr][nc] and building[nr][nc] == ".":
                        building[nr][nc] = "@"
                        v[nr][nc] = v[r][c] + 1
                        sg.append((nr, nc))

                else:
                    escape = v[r][c]
                    break

            if escape:
                break

        if escape:
            break
    return

T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    v = [[0] * M for _ in range(N)]
    building = []
    sg = deque()
    fire = deque()
    escape = 0

    for i in range(N):
        lst = list(sys.stdin.readline().strip())
        building.append(lst)
        for j in range(M):
            if lst[j] == "@":
                sg.append((i, j))
                v[i][j] = 1
            elif lst[j] == "*":
                fire.append((i, j))

    bfs()
    if escape:
        print(escape)
    else:
        print("IMPOSSIBLE")


