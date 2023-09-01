# 단순히 제일 작은 음수를 제거한다는게 의미가 있을까?
# 메모리 초과가 발생...


import copy

n = int(input())
arr = list(map(int,input().split()))
dp = [[0] * n for _ in range(2)] # dp[0]은 특정원소 제거 안한 것 dp[1]은 제거한 것 (n,2)보다 (2,n)이 최대를구하는 식이 더 이쁠려나
dp[0][0] = arr[0]  # 처음 녀석이 음수 일 수 있지만 반드시 하나는 선택해야 한다.
# 이제부터 dp시작.
if n == 1:
    print(arr[0])
else:
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1]+arr[i])
    print(max(max(dp[0]), max(dp[1])))


# 계속 어디서 틀리는 것일까