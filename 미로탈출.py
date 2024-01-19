def solution(maps):
    from collections import deque
    import copy

    max_y = len(maps)
    max_x = len(maps[0])
    start = None
    end = None
    lever = None
    for y in range(max_y):
        for x in range(max_x):
            if maps[y][x] == "S":
                start = (y, x)
            if maps[y][x] == "L":
                lever = (y, x)
            if maps[y][x] == "E":
                end = (y, x)
    visited = [[0] * max_x for _ in range(max_y)]
    result = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(start, target, visited):
        q = deque()
        visited[start[0]][start[1]] = 1
        q.append((start[0], start[1], 0))
        while q:
            y, x, count = q.popleft()
            print(f"y: {y}, x: {x}, count: {count}")
            if (y, x) == target:
                result.append(count)
                break
            for i in range(4):
                n_x = x + dx[i]
                n_y = y + dy[i]
                if (
                    0 <= n_y < max_y
                    and 0 <= n_x < max_x
                    and visited[n_y][n_x] == 0
                    and maps[n_y][n_x] != "X"
                ):
                    visited[n_y][n_x] = 1
                    q.append((n_y, n_x, count + 1))

        return 0

    bfs(start, lever, copy.deepcopy(visited))
    print("-------------------")
    bfs(lever, end, copy.deepcopy(visited))

    print("result", result)

    return sum(result) if len(result) == 2 else -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))

# 뭐... 이 이상으로 풀이가 짧은 수는 없네
