from collections import deque

def solution(relationships, target, limit): # limit은 100미만
    relationships.sort()
    # 그래프를 먼저 초기화 했다.
    graph = [[] for _ in range(101)]
    for i in relationships: # 최대 4000
        s = i[0]
        e = i[1]
        if e not in graph[s]:
            graph[s].append(e)
        if s not in graph[e]:
            graph[e].append(s)
    print("graph", graph)
    limit_table = bfs(graph, target)
    n_f = []
    for idx, l in enumerate(limit_table):
        if 1 < l <= limit:
            n_f.append(idx)
    print("n_f",n_f)
    
    
    answer = 0
    return answer


def bfs(graph, target):
    visited = [0] * 101
    dist = [0] * 101
    q = deque()
    d = 0 # 각 bfs 마다 얼마만큼의 거리인지 체크하기 위함.
    q.append([target, d])
    while q:
        cur_node, d = q.popleft()
        visited[cur_node] = 1
        dist[cur_node] = d
        for i in graph[cur_node]: # 아무것도 없다면 무시되겠지
            if visited[i] == 0:
                q.append([i, d+1]) # bfs의 한 바운드? 이후 녀석들은 1씩 더해줘서 정보를 준다.
    print("visited:", visited)    
    print("dist",dist)
    return dist 




solution([[1,2],[2,3],[2,6],[3,4],[4,5]], 2, 3)
solution([[1,2],[2,3],[2,6],[3,4],[4,5]], 1, 2)






    