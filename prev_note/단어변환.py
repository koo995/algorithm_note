def check_link(word1, word2):
    # word1과 word2가 딱 한글자만 다르다는 것을 체크하는 함수
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return True if count == 1 else False


def solution(begin, target, words: list):
    # 모든 words 간에 연관관계를 탐색해 봐야 겠어.
    # dict을 사용할까? 아니면 각 단어를 그냥 하나의 index로 생각할까? 후자가 나을듯
    words.append(begin)
    global graph
    # global visited
    graph = [[] for _ in range(len(words))]
    visited = [0] * len(words)

    for idx, word1 in enumerate(words[:-1]):
        for word2 in words[idx + 1 :]:
            if check_link(word1, word2) == True:
                idx_word2 = words.index(word2)
                graph[idx].append(idx_word2)
                graph[idx_word2].append(idx)
    # 위의 식을 람다식으로 한번 바꿔 보면... graph의 노드수와 반환되는 노드수의 차이가 발생하는데 어케 해결할까?
    graph_lambda = []
    # 이제부터 최단거리를 구하자 dfs을 이용한 백트래킹 bfs을 이용하기 위한 큐? 둘다 해보자 뭐
    if target in words:
        target_index = words.index(target)
    else:
        return 0
    start_index = words.index(begin)

    print("graph: ", graph)

    def dfs(start, target, count, results, visited):
        current_visited_table = visited.copy()
        current_visited_table[start] = 1
        # 종료조건 1 찾은 경우
        if start == target:
            print("찾았다.")
            results.append(count)
            return results
        # 종료조건 2 못찾았고 모든 노드 방문한 경우
        if 0 not in current_visited_table:
            print("못찾았다")
            return  # 아무것도 반환하지 않는다.
        # 만약에 못찾으면 종료조건을 어떻게 하지? 방문 했고 안했고를 추가해야지.
        for linked_idx in graph[start]:
            if current_visited_table[linked_idx] == 1:
                continue
            results = dfs(linked_idx, target, count + 1, results, current_visited_table)
        return results

    results = dfs(start_index, target_index, 0, [], visited)
    return min(results)


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
# 먼저 word을 통해 그래프를 만들어야 겠어. 추가로 그래프에 begin도 넣을까
# dfs는 기본적으로 노드들을 방문 하는 방법이다. 여러번 방문하면서 탐색할려면 또 다른 조건을 추가해야 한다.
# dfs? 그러니까 그냥 단순히 재귀를 사용할때 무엇을 반한할 것이냐를 전해야 하는데...
# 반환되는 것을 count과 visited 결과를 모두 반환할려고 하면 거기서 문제가 발생하는 것 같다.
# 오히려 visited을 사용하지 말고 모든 결과를 하나의 리스트에 넣어서 반환하는 방식이 나을지도
# visited는 가변객체라서... 넘겨주는 값이 같은 주소값이라 재귀적으로 이동하는 동안 항상 같은 주소가 왔다갔다 한 것 같아.
# 햐... 이거 너무너무 중요하다. 진짜.


def solution2(begin, target, words: list):
    from collections import defaultdict
    import heapq

    INF = int(1e9)

    # 연결관계 그래프를 만들어 줘야겠다.
    # 하나의 변환만으로 갈수 있나 없나가 연결관계의 조건이다.
    def _check(word1, word2):
        # 자 여기서 n개의 길이의 알파벳에서 한개의 알파벳만 다르다는 것을 체크해줘야 한다.
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
                if count == 2:
                    return False
        return True

    def dijkstra(node):
        q = []
        heapq.heappush(q, (0, node))
        distance[node] = 0
        while q:
            dis, now = heapq.heappop(q)
            if distance[now] < dis:
                continue
            for n_node in graph[now]:
                cost = dis + 1
                if cost < distance[n_node]:
                    distance[n_node] = cost
                    heapq.heappush(q, (cost, n_node))

    words = [begin] + words
    graph = defaultdict(list)
    for idx, word1 in enumerate(words[:-1]):
        for word2 in words[idx + 1 :]:
            if _check(word1, word2):  # 서로 관련이 있다면 양쪽으로 다 넣어주자잉
                graph[word1].append(word2)
                graph[word2].append(word1)
    distance = {word: INF for word in words}
    dijkstra(begin)
    return distance[target] if target in distance else 0




def solution3(begin, target, words: list):
    def is_one_diff(word1, word2):
        n = len(word1)
        diff_count = 0
        for i in range(n):
            if word1[i] != word2[i]:
                diff_count += 1
        return True if diff_count == 1 else False
    from collections import defaultdict, deque
    # 그렇다면... words 들중에서 한개의 변환으로 이동할 수 있는 루트를 다 찾아야겠는데?
    # 그렇다면 1개만 차이난다는 것을 어떻게 판단할까?
    words.append(begin)
    words_size = len(words)
    graph = defaultdict(list)
    for i in range(words_size):
        for j in range(i, words_size):
            if is_one_diff(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    print(graph)
    visited = {word: 0 for word in words}
    # 자 이제 begin을 시작으로 가장 짧은 변환과정을 찾아야 한다.
    # 다익스트라는 너무 쉬워보이니까.... bfs을 이용해볼까?
    q = deque()
    visited[begin] = 1
    q.append((begin, 0))
    while q:
        cur_word, cur_count = q.popleft()
        if cur_word == target:
            return cur_count
        for next_word in graph[cur_word]:
            if visited[next_word]:
                continue
            visited[next_word] = 1
            q.append((next_word, cur_count + 1))
    return 0


print(solution2("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
