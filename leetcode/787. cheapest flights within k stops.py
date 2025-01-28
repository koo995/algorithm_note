from collections import defaultdict
import heapq

class Solution:
    # 단순히 bfs를 이용하는 것이 맞을까? 단순히 bfs을 사용해야할 이유를 모르겠다.
    # 현재 메모리 초과가 발생한다...
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
            
        def bfs(node):
            from collections import deque
            
            INF = int(1e4)
            prices = [INF] * n
            prices[node] = 0
            q = deque()
            q.append((node, 0, 0))
            while q:
                node, price, count = q.popleft()
                if count > K :
                    break
                for n_node, n_price in graph[node]:
                    prices[n_node] = min(prices[n_node], n_price + price)
                    q.append((n_node, prices[n_node], count + 1))
            return prices[dst] if prices[dst] < INF else -1
        
        return bfs(src)

    def findCheapestPrice2(self, n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        Q = [(0, src, K)]
        
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        return -1
        # 이것도 시간초과가 발생한다.


    def findCheapestPrice1(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e9)
        distance = [[(INF, 0)] * n for _ in range(n)]
        for s, e, d in flights:
            distance[s][e] = (d, 0)
        for q in range(n):
            for s in range(n):
                for e in range(n):
                    if s == e:
                        continue
                    dist, _ = distance[s][e]
                    if dist > distance[s][q][0] + distance[q][e][0] and distance[s][q][1] + distance[q][e][1] + 1 <= k:
                        distance[s][e] = (distance[s][q][0] + distance[q][e][0], distance[s][q][1] + distance[q][e][1] + 1)
        return distance[src][dst][0] if distance[src][dst][0] < INF else -1

    def findCheapestPrice3(self, n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
        # 경유를 해야하는데 k 개 이네에 성공해야하네? 흠... 다익스트라
        # n이 겨우 100 이면 플로이드와샬도 가능은 한데... 경우되는 것의 갯수를 구할 수 있나?
        # 다 익스트라는 한점에서 모든 점까지의 최단 거리를 구하는 것이다. 비용을 계산 하면서 stop의 갯수를 저장할 수 있겠는데?
        graph = [[] for _ in range(n)]
        for start, end, cost in flights:
            graph[start].append((end, cost))
        INF = int(1e9)
        distance = [INF for _ in range(n)]
        distance[src] = 0
        q = [(0, 0, src)]
        # n이 100 이하라는 것을 생각해서... 처리된 것은 다시 처리하지 않는 최적화를 없애고 초기화를 한단계 미루었다.
        while q:
            stop_count, dist, node = heapq.heappop(q)
            if distance[node] > dist:
                distance[node] = dist
            if stop_count > K:
                continue
            for n_node, n_dist in graph[node]:
                if distance[n_node] > dist + n_dist:
                    heapq.heappush(q, (stop_count + 1, dist + n_dist, n_node))
        return distance[dst] if distance[dst] != INF else -1

    # 이게 마지막으로 새롭게 푼 풀이이다.
    # 지금까지 이상하게 풀었네... 거리초기화를 왜 노드에서 탐색한 뒤에 했냐?
    # 그냥 넥스트 노드 탐색할 때 바로 초기화를 하면 되는 것인데...
    def findCheapestPrice4(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for s, e, c in flights:
            graph[s].append((e, c))

        INF = int(1e9)
        distance = [INF] * n
        distance[src] = 0

        h = []
        heapq.heappush(h, (0, 0, src))
        while h:
            vertex_count, cost, cur_node = heapq.heappop(h)

            if vertex_count > k:  # 마지막 노드도 카운트에 들어가니까 딱 맞게 가져가도 될듯
                continue

            if distance[cur_node] > cost:
                continue

            for n_node, n_cost in graph[cur_node]:
                if distance[n_node] > cost + n_cost:
                    distance[n_node] = cost + n_cost
                    heapq.heappush(h, (vertex_count + 1, cost + n_cost, n_node))

        return distance[dst] if distance[dst] != INF else -1
        # k번의 경유지를 거쳐서
        # 기존의 다익스트라에서 문제는 그리디하기 때문에... K번의 경유지를 거쳐서 목적지까지 도착해야하는데
        # 다익스트라를 하면 K번 이상으로 목적지를 거쳐서 가장 빠른 길로 갈 수 있다는 것이다.
        # 이걸 방지해야한다. 최대 K번 이내에서 탐색이 이루어져야 하니 K번 보다 크다면? continue로 탐색을 그만둬버린다.
        # 즉 경유지 숫자를 제한할 필요가 있는데... 우선순위큐에는 비용이 가장 짧은 것으로 넣기는 무리다.
        # 그렇다면 경유지 순으로 정렬을 하고 같다면 비용순으로 정렬을 할까?


        
sol = Solution()
print(sol.findCheapestPrice(17, [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
, 13, 4, 13))

#플로이드 워샬로 풀었을때 이 케이스에서 통과하지 못했다. 이유야 자명하다. 그래프를 그려보니... 최단거리로 바로 업데이트 해버리니 답을 찾을 수가 없구나