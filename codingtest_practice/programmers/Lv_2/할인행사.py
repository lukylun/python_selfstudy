def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        temp = {}
        for j in range(i, i+10):
            if discount[j] in temp.keys():
                temp[discount[j]] += 1
            else:
                temp[discount[j]] = 1
        
        res = 0
        for j in range(len(want)):
            if want[j] in temp.keys() and temp[want[j]] >= number[j] and not res:
                res = 0
            else:
                res = 1
        
        if res == 0:
            answer += 1
            
    return answer

def solution1(want, number, discount):
    ans = 0
    temp = {}
    for i in range(len(discount)-9):
        res = discount[i:i+10]
        flag = 0
        for j in range(len(want)):
            if res.count(want[j]) != number[j]:
                print(res)
                flag = 1
                break
        if flag == 0:
            ans += 1
    
    return ans

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution1(want, number, discount))