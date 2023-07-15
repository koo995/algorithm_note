n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [-1] * (100000+1) # k번째까지 일단 모두 불가능으로 둔다...?
for c in coins: # 해당 코인까지의 조합중 제일 작은건 역시 코인 하나만 쓰는 것이지
    dp[c] = 1
    
if k <= coins[0]:
    print(dp[k])
else: # 여기서는 k가 coins[0]보다 큰 경우
    for i in range(coins[0]+1, k+1): # 코인의 제일 작은 녀석부터...? 아니 그 다음녀석부터 체크해야할듯
        temp = [dp[i-c]+1 for c in coins if i-c >= 0 and dp[i-c] != -1] # temp가 비었을 수 있다.
        if not temp: # 비엇다면 처리하지 않는다.
            continue
        if dp[i] != -1: # 이미 경우의 수가 존재한다면
            temp.append(dp[i])
        dp[i] = min(temp)
    print(dp[k])


# index 에러가 발생했다. 아마도 k의 값보다 c가 더 커서 그런 듯 하다
# 어디서 계속 index 에러가 발생하는 것이지?
# 아... coin은 10만 까지 갈 수 있는데 dp는 최대 10000까지 해놔서 그렇군...
# min() arg is an empty sequence 발생했다. min 안에 빈 리스트가 들어가서 그런듯 하다.