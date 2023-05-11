# 남동북서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def rotation(a, b):
    r, c = a, b
    global direction
    while True:
        nr = r + dr[direction]
        nc = c + dc[direction]
        # 유효성 검사, 방문 체크
        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
            # 값 바꾸고
            v[nr][nc] = maps[r][c]
            # 좌표 옮겨
            r, c = nr, nc
        # 더이상 못가면 방향 전환
        else:
            direction += 1
        # 4가 넘으면 탈출
        if direction >= 4:
            break
        
N, M, R = map(int, input().split())

# 배열
maps = [list(map(int, input().split())) for _ in range(N)]

# R번 회전
for _ in range(R):
    # 방문체크
    v = [[0] * M for _ in range(N)]
    # N, M 중 작은 수의 절반만 돌면 됨
    for n in range(min(N, M)//2):
        # global 변수
        direction = 0
        # 유효성 검사, 방문한 적 없는지 체크
        if 0 <= n < (min(N, M)//2) and not v[n][n]:
            rotation(n, n)
    maps = v

for _ in maps:
    print(*_)