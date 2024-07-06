n, m = map(int, input().split()) # 회사 갯수, 경로 갯수

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m): # 그래프 초기화
    a, b = map(int, input().split()) # a와 b는 연결되어 있다.
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int, input().split()) # 목적지, 경유지

for i in range(1, n+1):
    graph[i][i] = 0 # 자기 자신에게는 0의 비용

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else: print(distance)










# 어떤 알고리즘을 써야할까 목적지 경유지 다 주어지구나? 그러면 그것에 대한 케이스만 고려하면 되는거 아냐?
# 경유지까지 최소를 구하고, 경유지에서 목적지 까지 최소를 구해서 더하면 되겠네?
# 만약에 말야 어떤 위치까지 2개 이상을 거쳐야 도달할 수 있다면 어케함?
# 아하... 첫번째 for 문이 경유지이고 매번 a에서 b까지를 확인하게 되는 것이구나...