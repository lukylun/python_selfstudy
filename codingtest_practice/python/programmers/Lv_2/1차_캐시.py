"""
DB캐시를 적용할 때 캐시 크게아 따른 실행시간 측정 프로그램을 작성
캐시 크기 cacheSize
도시이름 배열 cities
도시이름은 대소문자 구분하지 않음

입력된 도시이름 배열을 순서대로 처리할 때 총 실행시간을 출력
조건
1) LRU 알고리즘
2) cache hit일 경우 실행시간은 1
3) cache miss일 경우 실행시간 5

"""

def solution(cacheSize, cities):
    answer = 0
    stack = []

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city not in stack:
            if len(stack) < cacheSize:
                stack.append(city)
            else:
                stack.pop(0)
                stack.append(city)

            answer += 5

        else:
            answer += 1
            idx = stack.index(city)
            stack.pop(idx)
            stack.append(city)

    return answer

# def solution(cacheSize, cities):
#     answer = 0
#     cache_list = []
#
#     if cacheSize == 0:
#         answer = 5 * len(cities)
#     else:
#         for city in cities:
#             city = city.lower()
#             if len(cache_list) < cacheSize and city not in cache_list:
#                 cache_list.append(city)
#                 answer += 5
#             elif city in cache_list:
#                 answer += 1
#                 cache_list.remove(city)
#                 cache_list.append(city)
#             elif len(cache_list) == cacheSize and city not in cache_list:
#                 cache_list.pop(0)
#                 cache_list.append(city)
#                 answer += 5
#
#
#     return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
