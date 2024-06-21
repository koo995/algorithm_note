def solution():
    from collections import deque
    import sys

    M, N = map(int, sys.stdin.readline().split())  # M은 가로 N 은 세로 각각 1000 까지 최대 총 10만개 까지
    Box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 처음부터 익어있는 토마토의 위치를 구한다.
    tomato_positions = []
    zero_count = 0
    for i in range(N):
        for j in range(M):
            if Box[i][j] == 1:
                tomato_positions.append((i, j))
            if Box[i][j] == 0:
                zero_count += 1
    # 각 토마토의 위치들에 대해서 동시에 bfs 가 진행이 되어야 하는데...
    q = deque()
    for start_position in tomato_positions:
        q.append((start_position, 0))
    result = 0
    while q:
        current_position, count = q.popleft()
        y, x = current_position
        # 다 익었는지 체크한다. 근데... 그 체크를 매번 한다...?
        if zero_count == 0:
            result = count
            break
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if (0 <= n_x < M and 0 <= n_y < N) and (Box[n_y][n_x] == 0):
                Box[n_y][n_x] = 1
                zero_count -= 1
                q.append(((n_y, n_x), count + 1))
    # 무엇으로 끝났는지 모르니까... check 로 끝났다면 q 가 남아있을수있다. 반복문을 다 처리했다면?
    if zero_count == 0:
        if q:
            _, count = q.pop()
            result = max(result, count)
        print(result)
    else:
        print(-1)

solution()