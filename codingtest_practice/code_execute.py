# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c):
    # 좌표 범위 유효한지 검사
    if r < 0 or c < 0 or r >= N or c >= N:
        return False
    # 해당 좌표에 집이 있으면
    if lst[r][c] == 1:
        global num
        num += 1
        # 방문했으니 리스트에서 집을 지워버림
        lst[r][c] = 0
        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 재귀로 계속 실행
            dfs(nr, nc)
        return True
    return False        



N = int(input())
lst = [list(map(int, input())) for _ in range(N)]
num = 0 # 집의 수
result = 0 # 단지의 수
stack = []
for r in range(N):
    for c in range(N):
        # 좌표에 집이 있으면 그 좌표에서 갈 수 있는 집은 다 탐색함
        if dfs(r,c) == 1:
            # 스택에 쌓아
            stack.append(num)
            # 단지 수 + 1
            result += 1
            # 집의 수 초기화
            num = 0
# 정렬
stack.sort()
print(result)
# 단지 수 하나씩 출력
for i in stack:
    print(i)