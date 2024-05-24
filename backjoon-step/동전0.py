def solution():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if K == 0:
            break
        count += K // coin
        K = K % coin    
    print(count)
            

solution()