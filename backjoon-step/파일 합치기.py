def solution():
    T = int(input())
    test_cases = [(int(input()), list(map(int, input().split()))) for _ in range(T)]
    for test_case in test_cases:
        K, files = test_case
        # 누적합을 구해준다.
        acc_sum = [0] * K
        acc_sum[0] = files[0]
        for i in range(1, K):
            acc_sum[i] = acc_sum[i - 1] + files[i]
        INF = int(1e9)
        dp = [[INF] * K for _ in range(K)]
        # 길이가 1인 녀석을 먼저 초기화 하자.
        for i in range(K):
            dp[i][i] = 0  # 2개이상 합한게 아닌 이상 1개짜리에는 비용이 존재하지 않는다. K는 최저 3이니까 1개짜리의 비용은 나오지 않을 것이다.
        # 이제부터 길이가 2이상인 녀석들을 탐색하자.
        for length in range(1, K):  # 2개 사이의 거리로 가야겠다.
            for i in range(K - length):  # i의 최대 범위를... K가 4이고 length 가 3이라면? i는 0만 가능
                j = i + length  # 이렇게 되면 j는 i보다 최소 1이상 크다.
                for m in range(i, j):  # m의 범위는 어떻게 되지? i <= m < j 의 범위면 충분하겠군
                    # 식을 어떻게 세울까? 하나 문제가 있다. 2개이상 합한게 아닌 이상 1개짜리에는 비용이 존재하지 않는다.
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j] + acc_sum[j] - (acc_sum[i - 1] if i - 1 >= 0 else 0))  # i가 0 인 경우 여기서 문제가 된다.
        print(dp[0][K - 1])


solution()
