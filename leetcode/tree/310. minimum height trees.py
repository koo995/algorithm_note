class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 가장 최소가 되는 트리의 루트를 찾을려면... 가장 바깥쪽 부터 안쪽으로 그래프를 탐색해야한다.
        # 그렇게 가장 가운데에 있는 녀석들을 찾아야한다.
        # 그럴려면 리프노드를 구해야하는데... 어케하지?
        leaf_nodes = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaf_nodes.append(i)
        while n > 2:
            n -= len(leaf_nodes)
            new_leaf_nodes = []
            for leaf_node in leaf_nodes:
                neighbor = graph[leaf_node].pop()
                graph[neighbor].remove(leaf_node)

                if len(graph[neighbor]) == 1:
                    new_leaf_nodes.append(neighbor)
            leaf_nodes = new_leaf_nodes
        return leaf_nodes