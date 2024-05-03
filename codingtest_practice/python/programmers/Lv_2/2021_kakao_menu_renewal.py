"""
코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
손님들이 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성

최소 2명 이상의 손님으로 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함

orders 손님들이 주문한 단품메뉴들의 문자열 형식
course 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열

추가하게 될 코스요리의 구성을 문자열 배열로 return
"""

def combinations(k, c, comb, order, count):

    if len(comb) == c:
        count[comb] = count[comb] + 1 if comb in count else 1

    for i in range(k+1, len(order)):
        comb += order[i]
        combinations(i, c, comb, order, count)
        comb = comb[:-1]

    return

def combination(arr, c):
    result = []

    if c > len(arr):
        return result

    if c == 1:
        for i in arr:
            result.append([i])

    elif c > 1:
        for i in range(len(arr) - c + 1):
            for j in combination(arr[i+1:], c - 1):
                result.append([arr[i]] + j)

    return result


def combs(arr, c):
    result = []

    if c > len(arr):
        return result

    if c == 1:
        for i in arr:
            result.append([i])

    elif c > 1:
        for i in range(len(arr) - c + 1):
            for j in combs(arr[i+1:], c - 1):
                result.append([arr[i]] + j)

    return result


# from itertools import combinations

def solution(orders, course):
    answer = []
    orders = [sorted(list(menu)) for menu in orders]
    course_dict = {}

    for cnt in course:
        for order in orders:
            comb_list = list(map(''.join, combs(order, cnt)))

            for comb in comb_list:
                if comb not in course_dict:
                    course_dict[comb] = 1
                else:
                    course_dict[comb] += 1

    course_dict = sorted(course_dict.items(), key=lambda x: (len(x[0]), x[1]), reverse=True)
    len_letter = 10
    max_cnt = 0
    for alpha, cnt in course_dict:
        len_alpha = len(alpha)
        if cnt > 1 and len_letter >= len_alpha and cnt >= max_cnt:
            len_letter = len_alpha
            max_cnt = cnt
            answer.append(alpha)

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE"], [3]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))