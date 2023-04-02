from collections import deque
d = (0, 1), (0, -1), (1, 0), (-1, 0)

def bfs():
    global ans, escape
    while q_J:
        ans += 1
        for _ in range(len(q_F)):
            fr, fc = q_F.popleft()
            for dr, dc in d:
                nfr = fr + dr
                nfc = fc + dc
                if 0 <= nfr < R and 0 <= nfc < C and arr[nfr][nfc] != '#' and arr[nfr][nfc] != "F":
                    arr[nfr][nfc] = "F"
                    q_F.append((nfr, nfc))
        for _ in range(len(q_J)):
            r, c = q_J.popleft()
            for dr, dc in d:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = "J"
                        q_J.append((nr, nc))
                else:
                    escape = 1
                    break
            if escape:
                break
        if escape:
            return ans

        if len(q_J) == 0:
            ans = 'IMPOSSIBLE'
            return ans
    return ans

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
q_J = deque()
q_F = deque()

ans = 0
escape = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "J":
            q_J.append((i, j))
        elif arr[i][j] == "F":
            q_F.append((i, j))

print(bfs())
