from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # 여기에서 어느시점에 False 가 호출되는 것이지? 한 노드에서 더이상 갈 곳이 없으면 for 문이 생략될 것이다.
        # true 인 경우 바로 답을 반환하는 것이고 traced을 리셋할 필요는 없지
        # 다만 false 인 경우 하나하나 다시 빼가는 것이다.
        def is_circulate(node):
            if node in traced:
                return True
            if node in visited:
                return False
            
            traced.add(node)
            for n_node in graph[node]:
                if is_circulate(n_node):
                    return True
            traced.remove(node)
            visited.add(node) # 여기에 넣은 노드로 부터는 순환을 만들지 않으니까... 가지를 쳐내는 것이다.
            return False
        
        graph = defaultdict(list)
        for start, end in prerequisites:
            graph[start].append(end)
        print("graph: ", list(graph)) # {0: [10], 3: [18], 5: [5], 6: [11], 11: [14], 13: [1], 15: [1], 17: [4]}
        print("graph: ", graph) # {0: [10], 3: [18], 5: [5], 6: [11], 11: [14], 13: [1], 15: [1], 17: [4]}
        
        traced = set()
        visited = set()
        for node in list(graph): # [0, 3, 5, 6, 11, 13, 15, 17]
            if is_circulate(node): # 순환한다면?
                return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def is_cycle(node, visited) -> bool:
            if visited[node]:
                return True
            visited[node] = 1
            if no_cycle[node]:
                return False
            for n_node in graph[node]:
                if is_cycle(n_node, visited[::]):
                    return True
                no_cycle[n_node] = True
            return False

        graph = [[] for _ in range(numCourses)]
        for dest, start in prerequisites:
            graph[start].append(dest)
        no_cycle = [False for _ in range(numCourses)]  # 이게 지금은 모두 사이클을 이룬다고 되어 있는 것이구나
        for start in range(numCourses):
            if no_cycle[start]: # 사이클을 이루지 않는 다면 넘어간다.
                continue
            if is_cycle(start, [0 for _ in range(numCourses)]):  # 사이클을 이룬다면 스케쥴 할 수 없으니까 정답인 False를 반환
                return False
            no_cycle[start] = True # 사이클을 이루지 않는 다면 탐색한 노드를 True로 할당
        return True
        # 아아... 역시 끊어져 있는 경우가 발생할 수 있다.


from collections import deque

# 이거는 위상 정렬을 이용한 것임.
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses

        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)  # b를 먼저 들어야 a도 들을 수 있다.
            in_degree[a] += 1

        q = deque()

        # 이제 진입차수가 0인 모든 노드를 큐에 넣는다.
        for num in range(numCourses):
            if in_degree[num] == 0:
                q.append(num)

        # 이제 큐에서 꺼내면서 확인한다.
        while q:
            now = q.popleft()

            for n_node in graph[now]:
                in_degree[n_node] -= 1
                if in_degree[n_node] == 0:
                    q.append(n_node)
                elif in_degree[n_node] < 0:
                    return False

        for i in range(numCourses):
            if in_degree[i] != 0:
                return False
        return True


# 이거는 책에서 본 것이다.
class Solution4:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def is_cycle(node) -> bool:
            if node in traced:
                return True

            # 현재의 호출 스택에 포함되어 있지는 않지만 방문 했던 녀석이라면? 그 말은 그때 탐색으로 사이클을 이루지 않음을 확인했다는 것이네
            if node in visited:
                return False

            traced.add(node)
            for n_node in graph[node]:
                if is_cycle(n_node):
                    return True
            visited.add(node)
            traced.remove(node)
            return False

        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()  # 이 부분이 마음에 안들어서 특정 노드가 사이클을 이루는지 안 이루는지 체크해둘려고 했는데
        traced = set()
        for i in range(numCourses):
            if is_cycle(i):
                return False
        return True


# 그래프의 각 노드들에 대해서 순환을 이루면 안된다가 문제이다. 그 말은 서로 순환을 이루지 않는 다른 집합들이 있을 수 있단것이지
# 각 노드들은 본인을 부모로 가지고 있고... 서로 부모가 다르다면 사이클을 이루지 않는다가 되는 것이다.
# 나는 처음 호출한 녀석이 재귀적으로 올라가다가 원래 녀석을 닿으면 뭔가를 어떻게 반환할려고 했는데 실패함
# visited 을 추가해서 가지치기라는 것을 햇다...
sol = Solution()
sol.canFinish(7, [[0,1], [1,2], [2,3], [2,5], [5,6], [3,4]])
# sol.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])
# sol.canFinish(100, [[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9],[11,9],[11,10],[12,10],[12,11],[13,11],[13,12],[14,12],[14,13],[15,13],[15,14],[16,14],[16,15],[17,15],[17,16],[18,16],[18,17],[19,17],[19,18],[20,18],[20,19],[21,19],[21,20],[22,20],[22,21],[23,21],[23,22],[24,22],[24,23],[25,23],[25,24],[26,24],[26,25],[27,25],[27,26],[28,26],[28,27],[29,27],[29,28],[30,28],[30,29],[31,29],[31,30],[32,30],[32,31],[33,31],[33,32],[34,32],[34,33],[35,33],[35,34],[36,34],[36,35],[37,35],[37,36],[38,36],[38,37],[39,37],[39,38],[40,38],[40,39],[41,39],[41,40],[42,40],[42,41],[43,41],[43,42],[44,42],[44,43],[45,43],[45,44],[46,44],[46,45],[47,45],[47,46],[48,46],[48,47],[49,47],[49,48],[50,48],[50,49],[51,49],[51,50],[52,50],[52,51],[53,51],[53,52],[54,52],[54,53],[55,53],[55,54],[56,54],[56,55],[57,55],[57,56],[58,56],[58,57],[59,57],[59,58],[60,58],[60,59],[61,59],[61,60],[62,60],[62,61],[63,61],[63,62],[64,62],[64,63],[65,63],[65,64],[66,64],[66,65],[67,65],[67,66],[68,66],[68,67],[69,67],[69,68],[70,68],[70,69],[71,69],[71,70],[72,70],[72,71],[73,71],[73,72],[74,72],[74,73],[75,73],[75,74],[76,74],[76,75],[77,75],[77,76],[78,76],[78,77],[79,77],[79,78],[80,78],[80,79],[81,79],[81,80],[82,80],[82,81],[83,81],[83,82],[84,82],[84,83],[85,83],[85,84],[86,84],[86,85],[87,85],[87,86],[88,86],[88,87],[89,87],[89,88],[90,88],[90,89],[91,89],[91,90],[92,90],[92,91],[93,91],[93,92],[94,92],[94,93],[95,93],[95,94],[96,94],[96,95],[97,95],[97,96],[98,96],[98,97],[99,97]])