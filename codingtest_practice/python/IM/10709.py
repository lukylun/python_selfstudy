H, W = map(int, input().split())
lst = [list(input()) for _ in range(H)]
arr = [[0] * W for _ in range(H)]

for i in range(H):
    m = -1
    for j in range(W):
        if lst[i][j] == 'c':
            arr[i][j] = 0
            m = 0
        else:
            if m != -1:
                m += 1
                arr[i][j] = m
            else:
                arr[i][j] = m

for i in arr:
    print(' '.join(map(str, i)))
