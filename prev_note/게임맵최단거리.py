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

    # 이거 틀린 코드임
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


# bfs로 했을때 왜 시간초과가 계속 뜨는 거지?
# dfs로 했을 때 문제가 발생한다는 것은 알겠지만... 비 효율적이잖아
# bfs는 큐에 넣기전에 방문처리를 해줘야 중복을 피할 수 있다...?
# 이거 매우매우 매우 중요하네... 큐에 넣기전에 방문처리를 해줘야 방문하지 않은녀석들이 쌓이지 않는구나


def solution2(maps):
    from collections import deque
    import time
    import copy

    INF = int(1e9)
    n = len(maps)
    m = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[0] * m for _ in range(n)]
    answers = []
    start = (0, 0)

    # solution1에서는 내가 왜 dp을 썼는지 모르겠지만.... 이게 맞다.
    def bfs(start, count):
        q = deque()
        visited[start[1]][start[0]] = 1
        q.append((start, count))
        while q:
            node, count = q.popleft()
            if node[0] == n - 1 and node[1] == m - 1:
                answers.append(count)
            for i in range(4):
                n_x = node[1] + dx[i]
                n_y = node[0] + dy[i]
                if 0 <= n_y < n and 0 <= n_x < m:
                    if maps[n_y][n_x] == 0 or visited[n_y][n_x] == 1:
                        continue
                    visited[n_y][n_x] = 1
                    q.append(((n_y, n_x), count + 1))

    # 자 이 방법은... 무지막지하게 완전탐색을 하니까 테케는 다 맞추었지만 효율성에서 탈락! 재귀는 알맞게 쓰기 위해선 dp를 건드려야 할까?
    # 건드리나 안드리나... 이 탐색방법에서는 문제를 나눠서 생각해볼 그것이 없는것 같은데...? 어쨋든 완전탐색이고... 질의응답을 봐도 dfs는 안된다고 하네
    def dfs(start, visited: list, count):
        visited[start[0]][start[1]] = 1
        if start[1] == m - 1 and start[0] == n - 1:
            answers.append(count)
            return

        for i in range(4):
            n_x = start[1] + dx[i]
            n_y = start[0] + dy[i]
            if 0 <= n_y < n and 0 <= n_x < m:
                if (
                    maps[n_y][n_x] == 0 or visited[n_y][n_x] == 1
                ):  # 0인 경우는 벽이거나, visited가 1인 경우는 방문햇던녀석
                    continue
                dfs(
                    (n_y, n_x), copy.deepcopy(visited), count + 1
                )  # 이렇게 했을때 visited가 겹치는 문제가 있네? 아.... 2차원 배열이지... deepcopy

    # dfs(start, visited, 0)
    bfs(start, 0)
    print("answer: ", answers)
    return min(answers) + 1 if answers else -1


print(
    solution2(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1],
        ]
    )
)


# 우선 문제는 최단거리를 찾는 문제다
# 최단거리는 보통 다익스트라, 플로이드 워셜과 같다
# 완전탐색으로 가야할까?
# 느낌상 bfs와 다익스트라가 가능할 것 같다.
# bfs가보자
# 방문처리를 할까 말까? 지나왔던 곳을 다시 갈 수 는 없잖아?
# 그렇다면 방문처리는 한다했을때 bfs에서 어케 처리가 되야할까
# dfs는 각자 한다했을때 방법이 생각난다. 그러면 dfs 먼저 해볼까?
# 그냥 별 의미없이 dfs나 bfs로 각자 최단거리 초기화시켜 나가면 될듯
# 방법 1. 모든 1인 경로에 최단거리를 직접 기록하고 마지막 녀석의 최단거리가 1이면 -1 아니면 그 값을 전달
# 방법 2. 어쨋든 무지막작하기 완전탐색을 하여서 그곳에 도달할때마다 answers 안에 넣는다. 그러면 언제까지 완전탐색을 할 것이냐가 중요한데... 이 방법은 효율성에서 탈락해
# visited_table을 만들어서 사방을 지나갈수없을때...? 참고로 이차원테이블을 전달할때는 deepcopy....
