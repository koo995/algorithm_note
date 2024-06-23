def solution():
    from collections import deque

    N, M = map(int, input().split())
    Map = [list(map(int, list(input()))) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    start = (0, 0)
    end = (N - 1, M - 1)
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]

    q = deque()
    visited[1][start[0]][start[1]] = 1
    q.append((start, 1, 1))
    while q:
        cur_node, wild_card, count = q.popleft()
        if cur_node == end:
            print(count)
            exit()
        y, x = cur_node

        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if (0 <= n_x < M and 0 <= n_y < N) and (visited[wild_card][n_y][n_x] == 0) and (Map[n_y][n_x] == 0):
                visited[wild_card][n_y][n_x] = 1
                q.append(((n_y, n_x), wild_card, count + 1))

        if wild_card:
            for i in range(4):
                n_y = y + 2 * dy[i]
                n_x = x + 2 * dx[i]
                if (0 <= n_x < M and 0 <= n_y < N) and (visited[wild_card - 1][n_y][n_x] == 0) and (Map[n_y][n_x] == 0):
                    visited[wild_card - 1][n_y][n_x] = 1
                    q.append(((n_y, n_x), wild_card - 1, count + 2))

    print(-1)


solution()