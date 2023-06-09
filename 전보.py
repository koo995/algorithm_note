import sys
import heapq
input = sys.stdin.readline

n, m, start = map(int, input().split()) # 도시의 갯수, 통로의 갯수, 출발지
INF = int(1e9)
graph = [[] for _ in range(n+1)] # index로 그래프를 표현하자
final_cost = [INF]*(n+1) # 걸리는 시간을 담을 변수
#통로의 정보
for _ in range(m): # 통로의 갯수만큼
    x, y, z = map(int, input().split()) # x에서 y로 비용은 z 이다
    graph[x].append((y, z))
    
def dijkstra(start):
    q = []
    final_cost[start] = 0
    heapq.heappush(q, (final_cost[start], start))
    while q: # 힙에 들어온 후로 처리를 시작한다
        cost, now_node = heapq.heappop(q)
        if final_cost[now_node] < cost:
            continue
        for linked_node in graph[now_node]:
            next_node = linked_node[0] # 목적지
            next_cost = cost + linked_node[1] # 비용
            if next_cost < final_cost[next_node]:
                final_cost[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))

dijkstra(start)

count = 0
total_time = 0
for i in final_cost:
    if i != INF:
        count +=1
        total_time = max(total_time, i)
print(count-1, total_time) 


# 어잿든 이 문제는 최단 경로 문제인 것을 보면 알려나?
# 주어진 조건의 수가 너무 크가 애초에 플로이드워셜은 안되겠어.
# count에서 시작노드는 제거해야 했어.
# 2치원 그래프를 생성하는데 문제가 있었어