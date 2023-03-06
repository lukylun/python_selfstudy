# 이동 방향
moves = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

# 킹의 위치(K), 돌의 위치(S), 움직이는 횟수(N)
K, S, N  = input().split()
sc, sr = S[0], int(S[1])
c, r = K[0], int(K[1])
for _ in range(int(N)):
    M = input()
    nc = ord(c) + moves[M][1]
    nr = r + moves[M][0]
    if ord('A') <= nc <= ord('H') and 1 <= nr <= 8 and (nc, nr) != (sc, sr):
        c = chr(nc)
        r = nr
        print(c, r)
    elif ord('A') <= nc <= ord('H') and 1 <= nr <= 8 and (nc, nr) == (sc, sr):
        nsc = sc + moves[M][1]
        nsr = sr + moves[M][0]
        if ord('A') <= nsc <= ord('H') and 1 <= nsr <= 8:
            sc = chr(nsc)
            sr = nsr
        else:
            continue
    
print(c, r)
print(sc, sr)