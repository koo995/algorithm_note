# n, k = map(int, input().split())
# coins = [ int(input()) for _ in range(n)]
# coins.sort()
# INF = int(1e9)
# dp = [INF] * (100001) # 100001까지의 가치를 나타내기 위함.
# for coin in coins:
#     dp[coin] = 1
#
# for i in range(coins[0]+1, k+1): # 첫번째 코인 전까지는 아무것도 못 만들테야
#     for coin in coins:
#         if i - coin >= 0 :
#             dp[i] = min(dp[i], dp[i-coin] + 1)
# print(dp[k] if dp[k] != INF else -1)




# index 에러가 발생했다. 아마도 k의 값보다 c가 더 커서 그런 듯 하다
# 어디서 계속 index 에러가 발생하는 것이지?
# 아... coin은 10만 까지 갈 수 있는데 dp는 최대 10000까지 해놔서 그렇군...
# min() arg is an empty sequence 발생했다. min 안에 빈 리스트가 들어가서 그런듯 하다.


# 처음에 그리디하게 생각을 했지만... 만약에 남은 수에 대해서 동전으로 만들지 못하는 경우가 생길 수 있음을 고려해야한다.
def solution():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort()

    INF = int(1e9)
    dp = [INF] * (k + 1)
    for coin in coins:
        if coin > k:
            continue
        dp[coin] = 1

    for value in range(k + 1):
        for coin in coins:
            if value - coin >= 0:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    print(dp[k] if dp[k] != INF else -1)

solution()