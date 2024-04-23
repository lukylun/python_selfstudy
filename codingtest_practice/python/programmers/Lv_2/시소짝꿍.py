
'''
조합의 특징
2C2 3C2 4C2 5C2 6C2의 규칙을 생각해보자
'''
def solution(weights):
    # dp: 처음 무게
    dp = [-1] * 1001
    # dp1: 2,3,4를 곱한 무게
    dp1 = [-1] * 4001
    # count
    cnt = 0
    # 무게 하나씩 돌려
    for i in weights:
        # dp 리스트에 +1 
        dp[i] += 1
        # cnt에 dp[i] 누적시키기
        cnt += dp[i]
        # 중복 cnt 나중에(2,3,4배 곱했을 때) 빼줘야함
        ol_cnt = dp[i]
        # 2,3,4배 곱해서 dp1에 쌓기
        for j in (2,3,4):
            dp1[i*j] += 1
            # 중복 cnt 값 빼고 cnt 하면 됨
            cnt += dp1[i*j] - ol_cnt

    return cnt