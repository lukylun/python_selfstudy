# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * (N+1) for _ in range(N)]
# dp[0][0] = lst[0][0]
# for i in range(1, N):
#     for j in range(len(lst[i])):
#         if j == 0:
#             dp[i][j] = dp[i-1][0] + lst[i][j]
#         elif j == len(lst[i]) - 1:
#             dp[i][j] = dp[i-1][j-1] + lst[i][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + lst[i][j]
#
# print(dp)


def dfs(x, lst, alpha):
    lst.append(x)
    for i in alpha:
        if len(x) != len(alpha):
            dfs(x + i, lst, alpha)
        else:
            x[:-1]


def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    ans = []
    for i in range(len(vowels)):
        dfs(vowels[i], ans, vowels)

    return ans.index(word) + 1

print(solution("AAAAE"))