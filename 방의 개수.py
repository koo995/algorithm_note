from collections import defaultdict, deque


def solution(arrows):
    # 특정 자료구조 안에 뭐가 잇나 없나를 체크하는 것은 dic구조가 적합하지 않을까?
    # 리스트로 in 연산은 시간 복잡도가 너무나 높다. O(N) 이나 된다.
    node_visited = defaultdict(int)
    line_visited = defaultdict(int)
    # 어떤 자료구조를 가져갈까? set 설정을 할 일은 많은데... 부모자식 관계는 한방향이란 말이지? 근데 선은 양방향이란 말이지?
    count = 0

    # 하나 확실한건 arrows을 전부다 살피기 전까지 어떤 크기의 배열을 가질지 알수 없다.
    # 힌트가 될수 있는것은 (0,0)을 기준으로 움직이는 것이다.
    def node_visit_check(node: tuple):
        if node_visited[node]:
            return True
        return False

    def line_visit_check(line: tuple):
        node1, node2 = line
        if line_visited[(node1, node2)] or line_visited[(node2, node1)]:
            return True
        return False

    start = (0, 0)
    node_visited[start] = 1
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for idx, arrow in enumerate(arrows):  # 이것은 10만 이하다.
        current_x = start[0]
        current_y = start[1]
        # 두칸씩 움직이기로 했지?
        for _ in range(2):
            next_x = current_x + dx[arrow]
            next_y = current_y + dy[arrow]

            # 방법 1
            if node_visit_check((next_x, next_y)):
                if not line_visit_check(((current_x, current_y), (next_x, next_y))):
                    count += 1
            else:
                node_visited[(next_x, next_y)] = 1
            # 차이는 밑의 두줄 차이인데... 도대체 왜????
            line_visited[(current_x, current_y), (next_x, next_y)] = 1
            line_visited[(next_x, next_y), (current_x, current_y)] = 1

            # 방법 2
            if not node_visit_check((next_x, next_y)):
                node_visited[(next_x, next_y)] = 1
                line_visited[(current_x, current_y), (next_x, next_y)] = 1
                line_visited[(next_x, next_y), (current_x, current_y)] = 1
            else:  # 만약 방문한 녀석이라면 count을 올려야 하는데, 대신에 지나갔던 길이면 안된다. 안지나갔던 길이면 지나갔다고 체크를 해줘야 하지.... 와 이런 멍청한
                if not line_visit_check(((current_x, current_y), (next_x, next_y))):
                    # print(f"arrow:{idx},{arrow} 일때 카운트 업")
                    count += 1
            # 방법 1과 방법 2의 차이가 도대체 뭐지? 이걸 해결해야 겠는데?
            current_x = next_x
            current_y = next_y
        start = (next_x, next_y)

    print("count: ", count)
    return 0


# 아래의 녀석처름... queue에다가 순서대로 다 담고 하는 방법이 편할꺼 같기도 하고?
def solution2(arrows):
    answer = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)

    # visited : 노드 방문 체크
    # visited_dir : 노드 방문 경로 체크 ((A, B)는 A -> B 경로를 의미)
    visited = defaultdict(int)
    visited_dir = defaultdict(int)

    # arrows 따라 노드 좌표를 큐에 추가
    queue = deque([now])
    for i in arrows:
        # 모래 시계 형태 예외를 처리하기 위해 해당 방향으로 2칸씩 추가한다.
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            queue.append(next)

            now = next

    now = queue.popleft()
    visited[now] = 1

    while queue:
        next = queue.popleft()

        # 이미 방문한 노드(visited[x]==1)인 경우
        if visited[next] == 1:
            # 해당 경로로 처음 들어온 경우인 경우 answer++
            # 처음 들어온 경우에 방이 처음 생성되므로!
            if visited_dir[(now, next)] == 0:
                answer += 1
        # 처음 방문한 노드인 경우 방문 체크를 한다.
        else:
            visited[next] = 1

        # 해당 노드로 들어온 경로를 방문 체크해준다.
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next

    return answer


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))
print(solution([0, 6, 4, 2, 7, 2, 5]))

# 아하.... set은 해시가 안되는 구나...
# 뭐때문에 틀렸을까? 시간초과가 발생하기도 한다.
# set안에 set을 넣는 것은 안되는 구나... 계속 unhashable이 발생하네
# 그렇다면 line의 방문처리는 어케 하는거지?
# 어디서 뭐가 잘못된 것이지? 논리구조는 맞는거 같은데... 되게 사소한 어느 부분에서 틀렸을 것 같다.
