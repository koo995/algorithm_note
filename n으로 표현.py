from collections import deque

def solution(N, number):
    INF = 1e9
    dp = [INF] * (32000)
    dp[N] = 1 # 동전을 한개만 쓴 경우
    stack = deque()
    stack.append(N)
    for i in range(2,9): # 동전을 2개만 썼을때 에서 8개 썼을 때까지
        while stack:
            e = stack.popleft()
            # concat
            e_cat_N = int(str(e) + str(N))
            if e_cat_N < 32000 and dp[e_cat_N] > i:
                dp[e_cat_N] = i
                stack.append(e_cat_N)
            # 곱하기
            e_pow_N = e*N
            if e_pow_N < 32000 and dp[e_pow_N] > i:
                dp[e_pow_N] = i
                stack.append(e_pow_N)
            # 나누기
            if e % N == 0 and dp[int(e/N)] > i:
                dp[int(e/N)] = i
                stack.append(int(e/N))
            # 더하기
            e_plus_N = e + N
            if e+N < 32000 and dp[e_plus_N] > i:
                dp[e_plus_N] = i
                stack.append(e_plus_N)
            # 빼기
            if e - N > 0 and dp[e-N] > i:
                dp[e - N] = i
                stack.append(e-N)            
    return dp[number] if dp[number] <= 8 else -1
print(dp[:20])
print(solution(5, 12))
# print(solution(2, 11))

# "/" 연산은 float을 반환하나 보네