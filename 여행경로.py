from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for start, dest in tickets:
        graph[start].append(dest)
    print("graph: ", graph)
    start = "ICN"

    def dfs(start, tickets: list, answer: list):
        print("현재 티켓들: ", tickets)
        if not tickets:
            answer_list.append(answer)
            return
        sorted_node = sorted(graph[start])
        for dest in sorted_node:
            tmp_answer = answer.copy()
            tmp_answer.append(dest)
            current_tickets = tickets.copy()
            print("ticket: ", [start, dest])
            if [start, dest] in current_tickets:  # 여기서 먼저 넣었다 하더라도...
                current_tickets.remove([start, dest])
                dfs(dest, current_tickets, tmp_answer)  # 여기서 이 tickets가 제거된 녀석을 원하지

    answer_list = []
    # answer.append(start)
    dfs(start, tickets, [start])
    print("answer_list: ", answer_list)
    return answer_list


# 엥 맞췄네... 뭐... 얼추 그럴꺼 같긴 했는데...
# 뭐 어쨋든 지역변수를 어떻게 맞춰갈까를 잘 정해서 다행이다...
# 문제를 잘 파악하고 계획을 짜는 것이 역시 중요해...

print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))


# 다른사람 풀이
def solution1(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]


# 다른사람 풀이
def solution2(tickets):
    graph = defaultdict(list)
    for start, dest in tickets:
        graph[start].append(dest)
    for start in graph.keys():
        graph[start].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if graph[q] != []:
            s.append(graph[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]
