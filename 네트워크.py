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
        global visited_list
        global graph
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
                    visited_list[linked_node_idx] = True
                    queue.append(linked_node_idx)
                    count = 1

        return count

    answer = 0
    for idx, node in enumerate(graph):
        answer += bfs(idx)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


def solution2(n, computers):
    return 0
