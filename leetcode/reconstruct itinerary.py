from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            print("a", a)
            while graph[a]:
                dfs(graph[a].pop())
            print("route: ", route)
            route.append(a)
        dfs('JFK')
        return route[::-1]

    
    
    def findItinerary2(self, tickets: list[list[str]]) -> list[str]:
        ticket_map = defaultdict(list)
        for from_node, to_node in sorted(tickets):
            if to_node not in ticket_map[from_node]:
                ticket_map[from_node].append(to_node)
        def dfs(c_node, path, remain_tickets):
            if not remain_tickets:
                return path
            for n_node in ticket_map[c_node]:
                if [c_node, n_node] not in remain_tickets:
                    continue
                n_remain_tickets = remain_tickets.copy()
                n_remain_tickets.remove([c_node, n_node])
                n_path = path.copy()
                n_path.append(n_node)
                result = dfs(n_node, n_path, n_remain_tickets)
                if result:
                    return result
        return dfs('JFK',['JFK'], tickets)
# 지금보니까 이새끼들 티켓이 중복으로 주어지기도 하네. 맵 자체를 중복을 제거하니 문제가 해결되었으나... 실행속도가 최악이다.
sol = Solution()
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))