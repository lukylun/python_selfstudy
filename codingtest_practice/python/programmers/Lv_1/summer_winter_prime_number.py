# def solution(nums):
#     ans = 0
#     for i in range(len(nums)-2):
#         for j in range(i+1, len(nums)-1):
#             for k in range(j+1, len(nums)):
#                 num = nums[i] + nums[j] + nums[k]
#                 chk = 0
#                 for prime in range(2, int(num**0.5 + 1)):
#                     if num % prime == 0:
#                         chk = 1
#                         break
#                 if chk == 0:
#                     ans += 1
#     return ans

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    num_list = [sum(c) for c in cb(nums, 3)]
    chk = 0

    for num in num_list:
        for prime in range(2, int(num ** 0.5 +1)):
            if num % prime == 0:
                chk = 1
                break

        if chk:
            chk = 0
            continue
        answer += 1
    return answer

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, int(cand ** 0.5 + 1)):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
