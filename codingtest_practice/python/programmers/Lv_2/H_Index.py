def solution(citations):
    answer = 0
    # 내가 푼 풀이
    # num_dict = {}
    
    # for citation in citations:
    #     if citation in num_dict.keys():
    #         num_dict[citation] += 1
    #     else:
    #         num_dict[citation] = 1
    
    # cnt = 0
    # for i in range(max(citations), -1, -1):
    #     if i in num_dict.keys():
    #         cnt += num_dict[i]
    #     if cnt >= i and len(citations) - cnt <= i:
    #         answer = i
    #         break

    # 간단한 풀이
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([5,6,7]))