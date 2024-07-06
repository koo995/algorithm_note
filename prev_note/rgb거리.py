def solution():
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = costs[0]
    for i in range(1, n):
        for c in range(3):
            dp[i][c] = min(dp[i - 1][(c + 1) % 3], dp[i - 1][(c + 2) % 3]) + costs[i][c]
    print(min(dp[-1]))


def solution2():
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    print("costs: ", costs)
    dp = costs.copy()
    for i in range(1, n):
        for c in range(3):
            dp[i][c] = min(dp[i - 1][(c + 1) % 3], dp[i - 1][(c + 2) % 3]) + costs[i][c]
    print(min(dp[-1]))


solution2()
