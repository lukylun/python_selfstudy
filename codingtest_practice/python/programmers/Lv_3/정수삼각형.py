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