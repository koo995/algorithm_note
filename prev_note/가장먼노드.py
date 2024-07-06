def solution(n, infos):
    # 그래프를 초기화 해야 하는데... 방법은 리스트로써 하던가 dict을 이용하던가... 2차원배열을 이용하던가...?
    # 그래프 이쁘게 만들려고 람다식이나 그런거 쓰지 말고 그냥 정석대로 하자.
    # 단순히 나열한 것으로는... 두번째 녀석의 연결된 지점을 파악하기가 어렵다.
    global graph
    global distance

    def dijkstra(start):
        import heapq

        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for next_node in graph[now]:
                next_cost = dist + 1
                if next_cost < distance[next_node]:
                    distance[next_node] = next_cost
                    heapq.heappush(q, (next_cost, next_node))

    graph = [[] for _ in range(n)]
    for info in infos:
        graph[info[0] - 1].append(info[1] - 1)
        graph[info[1] - 1].append(info[0] - 1)
    distance = [1e9] * n
    dijkstra(0)  # 그래프를 첫번째 부터 시작할때 최단거리를 업데이트 한다.
    print("result: ", distance)
    max_value = max(distance)
    return distance.count(max_value)


def solution2(n, infos):
    import heapq

    # n은 2만 이하, vertex는 5만 이하
    INF = int(1e9)
    distance = [INF if i != 0 else 0 for i in range(n + 1)]
    # 자 먼저 정보를 가지고 그래프를 초기화 하자.
    graph = [[] for _ in range(n + 1)]
    for node1, node2 in infos:
        graph[node1].append(node2)
        graph[node2].append(node1)
    print(graph)
    h = []
    distance[1] = 0
    heapq.heappush(h, (1, 0))  # 이 정보는 1번 노드 까지 비용은 0이란 것이다.
    while h:
        node, d = heapq.heappop(h)
        # 처리된 적이 있다면 무시... 이 부분이 조금 헷갈리는데?
        if d > distance[node]:
            continue
        for n_node in graph[node]:  # 어짜피 여기서 정보가 없으면 반복문은 실행이 안된다.
            if distance[n_node] > d + 1:
                distance[n_node] = d + 1  # 계속해서 업데이트가 될 수 있는데 방문처리를 하는것이 맞나?
                heapq.heappush(h, (n_node, d + 1))
    print("distance: ", distance)
    max_v = max(distance)
    return distance.count(max_v)


print(solution2(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
