from collections import deque, defaultdict
import time


def solution(info, edges):
    edges.sort(key=lambda edge: edge[0])
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)
    print(f"{graph} 크기는 {len(graph)}")

    # count는 양, 늑대
    # answer은 하나의 객체로 계속해서 그냥 업데이트 될 것이다.
    def dfs(start, count, visited):
        print(f"{start}노드 방문함. 현재 count는 {count} answer: {answer}")
        print("visited: ", visited)
        time.sleep(1)
        # 여기서가 종료조건이다
        sheep_count, wolf_count = count
        if sheep_count <= wolf_count or (
            0 not in visited
        ):  # 탐색을 그만해야하는데... 그냥 되돌아간다.
            return
        else:  # 일단은 양이 더 많으면 기록을 한다.
            answer.append(sheep_count)
        for node in graph[start]:
            if visited[node] == 0:
                visited[node] = 1
                if info[node]:
                    dfs(node, [sheep_count, wolf_count + 1], visited)
                else:
                    dfs(node, [sheep_count + 1, wolf_count], visited)
                visited[node] = 0
        return

    answer = []
    visited = [0] * len(info)
    start = 0
    visited[start] = 1
    dfs(start, [1, 0], visited)  # 양도 0명 늑대도 0명, 방문테이블도 넣어주자.
    return max(answer)


def solution1(info, edges):
    from collections import deque
    import time

    edges.sort(key=lambda edge: edge[0])
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        graph[parent].append(child)
    print(f"{graph} 크기는 {len(graph)}")

    def dfs(start, count, have2visit: set):
        print(f"{start}노드 방문함. 현재 count는 {count}, have2visit:{have2visit}")
        sheep_count, wolf_count = count
        if sheep_count <= wolf_count:  # 탐색을 그만해야하는데... 그냥 되돌아간다.
            return
        else:  # 일단은 양이 더 많으면 기록을 한다.
            answer.append(sheep_count)
            for node in graph[start]:
                have2visit.add(node)

        # 재귀가 어떻게 흘러가는지는 알겠으나... 방문해야할 집합을 정하고 그 부분만 방문한다는 것이 쉽지가 않네?
        for node in have2visit:
            # 자... 여기서 have2visit을 넘겨줄때... 본인을 빼고 넘겨줘야 하는데 어떻게? 빼고 넘겨줄까? 아니면 넘겨준다음 뺄까?
            if info[node]:
                dfs(node, [sheep_count, wolf_count + 1], have2visit - set([node]))
            else:
                dfs(node, [sheep_count + 1, wolf_count], have2visit - set([node]))
        return

    answer = []
    have2visit = set()
    start = 0
    dfs(start, [1, 0], have2visit)  # 양도 0명 늑대도 0명, 방문테이블도 넣어주자.
    return max(answer)


def solution2(info, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    def dfs(cur, sheep, wolf, next_set):
        sheep += info[cur] ^ 1
        wolf += info[cur]

        if sheep <= wolf:
            return
        if sheep > wolf:
            global answer
            answer = max(answer, sheep)
            for next_ in next_set:
                temp = set(graph.get(next_, []))
                next_set |= temp  # 여기서 다음에 들어가야할 노드를 방문해야할 노드에 추가해 준다.
                next_set -= set([next_])  # 그리고 여기서 현재 노드를 빼준다.
                dfs(next_, sheep, wolf, next_set)
                next_set |= set([next_])
                next_set -= temp

    dfs(0, 0, 0, set(graph.get(0)))
    print(answer)
    return answer


# dfs도 방문처리를 재귀를 타기 전에 방문했다고 한다?
# graph = [[1, 8], [2, 4], [], [], [3, 6], [], [5], [], [7, 9], [10, 11], [], []]

# print(
#     solution(
#         [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#         [
#             [0, 1],
#             [0, 2],
#             [1, 3],
#             [1, 4],
#             [2, 5],
#             [2, 6],
#             [3, 7],
#             [4, 8],
#             [6, 9],
#             [9, 10],
#         ],
#     )
# )


# edges이 부분을 처리하는 것이 좋을까 아니면 원본 그대로에서 탐색을 할까? 0번 노드를 방문했다면 1번과 8번을 방문해야한다는 것을 알아야해.
# 그러니까 조작을 좀 해줄까? 그런데 많아봐야 2개가 끝이야. 이 문제는 이진트리와 완전탐색이 합쳐져 있다.
# 음... 그렇지만 8번에 연결되어 있다 했을때 edges에서 8로 시작하는 녀석을 찾아나가야 한다. 그러면 지금 그냥 미리 그래프를 만들어놓자.
# 사람에 따라서는 굳이 정보를 조작해서 그래프로 만들 필요는 없구나...


def solution3(info, edges):
    from collections import deque

    edges.sort(key=lambda edge: edge[0])
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)

    def dfs(start, count, have2visit: set):
        sheep_count, wolf_count = count
        if sheep_count <= wolf_count:  # 탐색을 그만해야하는데... 그냥 되돌아간다.
            return
        else:  # 일단은 양이 더 많으면 기록을 한다.
            answer.append(sheep_count)
            for node in graph[start]:
                have2visit.add(node)

        for node in have2visit:
            # 자... 여기서 have2visit을 넘겨줄때... 본인을 빼고 넘겨줘야 하는데 어떻게? 빼고 넘겨줄까? 아니면 넘겨준다음 뺄까?
            if info[node]:
                dfs(node, [sheep_count, wolf_count + 1], have2visit - set([node]))
            else:
                dfs(node, [sheep_count + 1, wolf_count], have2visit - set([node]))

    answer = []
    have2visit = set()
    start = 0
    dfs(start, [1, 0], have2visit)  # 양도 0명 늑대도 0명, 방문테이블도 넣어주자.
    return max(answer)


