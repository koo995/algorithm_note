n = int(input())
costs = [int(input()) if i!=0 else 0 for i in range(n+1)]
dp = [0] * (n+1)
if n == 1:
    print(costs[1])
elif n <= 2:
    dp[1] = costs[1]
    print(dp[1] + costs[2])
else:
    dp[1] = costs[1]
    dp[2] = dp[1] + costs[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + costs[i-1]) + costs[i]
    print(dp[-1])