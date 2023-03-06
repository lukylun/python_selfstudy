lst = sorted([int(input()) for _ in range(9)])
total = sum(lst)
exclude = []
for i in range(8):
    for j in range(i+1, 9):
        if total - lst[i] - lst[j] == 100:
            exclude.append(lst[i])
            exclude.append(lst[j])
            break
    if exclude:
        break

for i in lst:
    if i not in exclude:
        print(i)
