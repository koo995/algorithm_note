def solution():
    N = int(input())
    arrays = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = 1
    
    for i in range(1, N):
        for j in range(i):
            # 감소하는 수열이라면
            if arrays[i] < arrays[j]:
                dp[i] = max(dp[i], dp[j] + 1)
            else:
                dp[i] = max(dp[i], 1)
    return max(dp)
    
print(solution())