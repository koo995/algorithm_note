n = int(input())
costs = [ list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (i+1) for i in range(n)]
dp[0] = costs[0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + costs[i][0]
for i in range(1, n):
    l = len(costs[i])
    for j in range(1,l):
        dp[i][j] = (max(dp[i-1][j-1], dp[i-1][j]) if j!=(l-1) else dp[i-1][j-1])  + costs[i][j]
print(max(dp[-1]))

# 제일 끝 부분에 있는 녀석은 max비교로 넣을 것이 아니군