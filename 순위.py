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


print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [7, 1], [2, 6]]))


# 아하... 2에서 1은 갈수 있고, 1에서는 5를 갈수있을지 모르는것과 2는 못간다는것은 확실하게 구분해야 하구나...
