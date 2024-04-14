class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import defaultdict
        
        def dfs(node):
            if node in traced:
                return False
            traced.add(node)
            for n_node in graph[node]:
                if not dfs(n_node):
                    return False
            traced.remove(node)
            return True
        
        graph = defaultdict(list)
        for start, end in prerequisites:
            graph[start].append(end)
        
        traced = set()
        for node in list(graph):
            if not dfs(node): # 순환한다면?
                return False
        return True
        
# 그래프의 각 노드들에 대해서 순환을 이루면 안된다가 문제이다. 그 말은 서로 순환을 이루지 않는 다른 집합들이 있을 수 있단것이지
# 각 노드들은 본인을 부모로 가지고 있고... 서로 부모가 다르다면 사이클을 이루지 않는다가 되는 것이다.
# 나는 처음 호출한 녀석이 재귀적으로 올라가다가 원래 녀석을 닿으면 뭔가를 어떻게 반환할려고 했는데 실패함