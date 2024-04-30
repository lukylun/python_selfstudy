def binary_num(n, num):
    binary = ''
    while num:
        binary += str(num % 2)
        num = num // 2
    if len(binary) < n:
        binary += '0' * (n - len(binary))
    binary = binary[::-1]
    return binary

def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    ans = []
    for num in arr1:
        map1.append(binary_num(n, num))
    for num in arr2:
        map2.append(binary_num(n, num))

    for i in range(n):
        tmp = ''
        for j in range(n):
            if map1[i][j] == "1" or map2[i][j] == "1":
                tmp += "#"
            else:
                tmp += " "
        ans.append(tmp)
    return ans


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))