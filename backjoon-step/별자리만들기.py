import math


def solution():
    def find_parent(node):
        if node == parent_table[node]:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def union(node1, node2):
        p1 = find_parent(node1)
        p2 = find_parent(node2)
        if p1 == p2:
            return False
        else:
            if p1 > p2:
                parent_table[p1] = p2
            else:
                parent_table[p2] = p1
            return True


    def get_dist(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2,), 2)

    n = int(input())
    graph = [tuple(map(float, input().split())) for _ in range(n)]
    graph_with_dist = []
    for i in range(n):
        for j in range(i + 1, n):
            node1 = graph[i]
            node2 = graph[j]
            dist = get_dist(node1, node2)
            graph_with_dist.append((i, j, dist))

    graph_with_dist.sort(key=lambda line:line[2])
    parent_table = [i for i in range(n)]
    min_dist = 0
    for n1, n2, dist in graph_with_dist:
        if union(n1, n2):
            min_dist += dist
    print(min_dist)


solution()


# 모든 거리를 구하는 것 4950 밖에 안하니까 할만하다.