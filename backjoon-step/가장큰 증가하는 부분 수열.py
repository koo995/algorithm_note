def solution():
    N = int(input())
    arrays = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = arrays[0]
    
    for i in range(1, N):
        for j in range(i):
            # 증가하는 수열이라면
            if arrays[i] > arrays[j]:
                dp[i] = max(dp[i], dp[j] + arrays[i])
            # 전까지 증가하다가 갑자기 감소할 수 있지
            else:
                dp[i] = max(dp[i], arrays[i])
    return max(dp)

print(solution())