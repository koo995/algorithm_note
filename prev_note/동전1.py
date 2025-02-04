# n, k = map(int,input().split())
# coins = [int(input()) for _ in range(n)]
# dp = [0] * (k+1) # 마지막 index는 k 가 될 것이다.
# dp[0] = 1
# for c in coins:
#     for j in range(c, k+1):
#         # if j-c >= 0: # 이거는 당연한건데... 하나같이 모든 사람이 다 이 조건을 명시해놨네 왜 그렇지?
#         dp[j] += dp[j-c]
#
# print(dp[k])



# 동전의 갯수가 아닌 경우의수다 그걸 유의하자
# 가치의 합이 k원이 되는 경우의 수를 구하는 전체의 문제를, 가치의 합이 i (1<i<k)원이 되는 경우의 수를 구하는 부분 문제로 나눈다.
# 추가적으로 부분 문제를 더욱 세부적으로 특정 동전을 썼을 때, 가치의 합이 i원이 되는 경우의 수를 구하는 부분 문제로 나눈다.

import sys

sys.setrecursionlimit(10 ** 7)


def solve():
    n, k = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline()) for _ in range(n)]

    # dp[i][v] = i번째 동전부터 사용하여 v원을 만드는 경우의 수
    dp = [[-1] * (k + 1) for _ in range(n)]

    def dfs(index, remain):
        # base case 1: 남은 금액이 정확히 0원이면 방법 1개 성립
        if remain == 0:
            return 1
        # base case 2: 동전을 더 사용할 수 없거나 금액이 음수가 되면 불가능
        if index == n or remain < 0:
            return 0

        # 이미 계산한 적이 있다면 dp 값 사용
        if dp[index][remain] != -1:
            return dp[index][remain]

        # ① index번째 동전을 "하나도 안 쓰고" 다음 동전으로 넘어가는 경우
        # ② index번째 동전을 "1개 이상 사용"하는 경우(한 번 쓰고 remain-coin만큼 다시 같은 index 동전 고려)
        dp[index][remain] = dfs(index + 1, remain) + dfs(index, remain - coins[index])
        return dp[index][remain]

    print(dfs(0, k))

# 실행 예시
# 입력 예:
#   3 10
#   1
#   2
#   5
# 출력: 10
