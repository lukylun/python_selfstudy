N = int(input())
lst = input().split()

for i in range(N-1):
    # idx, num 값을 저장해놓고
    idx = i
    num = lst[i]
    # for문 돌리면서 앞뒤 숫자 합친 크기를 비교
    for j in range(i+1, N):
        # 크면 idx, num 값 갱신
        # 선택정렬하고 같음
        # 1번부터 정렬시켜버려~
        if int(num + lst[j]) < int(lst[j] + num):
            idx = j
            num = lst[j]

    lst[i], lst[idx] = lst[idx], lst[i]

print(int(''.join(lst)))