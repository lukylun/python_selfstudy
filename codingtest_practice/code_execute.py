N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))

cnt = 1
end = lst[0][1]
for i in range(1, N):
    if end <= lst[i][0]:
        cnt += 1
        end = lst[i][1]

print(cnt)