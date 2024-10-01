# def solution():
#     from collections import deque
#
#     N, M = map(int, input().split())
#     Map = [list(map(int, list(input()))) for _ in range(N)]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     start = (0, 0)
#     end = (N - 1, M - 1)
#     visited = [[[0] * M for _ in range(N)] for _ in range(2)]
#
#     q = deque()
#     visited[1][start[0]][start[1]] = 1
#     q.append((start, 1, 1))
#     while q:
#         cur_node, wild_card, count = q.popleft()
#         if cur_node == end:
#             print(count)
#             exit()
#         y, x = cur_node
#
#         for i in range(4):
#             n_y = y + dy[i]
#             n_x = x + dx[i]
#             if (0 <= n_x < M and 0 <= n_y < N) and (visited[wild_card][n_y][n_x] == 0) and (Map[n_y][n_x] == 0):
#                 visited[wild_card][n_y][n_x] = 1
#                 q.append(((n_y, n_x), wild_card, count + 1))
#
#         if wild_card:
#             for i in range(4):
#                 n_y = y + 2 * dy[i]
#                 n_x = x + 2 * dx[i]
#                 if (0 <= n_x < M and 0 <= n_y < N) and (visited[wild_card - 1][n_y][n_x] == 0) and (Map[n_y][n_x] == 0):
#                     visited[wild_card - 1][n_y][n_x] = 1
#                     q.append(((n_y, n_x), wild_card - 1, count + 2))
#
#     print(-1)

def solution2():
    from collections import deque

    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    end = (N - 1, M - 1)
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1  # 벽을 안뚫고 왔다? 벽을 뚫고 가장 빨리 온 지점이 있다면 그 뒤는 고려할 필요가 없지
    while q:
        y, x, broken = q.popleft()
        if (y, x) == end:
            print(visited[broken][y][x])
            exit()
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if not (0 <= n_y < N and 0 <= n_x < M and visited[broken][n_y][n_x] == 0):
                continue
            # 자 이제 행렬을 판단해보자 벽인지 아니면 길인지
            if matrix[n_y][n_x] == "1":
                if broken:
                    continue
                visited[1][n_y][n_x] = visited[broken][y][x] + 1
                q.append((n_y, n_x, 1))
            else:
                visited[broken][n_y][n_x] = visited[broken][y][x] + 1
                q.append((n_y, n_x, broken))
    print(-1)

solution2()