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
    ) -> (
        int
    ):  # dfs의 역할을 무엇으로 할 것이냐? 최소값을 전달하는 것으로 목적을 정한다 해야할까?
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


# print(solution())

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


# print(solution2())

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


def solution3():
    N = int(input())  # 2~16
    costs = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)
    dp = [
        [-1] * (1 << N) for _ in range(N)
    ]  # 우선 방문하지 않았으니까 모두 -1로 둔다. 방문했고 불가능하다면 INF로 한다.

    # 아무것도 반환하지는 않을 것이다. 다만 dp테이블에 계속해서 초기화해나가는 함수다.
    def dfs(start, visited):

        # 모든것을 방문 했다면... 아... 어짜피 첫번째 노드는 방문처리가 되어있고... 마지막 녀석까지 갔고 이제 마지막 녀석에서 처음 녀석으로 돌아갈 일만 남았군...
        if visited == (1 << N) - 1:
            if costs[start][0] != 0:
                return costs[start][0]
            else:  # 갈수있는 길이 없다면?
                return INF
        if dp[start][visited] != -1:
            return dp[start][visited]

        # 그런데
        # 후... 여기서 방문처리를 해줘야 하는것을 잘 모르겠다...
        dp[start][visited] = INF

        for next in range(N):
            # 대신에 현재에서 next로 길이 있어야 한다. 그리고 방문했던 녀석이면 계산의 중복을 피하기 위해서 제외해야한다.
            if costs[start][next] == 0 or (visited & (1 << next) != 0):
                continue
            # 그러니까 여기서 dp[start][visited]라는 것은 반복문을 위에서 도는 것을 통해 next의 모든 경우를 다 고려하여 min 값을 얻은 것이다. 그런데 그게 INf라면?
            dp[start][visited] = min(
                dp[start][visited],
                dfs(next, visited | 1 << next) + costs[start][next],
            )
        return dp[start][visited]  # 결국에 이 함수는 이 최소비용을 던진다는 것인데...

    # start는 0번부터 시작하고
    start = 0
    # dp의 두번째 인자로 방문상태를 나타내기 위한, 이진수로는 모두 0이 되겠지? 방문한 것이 없으니까
    visited = 0b0
    result = dfs(start, visited | 1 << start)
    print("result: ", result)


# 위의 코드를 깔끔히...
def solution4():
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)
    dp = [[INF] * (1 << N) for _ in range(N)]

    def dfs(start, visited):
        if visited == (1 << N) - 1:
            if costs[start][0] != 0:
                return costs[start][0]
            else:
                return INF - 1
        if dp[start][visited] != INF:
            return dp[start][visited]

        for next in range(N):
            if costs[start][next] == 0 or (visited & (1 << next) != 0):
                continue
            dp[start][visited] = min(
                dp[start][visited],
                dfs(next, visited | 1 << next) + costs[start][next],
            )
        return dp[start][visited]

    start = 0
    visited = 0b0
    result = dfs(start, visited | 1 << start)
    print(result)

def solution5():
    def dfs(node, visited):
        # 종료조건은 무엇으로? 시작노드 포함 모든 노드를 다 탐색하였고, 현재 노드에서 시작노드로만 움직이면 되는 상황이다.
        if visited == (1 << N) - 1:
            if matrix[node][start] != 0:
                return matrix[node][start]
            else:  # 만약에 가는 길이 없다면...? 그렇지만 탐색했다는 해줘야하지 않나? 이 값이 최소비교를 당하니까... 기존의 값은 유지하기 위해 -1은 안되겠다.
                return INF - 1
        if dp[node][visited] != INF or dp[node][visited] != INF - 1:
            return dp[node][visited]

        for next_node in range(N):
            if matrix[node][next_node] == 0 or (visited & (1 << next_node) != 0):
                continue
            dp[node][visited] = min(dp[node][visited], dfs(next_node, visited | (1 << next_node)) + matrix[node][next_node])

        return dp[node][visited]

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 이 매트릭스로 따로 그래프를 그릴 필요는 없겠는데?
    INF = int(1e9)
    # dp[현재위치][방문한상태]
    dp = [[INF] * (1 << N) for _ in range(N)]
    start = 0
    visited = 0b0
    print(dfs(0, visited | 1 << start))


# solution5()
# 극단적인 케이스에 대해서 결국에 계산은 되지만 시간이 너무너무 많이 걸린다는 것이 문제였구나
# 순환할수 없는 경우와 방문하지않은 경우는 분리를 해야 하는 거야


def solution6():
    def tsp(node, visited_state):
        # 만약 모든 점을 방문했다면
        if visited_state == (1 << N) - 1:
            # 현재 위치에서 start로 갈수있냐?
            if board[node][start] != 0:
                return board[node][start]
            elif board[node][start] == 0:
                return INF

        # 현재상태를 가지고 방문한 적이 있으면 그 값을 넘겨준다. 만약 길이 없다면? INF가 넘겨지겠지..
        if dp[node][visited_state] != -1:
            return dp[node][visited_state]

        # 최소비교를 해야하는데 기존에 -1값이 있으면 비교를 할 수 없다..
        dp[node][visited_state] = INF
        for n_node in range(N):
            # 다음 길로 갈 수 없으면 못간다.
            if board[node][n_node] == 0 or visited_state & (1 << n_node) != 0:
                continue
            dp[node][visited_state] = min(dp[node][visited_state], tsp(n_node, visited_state | 1 << n_node) + board[node][n_node])

        return dp[node][visited_state]

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    INF = int(1e9)
    start = 0
    dp = [[-1] * (1 << N) for _ in range(N)]  # 방문 상태는 몇개가 될 수 있지?
    print(tsp(start, 1 << start))

solution6()