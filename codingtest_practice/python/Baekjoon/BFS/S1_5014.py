"""
F층으로 이루어진 고층 건물
스타트링크가 있는 곳의 위치는 G층

강호의 위치: S층
엘리베이터 버튼은 2개 뿐,
U버튼은 위로 U층 가는 버튼
D버튼은 아래로 D층 가는 버튼

몇 번 눌러야 하는지 구하는 프로그램을 작성
G층에 갈 수 없다면 "use the stairs"
"""
from collections import deque

F, S, G, U, D = map(int, input().split())
q = deque()

v = [0] * (F + 1)
q.append(S)
v[S] = 1

while q:
    now = q.popleft()

    if now == G:
        print(v[now] - 1)
        exit()
    # 2방향
    for d in (now+U, now-D):
        if 1 <= d <= F and not v[d]:
            q.append(d)
            v[d] = v[now] + 1
print("use the stairs")