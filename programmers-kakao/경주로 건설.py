def solution(board):
    import heapq

    dy = [-1, 1, 0, 0]  # 상하좌우가 된다.
    dx = [0, 0, -1, 1]
    N = len(board)
    costs = []
    q = []
    min_costs = [[[int(1e9)] * N for _ in range(N)] for _ in range(4)]
    for i in range(4):
        min_costs[i][0][0] = 0
        heapq.heappush(q, (0, (0, 0), i))  # 비용, 좌표, 방향
    while q:
        cost, point, d = heapq.heappop(q)
        y, x = point
        if point == (N - 1, N - 1):
            costs.append(cost)
        if min_costs[d][y][x] < cost: # 현재 내가 온 방향으로 부터 더 작은 값이 갱신된 것이 있다면 그 녀석은 건너뛴다.
            continue
        for n_d in range(4):
            n_y = y + dy[n_d]
            n_x = x + dx[n_d]
            if not (0 <= n_x < N and 0 <= n_y < N and board[n_y][n_x] == 0):
                continue
            if d != n_d:
                if min_costs[n_d][n_y][n_x] > cost + 600:
                    # 최소값이 같더라도 방향에 따라서 다음의 최소값이 달라질수있으니 등호를 추가해서 고려해주자.
                    min_costs[n_d][n_y][n_x] = cost + 600
                    heapq.heappush(q, (cost + 600, (n_y, n_x), n_d))
            else:
                if min_costs[n_d][n_y][n_x] > cost + 100:
                    min_costs[n_d][n_y][n_x] = cost + 100
                    heapq.heappush(q, (cost + 100, (n_y, n_x), n_d))

    return min(costs)



print(solution([[0,1,0,0,0],[0,0,0,1,0],[1,1,1,0,0],[0,0,0,0,1],[0,0,0,0,0]]))

# 아... 역시 db 에서 방향을 고려해줘야하나?