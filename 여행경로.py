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
                dfs(
                    dest, current_tickets, tmp_answer
                )  # 여기서 이 tickets가 제거된 녀석을 원하지

    answer_list = []
    # answer.append(start)
    dfs(start, tickets, [start])
    print("answer_list: ", answer_list)
    return answer_list


# 엥 맞췄네... 뭐... 얼추 그럴꺼 같긴 했는데...
# 뭐 어쨋든 지역변수를 어떻게 맞춰갈까를 잘 정해서 다행이다...
# 문제를 잘 파악하고 계획을 짜는 것이 역시 중요해...
# 위의 코드... 운이 좋아서 통과한거지 아니 그냥 뭣도 모르고 그리디로 간거 같은데?


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

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if graph[top] != []:
            stack.append(graph[top].pop(0))
        else:
            path.append(stack.pop())
    return path[::-1]


def solution3(tickets: list):
    from collections import defaultdict
    import time

    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
    for key in graph.keys():
        graph[key].sort(reverse=True)

    # 길은 반드시 있을 것이고... 그리디하게 가도 될것 같은데?
    # while문을 사용할 방법은 뭐가 있을가
    # 그래프는 {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}
    # 완료라는 것은 tickets을 모두 소모했거나... 어쨋든 모두 소모한 경우인데,
    stack = ["ICN"]
    result = [start]
    while stack:  # 확실한 것은 티켓을 다 소모했다는 것이 필요하다
        # 티켓을 다 소모할때 까지 반복문을 돌린다.
        # 먼저 start에 해당하는 노드에서 그리디하게 다음 노드를 선택한다.
        # 그리디하게 선택했지만 길이 없는 곳일 수 있다.
        # 그렇다면 다음 노드를 선택해야 할 것이다.
        # 그렇다면 다음 노드를 선택하기 위해서는... 한 노드에서 연결된 노드들을 담아줄 변수가 필요하다.
        # 그렇다면 성공조건은 어떻게 하나? 더이상 방문해야할 곳이 없다. 즉 모든 곳을 방문했다? 둘이 똑같은 말이다 경우에 따라서는 두가지중 하나를 선택하는 것이 맞다.
        if graph[start]:  # 여기에 여러개가 3있을 수 있단 것이지
            next_node = stack.pop()  # 최대한 그리디하게 가는 것이다.
            result.append(next_node)  # 이렇게 하면 제일 빠른 녀석이 나올 것이다.
            start = next_node
        else:
            next_node = stack.pop()

    print("results: ", results)
    # 그리기하게 가도 되겠지만 경우를 다 찾고 정렬해서 빠른 녀석을 답으로 제출한다.
    # 하지만 잘 생각해보니 모든 경로중에서... 글자가 앞선 녀석을 선택한다? 어떻게? 그건 안되겠는데?
    # 그렇다면 처음부터 쩔수없이 그리디하게 가능 방법?
    pass


print(
    solution3(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
