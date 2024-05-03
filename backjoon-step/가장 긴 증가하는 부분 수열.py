def solution():
    N = int(input())
    arrays = list(map(int, input().split()))
    pre_end = int(1e9)
    # 가장 긴 증가하는 수열들을 나타내는 인덱스를 활용해볼까?
    dp = [0] * N
    dp[0] = 1
    if N == 1:
        return 1
    else:
        for i in range(1, N):
            for j in range(i):
                if arrays[i] > arrays[j]:
                    # 이런식으로 간다면 2차 dp 가 필요한가?
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    # 작은 경우는 어떻게 해야하지?
                    dp[i] = max(dp[i], 1)
    return max(dp)


print(solution())
# 단순히 한단계 앞의 녀석의 포함여부를 비교하는 것으로는 무리가 있다.
# 그렇다면 그보다 더 앞의 녀석들을 비교해 나가야 할텐데? 그렇다면 이중 for문으로 확인을 해나가야할까? N이 1000인 이상 10만도 괜찮다.