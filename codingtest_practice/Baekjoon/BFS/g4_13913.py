                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             0from collections import deque
N, M = map(int, input().split())
q = deque()
q.append(N)
# 방문 체크
visited = [-1 for _ in range(100001)]
# 이전에 방문했던 좌표 담기
ex_posi = [0 for _ in range(100001)]
# 시작 방문좌표는 한번에 가니까 0
visited[N] = 0


while q:
    num = q.popleft()

    if num == M:
        print(visited[num])

    # +1, -1, *2일 때
    for i in (num-1, num+1, num*2):
        # 첫 방문이고 i가 유효범위면
        if 0 <= i <= 100000 and visited[i] == -1:
            q.append(i)
            # 이전의 좌표에서 이동횟수 +1
            visited[i] = visited[num] +1
            # 이전 방문좌표 기록
            ex_posi[i] = num

# 좌표출력하기 위해 좌표를 담을 리스트
ans = []
# 총 이동횟수
cnt = visited[M]
# 시작 index
idx = M
# cnt가 0일 때까지 계속 ans에 담는다
while cnt >= 0:
    ans.append(idx)
    cnt -= 1
    # index 갱신
    idx = ex_posi[idx]

# 출력
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=" ")