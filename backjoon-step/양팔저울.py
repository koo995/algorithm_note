def solution():
    CHU_N = int(input())  # 30이하
    chu_lst = list(map(int, input().split()))  # 500이하. 같은 무게가 여러개일수있음
    MARBLE_N = int(input())  # 7이하
    marble_lst = list(map(int, input().split()))  # 4만이하
    # max_weight = max(max(chu_lst), max(marble_lst)) + 1
    max_weight = 40001
    dp = [["N"] * max_weight for _ in range(CHU_N)]
    dp2 = ["N"] * max_weight
    for i, chu_w in enumerate(chu_lst):
        for w in range(max_weight):
            if w == chu_w:
                dp[i][w] = "Y"
            if dp[i - 1][w] == "Y":
                dp[i][w] = "Y"
            if i - 1 >= 0 and w + chu_w < max_weight and dp[i - 1][w + chu_w] == "Y":
                dp[i][w] = "Y"
            if i - 1 >= 0 and 0 <= chu_w - w < max_weight and dp[i - 1][chu_w - w] == "Y":
                dp[i][w] = "Y"
            if i - 1 >= 0 and 0 <= w - chu_w < max_weight and dp[i - 1][w - chu_w] == "Y":
                dp[i][w] = "Y"
            if dp[i][w] == "Y":
                dp2[w] = "Y"
    for marble in marble_lst:
        print(dp2[marble], end=" ")

def solution2():
    chu_number = int(input())
    chu_lst = list(map(int, input().split()))
    marble_number = int(input())
    marble_lst = list(map(int, input().split()))

    dp = {chu_lst[0]}
    for i in range(1, chu_number):
        s = {chu_lst[i]}
        for j in dp:
            s.add(j + chu_lst[i])
            s.add(abs(j - chu_lst[i]))
        dp = dp | s

    print(*map(lambda x: ('Y' if x in dp else 'N'), marble_lst))


solution()
# 1. 구슬의 모든 경우의수를 탐색해 나갈까? 낱개는 미리 y / n 로 정해놓는다 치면은 덧셈과 뺄셈만 모두 구하면 되는데...
# 연산은 최대 2^500이다.... 적당한 가자치기를 한다해도... 줄이기는 쉽지 않아보이는데
# 그냥 ㅆ 생각나는데로 하면 되는건데 계속 냅색이니 그런거나 다른 블로그에서 본 방식을 생각해서 꼬이는거 아녀