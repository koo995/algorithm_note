# 이것을 잘 못 했구나? 이것도 재귀적으로 부모노드를 찾아 올라가야 하는 것이군...
def find_parent(node):
    if parent_table[node] == node:
        return node
    parent = find_parent(parent_table[node])
    return parent


def check_cycle(node1, node2):
    parents = sorted([find_parent(node1), find_parent(node2)])
    if parents[0] != parents[1]:
        parent_table[parents[1]] = parents[0]
        return False
    return True


def solution(n, costs: list):
    global parent_table

    total_min_cost = 0
    road_count = 0
    parent_table = [i for i in range(n)]
    ordered_by_cost_asc = sorted(costs, key=lambda cost: cost[2])
    for cost in ordered_by_cost_asc:
        c = cost[2]
        first_node = cost[0]
        second_node = cost[1]
        if check_cycle(first_node, second_node) == False:
            total_min_cost += c
            road_count += 1
        if road_count == n - 1:
            return total_min_cost


# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(
    solution(
        7,
        [
            [2, 3, 7],
            [3, 6, 13],
            [3, 5, 23],
            [5, 6, 25],
            [0, 1, 29],
            [1, 5, 34],
            [1, 2, 35],
            [4, 5, 53],
            [0, 4, 75],
        ],
    )
)

# 이 노드들이 연결되어 있다가 아닌. 순환한다는 것을 어떻게 확인하지?
# ordered_by_costs:  [[2, 3, 8], [1, 2, 5], [0, 2, 2], [0, 1, 1], [1, 3, 1]]
# 삼각형을 이룬다를 어케 해야할지 모르겠네... graph을 만들고 하긴 했는데
# 번외로 사이클을 이룬다는 것은 union을 하는 방식으로 구할 수 있구나
# 테스트에서 틀리네... 삼각형을 지운 다는 것이 틀렸을까?
# 최소신장트리라는 문제구나... 단순히 삼각형으로 가면 안되는 것이였군
# 크루스칼 알고리즘은 그리디 알고리즘의 일종입니다.
# 즉, 그래프 간선들을 가중치의 오름차순으로 정렬해 놓은 뒤, 사이클을 형성하지 않는 선에서 정렬된 순서대로 간선을 선택합니다.
