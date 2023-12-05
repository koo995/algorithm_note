def solution(maps):
    from collections import deque

    INF = 1e9
    global dp
    global visited
    dp = [[INF] * len(maps[0]) for _ in range(len(maps))]
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    start = [0, 0]

    def bfs(start, count):
        q = deque()
        visited[start[0]][start[1]] = 1
        q.append((start, count))
        while q:
            current, count = q.popleft()
            current_x = current[0]
            current_y = current[1]
            print(f"current_x:{current_x}, current_y: {current_y}")
            dp[current_x][current_y] = min(dp[current_x][current_y], count)
            if current_x == len(dp) - 1 and current_y == len(dp[0]) - 1:
                break
            for i in range(4):
                n_x = current_x + dx[i]
                n_y = current_y + dy[i]
                if (
                    0 <= n_x < len(dp)
                    and 0 <= n_y < len(dp[0])
                    and visited[n_x][n_y] == 0
                    and maps[n_x][n_y] == 1
                ):
                    visited[n_x][n_y] = 1
                    q.append(([n_x, n_y], count + 1))
        return 0

    def dfs(start, count):
        current_x = start[0]
        current_y = start[1]
        visited[current_x][current_y] = 1
        dp[current_x][current_y] = min(dp[current_x][current_y], count)
        if current_x == len(dp) - 1 and current_y == len(dp[0]) - 1:
            return 0
        for i in range(4):
            n_x = current_x + dx[i]
            n_y = current_y + dy[i]
            if (
                0 <= n_x < len(dp)
                and 0 <= n_y < len(dp[0])
                and visited[n_x][n_y] == 0
                and maps[n_x][n_y] == 1
            ):
                dfs([n_x, n_y], count + 1)

    bfs(start, 0)
    print("dp: ", dp)

    return (
        dp[len(maps) - 1][len(maps[0]) - 1] + 1
        if dp[len(maps) - 1][len(maps[0]) - 1] != INF
        else -1
    )


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)


# bfs로 했을때 왜 시간초과가 계속 뜨는 거지?
# dfs로 했을 때 문제가 발생한다는 것은 알겠지만... 비 효율적이잖아
# bfs는 큐에 넣기전에 방문처리를 해줘야 중복을 피할 수 있다...?
# 이거 매우매우 매우 중요하네... 큐에 넣기전에 방문처리를 해줘야 방문하지 않은녀석들이 쌓이지 않는구나
