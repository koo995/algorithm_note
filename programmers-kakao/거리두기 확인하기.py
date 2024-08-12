from collections import deque

def solution(places):
    def check(p):
        # 흠... bfs 또는 dfs 을 사용하는 것 같은데...
        # 최단거리가 2이하면 안된다.
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        human_points = []
        for i in range(5):
            for j in range(5):
                if p[i][j] == "P":
                    human_points.append((i, j))
        for human_point in human_points:
            # 각 포인트에서 bfs 을 실행한다.
            q = deque()
            visited = [[0] * 5 for _ in range(5)]
            q.append((human_point, 0))
            visited[human_point[0]][human_point[1]] = 1
            while q:
                point, dist = q.popleft()
                y, x = point
                if dist >= 2:
                    break
                for i in range(4):
                    n_y = y + dy[i]
                    n_x = x + dx[i]
                    if not (0 <= n_y < 5 and 0 <= n_x < 5 and p[n_y][n_x] != "X" and visited[n_y][n_x] == 0):
                        continue
                    if p[n_y][n_x] == "P":
                        return 0
                    visited[n_y][n_x] = 1
                    q.append(((n_y, n_x), dist + 1))
        return 1

    answer = []
    for place in places:
        answer.append(check(place))
    return answer