def solution(cacheSize, cities):
    answer = 0
    cache_list = []
    
    if cacheSize == 0:
        answer = 5 * len(cities)
    else:
        for city in cities:
            city = city.lower()
            if len(cache_list) < cacheSize and city not in cache_list:
                cache_list.append(city)
                answer += 5
            elif city in cache_list:
                answer += 1
                cache_list.remove(city)
                cache_list.append(city)
            elif len(cache_list) == cacheSize and city not in cache_list:
                cache_list.pop(0)
                cache_list.append(city)
                answer += 5
                    

    return answer


cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))

