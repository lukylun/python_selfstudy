S = input()
T = input()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
if T == S:
    print(1)
else:
    print(0)