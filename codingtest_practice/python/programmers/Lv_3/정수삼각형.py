"""
삼각형 꼭대기에서 바닥까지 이어지는 경로 중
거쳐간 숫자의 합이 가장 큰 경우 찾기

삼각형의 정보가 담긴 배열 triangle
거쳐간 숫자의 합 최대
"""

# 더 오래 걸림
def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    dp[0] = triangle[0]

    for i in range(1, len(triangle)):
        tri = triangle[i]
        for t in range(len(tri)):
            if t == 0:
                dp[i].append(tri[t] + dp[i-1][t])
            elif 0 < t < len(tri) - 1:
                dp[i].append(max(tri[t] + dp[i-1][t], tri[t] + dp[i-1][t-1]))
            elif t == len(tri) - 1:
                dp[i].append(tri[t] + dp[i-1][t-1])

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


# 시간이 더 적게걸림
def solution(triangle):
    # 첫번째 idx
    dp = triangle[0]
    # 1번 idx부터 반복문
    for tri in triangle[1:]:
        # dp를 갱신하기 위해
        # dp1을 생성하고 계산값을 담아둔다
        dp1 = []
        for t in range(len(tri)):
            # 0이면 더하고 그대로 저장, 비교할 필요 없음.
            if t == 0:
                dp1.append(dp[t] + tri[t])
            # 처음과 끝이 아니면, 비교해서 max값 저장
            elif 0 < t < len(tri) - 1:
                dp1.append(max(dp[t] + tri[t], dp[t-1] + tri[t]))
            # 마지막도 더하고 그대로 저장
            elif t == len(tri) - 1:
                dp1.append(dp[t-1] + tri[t])
        # dp, dp1 바꾸기
        dp = dp1

    return max(dp)