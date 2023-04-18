N = int(input())
lst = [list(input()) for _ in range(N)] # 알파벳
alphas = {} # 단어 알파벳: 숫자
temp = [] # 숫자 저장

for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j] in alphas:
            alphas[lst[i][j]] += 10 ** (len(lst[i])-j -1)
        else:
            alphas[lst[i][j]] = 10 ** (len(lst[i])-j-1)

for i in alphas.values():
    temp.append(i)

temp.sort(reverse=True)
sum = 0
num = 9
for i in temp:
    sum += num * i
    num -= 1

print(sum)