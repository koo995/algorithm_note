def solution(n, results):
    # 이 승부의 결과를 단방향 그래프로 만들어서 표현해 볼까?
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for win, lose in results:
        graph[lose][win] = 1
        graph[win][lose] = -1
    print("graph: ", graph)
    # table = [[0] * (n + 1) for _ in range(n + 1)]  #
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # 갈수있고, 갈수없고, 모른다를 정하자.
                # 그러기 위해서 갈 수 없다는 확실하게 진다는 정보구나. 그걸 정해야 겠어.
                # 먼저 갈수있는것을 체크해 놓자. 그냥 갈 수 있는 것은 정했으니, 다른 노드를 거치고 갈 수 있는지 없는지 체크하자.
                if (i == j) or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1
                    continue
                # 4에서 5로도 갈 수 없다는 것을 알려줘야 겠구나. 이 부분이 잘못되었어.
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1  # 하... 여기다가 등호를 2개를 써놨네...
    return n - len([1 for node in graph[1:] if 0 in node[1:]])


# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [7, 1], [2, 6]]))


# 아하... 2에서 1은 갈수 있고, 1에서는 5를 갈수있을지 모르는것과 2는 못간다는것은 확실하게 구분해야 하구나...


def solution2(n, results):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for win, lose in results:
        dp[win][lose] = 1
        dp[lose][win] = -1
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if dp[a][k] == 1 and dp[k][b] == 1:
                    dp[a][b] = 1
                elif dp[a][k] == -1 and dp[k][b] == -1:
                    dp[a][b] = -1
    count = 0
    for row in dp[1:]:
        row: list = row[1:]  # 슬라이싱함
        if row.count(0) == 1:
            count += 1
    return count


print(solution2(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 플로이드 워셜 알고리즘이라..
# 바킹독의 알고리즘 강의 듣기

# 이 문제 위상정렬을 한번 응용해 보자.
def solution3(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for win, lose in results:
        graph[lose][win] = 1
        graph[win][lose] = -1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if (i == j) or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1
                    continue
                # 4에서 5로도 갈 수 없다는 것을 알려줘야 겠구나. 이 부분이 잘못되었어.
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    return n - len([1 for node in graph[1:] if 0 in node[1:]])