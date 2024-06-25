import heapq


def solution1():
    T = int(input())
    for _ in range(T):
        vertex_n, road_n, dest_candi_n = map(int, input().split())  # 교차로, 도로, 목적지 후보의 개수
        start, point_g, point_h = map(int, input().split())
        lines = [tuple(map(int, input().split())) for _ in range(road_n)]
        graph = [[] for _ in range(vertex_n + 1)]

        for node1, node2, d in lines:
            graph[node1].append((node2, d))
            graph[node2].append((node1, d))
        destination_candidates = [int(input()) for _ in range(dest_candi_n)]
        # 다익스트라를 구현하면 되겠다.
        q = []
        pre_table = [i for i in range(vertex_n + 1)]
        dp = [int(1e9) for _ in range(vertex_n + 1)]
        dp[start] = 0
        heapq.heappush(q, (start, 0))
        while q:
            node, dist = heapq.heappop(q)
            if dist > dp[node]:
                continue
            for n_node, n_dist in graph[node]:
                if dp[n_node] > dist + n_dist:
                    dp[n_node] = dist + n_dist
                    pre_table[n_node] = node
                    heapq.heappush(q, (n_node, dp[n_node]))
        result = []
        for dest in destination_candidates:
            # dest 의 경로를 구해보자
            now = dest
            while now != start:
                prev = pre_table[now]
                if (now == point_h and prev == point_g) or (now == point_g and prev == point_h):
                    result.append(dest)
                now = prev
        print(*sorted(result))


def solution2():
    def dijkstra(start):
        q = []
        dp = [int(1e9) for _ in range(vertex_n + 1)]
        dp[start] = 0
        heapq.heappush(q, (start, 0))
        while q:
            node, dist = heapq.heappop(q)
            if dist > dp[node]:
                continue
            for n_node, n_dist in graph[node]:
                if dp[n_node] > dist + n_dist:
                    dp[n_node] = dist + n_dist
                    heapq.heappush(q, (n_node, dp[n_node]))
        return dp

    T = int(input())
    for _ in range(T):
        vertex_n, road_n, dest_candi_n = map(int, input().split())  # 교차로, 도로, 목적지 후보의 개수
        s, point_g, point_h = map(int, input().split())
        lines = [tuple(map(int, input().split())) for _ in range(road_n)]
        graph = [[] for _ in range(vertex_n + 1)]
        for node1, node2, d in lines:
            graph[node1].append((node2, d))
            graph[node2].append((node1, d))
        destination_candidates = [int(input()) for _ in range(dest_candi_n)]
        # 다익스트라를 구현하면 되겠다.
        min_dist = dijkstra(s)
        min_dist_start_g = dijkstra(point_g)
        min_dist_start_h = dijkstra(point_h)
        result = []
        for dest_node in destination_candidates:
            if (min_dist[dest_node] == min_dist[point_g] + min_dist_start_g[point_h] + min_dist_start_h[dest_node]) \
                    or (
                    min_dist[dest_node] == min_dist[point_h] + min_dist_start_h[point_g] + min_dist_start_g[dest_node]):
                result.append(dest_node)
        print(*sorted(result))

# 아하... 똑같은 거리지만... 경로가 다를 수 잇구나

