def solution():
    A = input()
    B = input()
    dp = [[0] * len(A) for _ in range(len(B))]  # y축이 B에 관한 것이고 x 축이 A에 관한 것이다.
    max_value = -int(1e9)
    for y in range(len(B)):
        for x in range(len(A)):
            if B[y] == A[x] and (y == 0 or x == 0):
                dp[y][x] = 1
            elif B[y] == A[x]:
                dp[y][x] = dp[y - 1][x - 1] + 1
            else:
                dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])    
            max_value = max(max_value, dp[y][x])
    print(max_value)
solution()