from collections import deque

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input())))

cost = [[0] * m for _ in range(n)]
d_row = [1, -1, 0, 0]
d_col = [0, 0, 1, -1]


def check_boundary(i, j):
    return i >= 0 and i < n and j >= 0 and j < m


def check_monster(i, j):
    return array[i][j] == 0


def bfs(i, j):
    global cost
    q = deque()
    q.append((i, j, 0))  # row col cost
    while q:
        row, col, prev_c = q.popleft()
        cost[row][col] = prev_c + 1
        for i in range(len(d_row)):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            if not check_boundary(n_row, n_col):  # 이 부분을 먼저 처리해 주고 몬스터나 방문을 처리해야지!
                continue
            if not check_monster(n_row, n_col) and cost[n_row][n_col] == 0:
                q.append((n_row, n_col, cost[row][col]))


bfs(0, 0)
for i in range(n):
    print(cost[i])
print(cost[n - 1][-1])


# 현재 궁금. 이걸 최단거리 문제인데... bfs? dfs? 또는 다익스트라? 그런걸 어떻게 구분할까?
# 어짜피 다 이어져 있으니까 포문을 돌 필요가 있을까? n과 m도 4-200인데... 다익스트라로도 가능?
# 다 돌필요가 없다 그냥 0,0에서 bfs 수행하면 끝
# 과거의 값을 저장하고 그 값에서 더하는 것은 어떻게 하지...?
# list index out of range가 뜨는 이유가 뭘까
# check boundary을 반대로 했네...
# 굳이 visited 테이블을 만들 필요는 없었던거 같아... cost가 0일때 새롭게 방문하면 되니까
