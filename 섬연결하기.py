def check_tri(cost):
    answer = False
    first_node = cost[0]
    second_node = cost[1]
    if graph[first_node] & graph[second_node]:
        answer = True
        graph[first_node].remove(second_node)
        graph[second_node].remove(first_node)
    return answer


def solution(n, costs: list):
    # costs로 부터 연결관계에 대한 그래프를 미리 구할까?
    global graph
    graph = [set() for _ in range(n)]
    for cost in sorted(costs, key=lambda cost: cost[0]):
        f_node, s_node, c = cost
        graph[f_node].add(s_node)
        graph[s_node].add(f_node)

    ordered_by_costs = sorted(costs, key=lambda cost: cost[2], reverse=True)

    total_cost = sum([cost[2] for cost in costs])
    for cost in ordered_by_costs:
        if check_tri(cost) == True:
            total_cost -= cost[2]

    return total_cost


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

# 이 노드들이 연결되어 있다가 아닌. 순환한다는 것을 어떻게 확인하지?
# ordered_by_costs:  [[2, 3, 8], [1, 2, 5], [0, 2, 2], [0, 1, 1], [1, 3, 1]]
# 삼각형을 이룬다를 어케 해야할지 모르겠네... graph을 만들고 하긴 했는데
# 테스트에서 틀리네... 삼각형을 지운 다는 것이 틀렸을까?
# 최소신장트리라는 문제구나... 단순히 삼각형으로 가면 안되는 것이였군
# 크루스칼 알고리즘은 그리디 알고리즘의 일종입니다.
# 즉, 그래프 간선들을 가중치의 오름차순으로 정렬해 놓은 뒤, 사이클을 형성하지 않는 선에서 정렬된 순서대로 간선을 선택합니다.
