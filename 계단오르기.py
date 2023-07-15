n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [0] * (n+1) # 최대 인덱스 n까지
if n <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, n): # 최대 인덱스 n-1까지 고려됨. 그러니까 index -1은 0의 값으로 가져가도 괜찮다?
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]) # starirs[i]을 마지막에 안넣어서 계속 틀렸군...
    print(dp[n-1])
    


# 아직 까지 명확하게 이해하는게 쉽지는 않다.
# 밟는다 안밟는다 2가지 경우가 모두 있는 경우는 어떤것이던지 상관없다라는 흐름이 쉽지가 않네...
# 왜 틀렸다고 나오는 것이지?
# 아하 n이 처음부터 1또는 2가 주어질 수 있구나...