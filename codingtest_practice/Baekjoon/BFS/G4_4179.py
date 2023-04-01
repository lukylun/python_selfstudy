from collections import deque
d = (0, 1), (0, -1), (1, 0), (-1, 0)

def bfs():
    global ans
    while q_J:
        ans += 1
        for _ in range(len(q_F)):
            fr, fc = q_F.popleft()
            for dr, dc in d:
                nfr = fr + dr
                nfc = fc + dc
                if 0 <= nfr < R and 0 <= nfc < C and arr[nfr][nfc] != '#':
                    arr[nfr][nfc] = "F"
                    q_F.append((nfr, nfc))
        for _ in range(len(q_J)):
            r, c = q_J.popleft()
            for dr, dc in d:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == '.':
                    arr[nr][nc] = "J"
                    q_J.append((nr, nc))

    return ans

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
q_J = deque()
q_F = deque()

ans = 0
r, c = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "J":
            if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                ans = 1
            r, c = i, j
        elif arr[i][j] == "F":
            q_F.append((i, j))

if ans != 1:
    q_J.append((r, c))
    print(bfs())
else:
    print(1)