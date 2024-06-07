def solution():
    def dfs(y, x):
        # 목표지점에 도착하면 끝?
        # 외판원 순회 문제이서 힌트를 얻자... 거쳐온 녀석들이 같다면?
        if y == M - 1 and x == N - 1:
            # 여기서 값을 설정하고 되돌아갈 필요가 있을까? 그냥 끝이니까 되돌아가면 될듯?
            return 1

        # 또 어떤 경우에 끝내야할까? 이미 방문했던 지점 즉 dp값이 있는 경우?
        if dp[y][x] >= 0: # 처음에 0 초과로 설정해서 잘못되었네... 0인 경우도 체크해야지
            return dp[y][x]  # 여기서 그냥 1로 반환했더니 틀렸다. 다음 노드에서 기대되는 값이 현재 노드에 전달되어야지?

        results = [0, 0, 0, 0]
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if not (0 <= n_y < M and 0 <= n_x < N):
                continue
            if Map[y][x] > Map[n_y][n_x]:
                results[i] = dfs(n_y, n_x)
        # results에 각 방향으로의 예상 값이 적혀있을 것이다.
        dp[y][x] = sum(results)
        return dp[y][x]

    M, N = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(M)]
    dp = [[-1] * N for _ in range(M)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dp[0][0] = dfs(0, 0)
    print(dp[0][0])



solution()
#  결과론적으로 답이 있을것이다 라고 생각한 것이 문제구나?
# 답이 없을 수 있다. 그러면 어떻게 처리할 것이냐?특정지점에서 답이 없다는 것을 체크해야하는데... 방문하지 않은 경우는 -1로... 방문한 경우는 답이 없는 0으로 하자.