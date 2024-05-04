def solution():
    N = int(input())
    arrays = list(map(int, input().split()))
    reverse_arrays = arrays[::-1]
    i_dp = [0] * N
    d_dp = [0] * N
    i_dp[0] = 1
    d_dp[0] = 1
    
    for i in range(1, N):
        for j in range(i):
            if arrays[i] > arrays[j]:
                i_dp[i]  = max(i_dp[i], i_dp[j] + 1)
            else:
                i_dp[i] = max(i_dp[i], 1)
            if reverse_arrays[i] > reverse_arrays[j]:
                d_dp[i] = max(d_dp[i], d_dp[j] + 1)
            else:
                d_dp[i] = max(d_dp[i], 1)
    print(i_dp)
    print(d_dp[::-1])
    print(max((map(lambda t:t[0] + t[1], zip(i_dp, d_dp[::-1]))))-1)

solution()