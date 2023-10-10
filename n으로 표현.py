from collections import deque

def solution(N, number):
    INF = 1e9
    dp = [INF] * (32001)
    dp[N] = 1 # 동전을 한개만 쓴 경우
    stack = deque()
    stack.append((1,N))
    while stack:
        i, e = stack.popleft()
        if i >= 8:
            break
        # concat
        e_cat_N = int(str(e) + str(N))
        if e_cat_N < 32001:
            dp[e_cat_N] = min(dp[e_cat_N], i+1)
            stack.append((i+1,e_cat_N))
        # 곱하기
        e_pow_N = e*N
        if e_pow_N < 32001:
            dp[e_pow_N] = min(dp[e_pow_N], i+1)
            stack.append((i+1, e_pow_N))
        # 나누기
        if 0 <= int(e/N) < 32001:
            dp[int(e/N)] = min(dp[int(e/N)], i+1)
            stack.append((i+1,int(e/N)))
        # 더하기
        e_plus_N = e + N
        if e+N < 32001:
            dp[e_plus_N] = min(dp[e_plus_N], i+1)
            stack.append((i+1,e_plus_N))
        # 빼기
        if e - N >= 0:
            dp[e - N] = min(dp[e - N], i+1)
            stack.append((i+1, e-N))
    return dp[number] if dp[number] <= 8 else -1
    print(dp[:20])
print(solution(5, 12))
print(solution(5, 3025))
# print(solution(2, 11))
# "/" 연산은 float을 반환하나 보네
# 무한 루프에 빠지는 이유는 뭐지? 동전의 갯수가 업데이트가 안되는 구나
# 나머지는 무시한다는데...