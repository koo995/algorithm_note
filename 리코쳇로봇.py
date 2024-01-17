from collections import deque
import heapq


def solution(board):
    def check_go(node):
        if (
            (0 <= node[0] < len(board))
            and (0 <= node[1] < len(board[0]))
            and (board[node[0]][node[1]] != "D")
        ):
            return True
        else:
            return False

    def find_nodes(cur_node):
        nodes = []
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for move in moves:
            go = True
            m = 1
            while go:
                next_node = [cur_node[0] + move[0] * m, cur_node[1] + move[1] * m]
                prev_node = [
                    cur_node[0] + move[0] * (m - 1),
                    cur_node[1] + move[1] * (m - 1),
                ]
                go = check_go(next_node)
                if go == False and prev_node != cur_node:
                    nodes.append(prev_node)
                m += 1
        return nodes

    # 시작
    INF = int(1e9)
    dp = [[INF] * len(board[0]) for _ in range(len(board))]  # 모든 거리는 최대로 만들어 본다.
    start = []
    end = []
    for row, b in enumerate(board):
        if "R" in b:
            start = [row, b.index("R")]
        if "G" in b:
            end = [row, b.index("G")]
    nodes = find_nodes(start)
    dp[start[0]][start[1]] = 0  # 시작지점은 거리가 0이지
    q = []
    for node in nodes:
        heapq.heappush(q, (1, node))
    while q:
        print("지금 큐에 있는 것", q)
        min_dist, cur_node = heapq.heappop(q)
        if dp[cur_node[0]][cur_node[1]] < min_dist:  # 처리된 적 있는 노드라면 무시한다
            continue
        n_nodes = find_nodes(cur_node)
        for n_node in n_nodes:
            cost = min_dist + 1
            if cost < dp[n_node[0]][n_node[1]]:
                dp[n_node[0]][n_node[1]] = cost
                heapq.heappush(q, (cost, n_node))

    print(dp)
    answer = dp[end[0]][end[1]]
    return answer - 1 if answer != INF else -1


# dp와 bfs로 푼다...?
d = [
    [5, 1000000000, 4, 1000000000, 1, 1000000000, 2],
    [1000000000, 1000000000, 3, 8, 2, 1000000000, 1],
    [6, 6, 1000000000, 7, 1000000000, 1000000000, 1000000000],
    [1000000000, 5, 4, 1000000000, 5, 1000000000, 8],
    [7, 6, 1000000000, 7, 6, 1000000000, 7],
]
# 매우 중요한것을 하나 얻은 것 같다. bfs에 치명적인 약점이 있군
# 방문처리 하기전에 같은 노드에 하나의 쿠에 중복으로 담겨 있으면 이후의 녀석으로 바뀌는 구나...
e = [
    [4, 1000000000, 3, 1000000000, 1, 1000000000, 0],
    [1000000000, 1000000000, 2, 7, 2, 1000000000, 1],
    [5, 5, 1000000000, 6, 1000000000, 1000000000, 1000000000],
    [1000000000, 4, 4, 1000000000, 5, 1000000000, 7],
    [6, 6, 1000000000, 7, 6, 1000000000, 7],
]


def solution2(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    start = None
    end = None
    d_s = []
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    for y, row in enumerate(board):
        for x in range(len(row)):
            if board[y][x] == "R":
                start = (y, x)
            if board[y][x] == "G":
                end = (y, x)
            if board[y][x] == "D":
                d_s.append((y, x))

    def bfs(start):
        from collections import deque

        q = deque()
        y, x = start[0], start[1]
        visited[y][x] = 1
        q.append((y, x, 0))
        while q:
            y, x, count = q.popleft()
            if (y, x) == end:
                return count
            for i in range(4):
                n_y, n_x = y, x
                while 1:
                    tmp_n_y = n_y + dy[i]
                    tmp_n_x = n_x + dx[i]
                    if (
                        (not (0 <= tmp_n_y < len(board)))
                        or (not (0 <= tmp_n_x < len(board[0])))
                        or (tmp_n_y, tmp_n_x) in d_s
                    ):
                        break
                    else:
                        n_y, n_x = tmp_n_y, tmp_n_x
                if visited[n_y][n_x] == 0:
                    visited[n_y][n_x] = 1
                    q.append((n_y, n_x, count + 1))

    result = bfs(start)
    return result if visited[end[0]][end[1]] == 1 else -1


print(solution2(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
