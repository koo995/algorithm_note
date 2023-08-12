n = int(input())
INF = int(1e6)
dp = [INF] * (1000001)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    if dp[i-1] != INF:
        dp[i] = dp[i-1] + 1 # 먼저 1을 뺀 녀석을 시작한다.
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])


# n이 1 이나 2 3인경우가 문제구나
# 그냥 3칸만 더 구하면 되지않나?
# 왜 틀린거지...? 
# 잠시만 dp[1]의 값은 뭐가 되야하지?
