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
    import copy

    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)

    result = []

    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']})
    def dfs(node: str, tickets: list, answer: list) -> None:
        # 종료조건... 티켓을 모두다 소모했다?
        if not tickets:
            result.append(answer)
            return
        for n_node in graph[node]:
            # 왔던 길을 또 올 수 있잖아? 그것에 대한 중복을 없애기 위해서 티켓을 제거하는데..
            # 와... 이거 뭔 차이야? deepcopy()는 시간 오류뜨고... copy()는 성공이고...
            # 아! 단순히... 테스트케이스 1번이 어머어마한 연산때문에 deepcopy()가 시간초과가 발생하는 것...
            # 한가지 중요한 것은 역시 할당과 얕은 복사의 차이!
            # tmp_tickets = copy.deepcopy(tickets)
            tmp_tickets = tickets.copy()
            print(f"id: {id(tmp_tickets)}, tickets: {tmp_tickets}")
            tmp_answer = answer.copy()
            if [node, n_node] in tmp_tickets:
                tmp_tickets.remove([node, n_node])
                tmp_answer.append(n_node)
                dfs(n_node, tmp_tickets, tmp_answer)

    print(f"id: {id(tickets)}, tickets: {tickets}")
    start = "ICN"
    dfs(start, tickets, [start])
    print("result: ", result)


print(
    solution3(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)

# 방금 알았는데.... 이중리스트인데도 정렬이 가능하네....?
# 근데.. 과연 이렇게 재귀함수 안에... 가변객체를 넣어두는 것이 괜찮은가?
# 자 문제는 과연 dic인데... dic에 대해서 안에 원소들이 없더라도 키값만 있는것으로도 그 길이는 키에 해당하는구나...
