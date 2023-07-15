n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [-1] * (10000+1) # k번째까지 일단 모두 불가능으로 둔다...?
for c in coins: # 해당 코인까지의 조합중 제일 작은건 역시 코인 하나만 쓰는 것이지
    dp[c] = 1

for i in range(coins[0]+1, k+1): # 코인의 제일 작은 녀석부터...? 아니 그 다음녀석부터 체크해야할듯
    temp = [dp[i-c]+1 for c in coins if i-c >= 0 and dp[i-c] > 0]
    if dp[i] > 0:
        temp.append(dp[i])
    dp[i] = min(temp)
# print(dp)
print(dp[k])


# index 에러가 발생했다. 아마도 k의 값보다 c가 더 커서 그런 듯 하다
# 어디서 계속 index 에러가 발생하는 것이지?
# min() arg is an empty sequence 발생했다. min 안에 빈 리스트가 들어가서 그런듯 하다.