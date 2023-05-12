def solution(k, tangerine):
    answer = 0
    num_dict = {}

    for tan in tangerine:
        if tan in num_dict.keys():
            num_dict[tan] += 1
        else:
            num_dict[tan] = 1
    
    num_dict = sorted(num_dict.items(), key=lambda item:item[1], reverse=True)
    
    print(num_dict)
    return answer
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
solution(k, tangerine)