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

def solution2():
    N = int(input())
    dp = {n: {i: 0 for i in range(10)} for n in range(N + 1)}
    # 길이가 1이 녀석 먼저 초기화
    for i in range(10):
        if i == 0:
            dp[1][i] = 0
            continue
        dp[1][i] = 1
    if N == 1:
        print(sum(dp[1][i] for i in range(10)))
    # 길이가 2 이상인 녀석들 초기화하자
    else:
        for n in range(2, N + 1):
            for i in range(10):
                dp[n][i] = (dp[n - 1][i - 1] if i - 1 >= 0 else 0) + (dp[n - 1][i + 1] if i + 1 < 10 else 0)
        print(sum(dp[N][i] for i in range(10)) % int(1e9))


solution2()