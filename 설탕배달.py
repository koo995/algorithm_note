n = int(input())
INF = int(1e9)
dp = [INF] * (5001)
dp[3] = 1
dp[5] = 1
for i in range(6,n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
        
print(dp[n] if dp[n] < INF else -1)
