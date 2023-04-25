N = int(input())
S = set()

for _ in range(N):
    lst = input().split()

    if lst[0] == 'add':
        S.add(int(lst[1]))
    elif lst[0] == 'remove':
        S.discard(int(lst[1]))
    elif lst[0] == 'check':
        if int(lst[1]) in S:
            print(1)
        else:
            print(0)
    elif lst[0] == 'toggle':
        if int(lst[1]) in S:
            S.discardint((lst[1]))
        else:
            S.add(int(lst[1]))
    elif lst[0] == 'all':
        for i in range(1, 21):
            S.add(i)
    elif lst[0] == 'empty':
        for i in range(1, 21):
            S = set()
