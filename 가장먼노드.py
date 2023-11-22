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


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
