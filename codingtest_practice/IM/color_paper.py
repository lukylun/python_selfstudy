N = int(input())
square = set()

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            square.add((a+i, b+j))

print(len(square))