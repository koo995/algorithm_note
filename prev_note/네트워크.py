def solution(n, computers):
    from collections import deque

    global graph
    global visited_list

    # 우선 computers에서 받은것을 조금 수정해 볼까?
    graph = [
        (
            lambda node_computer: [
                linked_idx
                for linked_idx, linked_computer in enumerate(node_computer)
                if linked_computer == 1 and linked_idx != node_idx
            ]
        )(node_computer)
        for node_idx, node_computer in enumerate(computers)
    ]

    visited_list = [False] * n

    def bfs(idx):
        count = 0
        queue = deque()

        if visited_list[idx] != True:
            visited_list[idx] = True
            queue.append(idx)
            count = 1

        while queue:
            current_node_idx = queue.pop()
            for linked_node_idx in graph[current_node_idx]:
                if visited_list[linked_node_idx] != True:
                    visited_list[linked_node_idx] = True  # 여기서 방문처리를 하고 queue에 넣어주는구나.
                    queue.append(linked_node_idx)
                    count = 1

        return count

    answer = 0
    for idx, node in enumerate(graph):
        answer += bfs(idx)  # bfs로 돌아가면서... 연결되어 있는지

    return answer


def solution2(n, computers):
    parent_table = [i for i in range(n)]  # 우선은 자기자신을 부모로 가지고 잇다.

    def find_parent(node):  # 그렇다면 여기서 초기화를 시켜줄려면?
        if parent_table[node] != node:
            parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def find_parent2(node):  # 그렇다면 여기서 초기화를 시켜줄려면?
        if parent_table[node] != node:
            return parent_table[node]
        return node

    def union(node1, node2):
        p1 = find_parent(node1)
        p2 = find_parent(node2)
        if p1 > p2:
            parent_table[p1] = p2  # 어쨋든 p2가 더 작은 녀석이다...
        else:
            parent_table[p2] = p1

    # 자 여기서 이제 서로 연결관계를 만들어 줘야 겠지
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)

    # 이 연산을 통해서 모든 노드의 부모를 최상단으로 초기화시켜준다.
    for node in range(n):
        find_parent(node)

    parent_table.sort()
    count = 1
    prev = parent_table[0]
    for p in parent_table[1:]:
        if prev != p:
            count += 1
            prev = p
    return count


print(solution2(10, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
