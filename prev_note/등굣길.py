def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print("dp: ", dp)
    return dp[n][m]


print(solution(4, 3, [[2, 2]]))
# 마지막에 10000000007 나누는 것을 안해서 효율성테스트에서 틀렸군...
