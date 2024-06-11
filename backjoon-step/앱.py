def solution():
    N, M = map(int, input().split())  # N개의 앱이 활성화, M 이상의 메모리를 확보해야함
    active_app_memory = list(map(int, input().split()))
    de_active_cost = list(map(int, input().split()))
    INF = int(1e9)
    dp = [[0] * 10001 for _ in range(N)]
    min_cost = INF

    for i in range(N):
        for cost in range(10001):
            require_cost, memory = de_active_cost[i], active_app_memory[i]
            dp[i][cost] = max(dp[i - 1][cost],
                              dp[i - 1][cost - require_cost] + memory if cost - require_cost >= 0 else 0)
            if dp[i][cost] >= M:
                min_cost = min(min_cost, cost)
    print(min_cost)


solution()
# 냅색문제랑 비슷한거 같은데?
# 문제를 다르게 생각하면 최소 M이상의 메모리를 가져야할때, 최소의 비용을 구하여라!
# 뭔가 이상하다... 최소비용 그거 만들 수 있는 것이어야 하잖아?
# 최소 min_cost 에서 같은 i 번째 라인에서 제일 작은 cost 가 들어가겠지? 그리고 그곳에서 M이상 이였다면 변경이 일어났다는 것이니까
# 변경이 일어났다는 것은 메모리 확보가 가능한 케이스다?
# dp 값으로 최대 확보할 수 있는 메모리가 들어가는 문제로 바꾸는 것은 그래프를 그려보기전까지 상상하기가 쉽지않다.
# 그치만 이런게 가능하다는 것을 알게되었고 언젠가 코테에서 본다면 떠올려보자
