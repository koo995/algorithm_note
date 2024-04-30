def solution():
    N = int(input()) # 길이가 N인 계단수는 총 몇개가 있는지 찾는 것이다. N의 최대는 100이므로 최대 길이 100을 가지는 계단수는 몇개인지 구해야할지도
    dp = [[0] * 10 for _ in range(N+1)] # dp[i][j] 이것은 길이가 i 일때 제일 오른쪽이 j 인경우
    # 길이가 1인 경우는 초기화 하자
    for i in range(1, 10):
        dp[1][i] = 1
    # N이 1이라면 그냥 실행 안되고 끝나겠다.
    for n in range(2, N + 1):
        for i in range(0, 10):
            if i == 0:
                dp[n][0] = dp[n-1][1]
            elif 0 < i < 9:
                dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]
            else:
                dp[n][9] = dp[n-1][8]
   
    print(sum([dp[N][i] for i in range(10)]) % int(1e9))

solution()