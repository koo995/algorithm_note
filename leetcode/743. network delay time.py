from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, duration in times:
            graph[start].append((end, duration))
            
        q = [(0, k)]
        dist = defaultdict(int)
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for n_node, n_time in graph[node]:
                    alt = time + n_time
                    heapq.heappush(q, (alt, n_node))
    
    def networkDelayTime2(self, times: list[list[int]], n: int, k: int) -> int:
        # 제일 먼 거리까지의 시간을 구하면 되는 것이군
        INF = int(1e9)
        graph = [[] for _ in range(n + 1)]
        for start, end, duration in times:
            graph[start].append((end, duration))
        arrive_time = [INF] * (n + 1)
        def dijkstra(start):
            import heapq
            
            arrive_time[start] = 0
            q = []
            heapq.heappush(q, (arrive_time[start], start))
            while q:
                t, node = heapq.heappop(q)
                if arrive_time[node] < t:
                    continue
                for n_node, n_t in graph[node]:
                    if arrive_time[n_node] > t + n_t:
                        arrive_time[n_node] = t + n_t
                        heapq.heappush(q, (arrive_time[n_node], n_node))
        
        dijkstra(k)
        return max(arrive_time[1:]) if max(arrive_time[1:]) != INF else -1
    
sol = Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))