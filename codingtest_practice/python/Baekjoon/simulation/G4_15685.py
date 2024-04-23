# 동북서남
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


N = int(input())
maps = []
starts = []
generations =[]
for _ in range(N):
    x,y,d,g = map(int, input().split())
    maps.append((x,y))
    starts(d)
    generations(g)
