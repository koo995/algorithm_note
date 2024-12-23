from collections import deque

def solution():
    M, N = map(int, input().split())
    board = [input() for _ in range(M)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = set()
    visited.add(board[0][0])
    q = deque()
    q.append(((0, 0, 1, visited)))

    max_dist = 1
    while q:
        y, x, d, cur_visited = q.popleft()
        max_dist = max(max_dist, d)

        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]

            # board을 나간다면 탐색 안함.
            if not (0 <= n_y < M and 0 <= n_x < N):
                continue

            # 지나간 알파벳도 안감.
            if board[n_y][n_x] in cur_visited:
                continue
            next_visited = cur_visited.copy()
            next_visited.add(board[n_y][n_x])
            q.append((n_y, n_x, d + 1, next_visited))

    print(max_dist)


solution()