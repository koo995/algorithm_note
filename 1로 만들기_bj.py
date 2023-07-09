n = int(input())
dp = [0] * int(1e6 +1) # 메모리제한이 어짜피 128이니까 10^6까지 그냥 만들어 놔도 될듯
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, n+4):
    min_prev = dp[i-1]
    if i % 3 == 0:
        min_prev = min(min_prev, dp[int(i//3)])
    if i % 2 == 0:
        min_prev = min(min_prev, dp[int(i//2)])
    dp[i] = min_prev + 1

print(dp[n])

# n이 1 이나 2 3인경우가 문제구나
# 그냥 3칸만 더 구하면 되지않나?
# 왜 틀린거지...? 
# 잠시만 dp[1]의 값은 뭐가 되야하지?