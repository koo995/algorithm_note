def solution():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 어쨋든 dp을 이용하여 완전히 탐색을 이어나가야 한다는 것이다.
    # 방문한 녀석들이 같고, 현재 위치가 같다면 그 뒤의 최소비용은 일치할 것이다.
    # 그 상황에서 여러번 구하는 것을 막겠다가 여기서의 주요 메모이제이션이다.
    INF = int(1e9)
    dp = [
        [INF] * (1 << N) for _ in range(N)
    ]  # 이 값은 종료지점까지의 최소거리로 해야할까? 그러니까 이전까지가 아닌 미래의 기대되는 값

    def dfs(
        start: int, visited
    ) -> int:  # dfs의 역할을 무엇으로 할 것이냐? 최소값을 전달하는 것으로 목적을 정한다 해야할까?
        # 여기서 종료조건을 정의한다. 아니 정확히는 모든 곳을 방문했을때 어떤 값을 전달하지? 그 동안의 합을 전달해야 하지 않나?
        # 아니다 여기서는 그동안의 전체가 아니라 바로 전 녀석에게 값을 전달해줘야지
        if visited == (1 << N) - 1:
            if (
                graph[start][0] != 0
            ):  # 모든 녀석들을 다 방문했을때 거기서에서 미래에 방문할 값을 전달해야하지 그러니까 길이 있으면?
                return graph[start][0]
            else:  # 갈수있는 길이 없다면 INF
                return INF
        # 구한 최소값이 있다면 그 녀석을 넘겨준다.
        if dp[start][visited] != INF:
            return dp[start][visited]
        # 이제부터 탐색을 한다.
        for next in range(N):
            # 길이 없거나, 방문했던 녀석이라면 제외한다.
            if (graph[start][next]) == 0 or (visited & (1 << next) != 0):
                continue
            # 근데 말야... 이 값이 최소라고 할 수 있나? 으흠... 현재 위치와 그 이전상태의 방문여부니까 완전히 일치한다고 볼 수 있는 것인가?
            # 왜 이게 크게 와닿지가 않지?
            dp[start][visited] = min(
                dp[start][visited], dfs(next, visited | 1 << next) + graph[start][next]
            )
        return dp[start][
            visited
        ]  # 제일 마지막에 반환되는 이녀석은 start = 0이고 visited는 00001인 경우가 되겠네...

    visited = 0b0
    start = 0
    return dfs(
        start, visited | 1 << start
    )  # visited는 이전에 방문했던 목록을 뜻한다. start의 방문처리를 해준다.


print(solution())

# 시간초과가 발생했다... 뭐가 문제지?


def solution2():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)
    dp = [[INF] * (1 << N) for _ in range(N)]

    def dfs(start, visited):
        if visited == (1 << N) - 1:
            if graph[start][0] != 0:
                return graph[start][0]
            else:
                return INF
        if dp[start][visited] != INF:
            return dp[start][visited]
        for next in range(N):
            if (graph[start][next]) == 0 or (visited & (1 << next) != 0):
                continue
            dp[start][visited] = min(
                dp[start][visited], dfs(next, visited | 1 << next) + graph[start][next]
            )
        return dp[start][visited]

    visited = 0b0
    start = 0
    return dfs(start, visited | 1 << start)


print(solution2())

# 시간초과가 발생했다... 뭐가 문제지?
# 어떤 점에서 어떤 길로도 갈 수 없으면 어떻게 될까?
"""저도 같은 이유로 정말 오래 며칠 고민했습니다 ㅠㅠ

결국 해결했는데 문제는 dp 를 INF 로 초기화 하는 것입니다.


dp를 INF로 놓고 dfs를 하면 발생할 수 있는 문제가

방문을 해봤는데 가능한 경우가 없는 케이스 입니다.

예를 들어 0010을 방문했다고 가정했을 때

만약 3 -> 1 , 3 -> 2, 3-> 4 로 가는 경우가 모두 없는 경우에는 마지막에 INF를 return하게 되는데 그러면

방문을 해봤는데 경로가 없어서 INF인건지, 방문을 안했는지를 알 수 가 없어

0010 이 호출 될 때마다 dp 값을 리턴하는게 아니라 dfs를 계속 돌기 때문에 시간 초과가 발생하는 것 같습니다.



그래서 저는 dp 값을 -1로 초기화 한 후에 마지막에 dp 값이 -1인 경우 ( 즉 다른 노드로 가는 경로가 없는 경우 ) 에는 INF 값을 리턴하게 만들어서 

방문하지 않은 케이스는 dp 값이 -1이게 하고

방문 했는데 길이 없는 경우에는 dp 값을 INF를 리턴하게 했더니 문제가 맞았습니다.

조금 두서 없는 글인데 해결 되셨으면 좋겠습니다
"""
