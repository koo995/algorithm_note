n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1) # 마지막 index는 k 가 될 것이다.
dp[0] = 1
for c in coins:
    for j in range(c, k+1):
        # if j-c >= 0: # 이거는 당연한건데... 하나같이 모든 사람이 다 이 조건을 명시해놨네 왜 그렇지?
        dp[j] += dp[j-c]

print(dp[k])



# 동전의 갯수가 아닌 경우의수다 그걸 유의하자
# 가치의 합이 k원이 되는 경우의 수를 구하는 전체의 문제를, 가치의 합이 i (1<i<k)원이 되는 경우의 수를 구하는 부분 문제로 나눈다.
# 추가적으로 부분 문제를 더욱 세부적으로 특정 동전을 썼을 때, 가치의 합이 i원이 되는 경우의 수를 구하는 부분 문제로 나눈다.