def solution4(info, edges):
    from collections import defaultdict

    edges.sort(key=lambda x: x[0])
    dic = defaultdict(list)
    for e1, e2 in edges:
        dic[e1].append(e2)

    def dfs(start, sheep_and_wolf, to_visit: set):
        sheep_count, wolf_count = sheep_and_wolf
        if sheep_count > wolf_count:
            result.append(sheep_count)
        else:  # 더이상 탐색이 불가능하다 무언가를 반환할것도 아니가.
            return
        for edge in dic[start]:
            to_visit.add(edge)
        for edge in to_visit:
            if info[edge]:  # 여기가 1인것은 양이라는 말이니까
                dfs(edge, [sheep_count, wolf_count + 1], to_visit - set([edge]))
            else:
                dfs(edge, [sheep_count + 1, wolf_count], to_visit - set([edge]))

    # 여기서 하나 다른게 생긴다... 방문했던 지역도 재 방문이 가능하며... 아닌가? 방문여부 안채크하고
    # 방문해야할 테이블을 정해야할까? 아니면 방문했던 것을 기록할까? 아니면 둘다?
    # 애초에 이런 경우 재귀적인 경우 어떻게 시간복잡도를 계산하지? 재귀적인것은 for문과 같다고 봐야할까
    start = 0
    sheep_and_wolf = [1, 0]
    to_visit = set()
    result = []
    dfs(
        start, sheep_and_wolf, to_visit
    )  # 무엇을 return 할까? 라기보단... return 하는 것은 없고 전역 변수인 result에 값을 계속 없데이트해 나가자
    print("result: ", result)
    return max(result)


def solution5(info, edges):
    from collections import defaultdict

    edges.sort(key=lambda x: x[0])
    dic = defaultdict(list)
    for e1, e2 in edges:
        dic[e1].append(e2)
    # 비트마스킹을 이용한 메모이제이션기법을 사용해보자

    pass


print(
    solution4(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [
            [0, 1],
            [1, 2],
            [1, 4],
            [0, 8],
            [8, 7],
            [9, 10],
            [9, 11],
            [4, 3],
            [6, 5],
            [4, 6],
            [8, 9],
        ],
    )
)

## 바킹독 풀이

l = [-1] * 20  # 왼쪽 자식
r = [-1] * 20  # 오른쪽 자식
val = []  # 양/늑대 값
n = 0
ans = 1
vis = [0] * (1 << 17)  # vis[x] : 상태 x를 방문했는가?


def solve(state):
    global ans
    if vis[state]:
        return None
    vis[state] = 1
    # wolf : 늑대의 수, num : 전체 정점의 수
    wolf, num = 0, 0
    for i in range(n):
        if state & (1 << i):
            num += 1
            wolf += val[i]
    # 만약 늑대가 절반 이상일 경우 방문할 수 없는 상태이니 종료
    if 2 * wolf >= num:
        return None
    # 현재 state의 양의 수가 ans보다 클 경우 ans를 갱신
    ans = max(ans, num - wolf)

    # 이제 다음 상태로 넘어갈 시간
    for i in range(n):
        if not state & (1 << i):
            continue
        # 현재 보고 있는 i번째 정점의 left가 있다면
        if l[i] != -1:
            solve(state | (1 << l[i]))
        if r[i] != -1:
            solve(state | (1 << r[i]))


def solution(info, edges):
    global n, val
    n = len(info)
    val = info[:]
    for u, v in edges:
        if l[u] == -1:
            l[u] = v
        else:
            r[u] = v

    solve(1)
    return ans


# 여기선ㄴ 2025년 2월 5일 풀이다.
max_sheep = 0
def solution10(info, edges):
    global max_sheep

    def dfs(node, sheep_wolf, have_to_visit):
        global max_sheep

        # 방문했으니까 동물을 획득한다.
        animal = info[node]
        if animal == 0:  # 양인 경우
            sheep_wolf[0] += 1
        else:  # 늑대인 경우
            sheep_wolf[1] += 1

        # 늑대가 같거나 많아진다면 여기서 양이 최대이다.
        if sheep_wolf[0] <= sheep_wolf[1]:
            max_sheep = max(max_sheep, sheep_wolf[0])
            return

            # 가야할 노드를 추가한다.
        for n_node in graph[node]:
            have_to_visit.append(n_node)

        # 그렇다면 이제 여기서 차례로 방문을 시작한다.
        for n_node in have_to_visit:
            next_have_to_visit = have_to_visit.copy()
            next_have_to_visit.remove(n_node)
            dfs(n_node, sheep_wolf[:], next_have_to_visit)

        # 더이상 방문할 곳이 없는 경우라면
        max_sheep = max(max_sheep, sheep_wolf[0])

    N = len(info)  # 총 노드의 갯수
    graph = [[] for _ in range(N)]
    for p, c in edges:
        graph[p].append(c)

    dfs(0, [0, 0], [])
    return max_sheep