def solution():
    from collections import deque
    N, K = map(int, input().split())
    # N 에서 K로 가는 가장 빠른 시간?
    # 기본적으로 완전탐색이 아닌가?
    visited = [0] * 100001

    q = deque()
    visited[N] = 1
    q.append((N, 0))
    while q:
        cur_point, second = q.popleft()
        if cur_point == K:
            print(second)
            break
        if (0 <= cur_point * 2 < len(visited)) and visited[cur_point * 2] == 0:
            visited[cur_point * 2] = 1
            q.append((cur_point * 2, second))
        if (0 <= cur_point - 1 < len(visited)) and visited[cur_point - 1] == 0:
            visited[cur_point - 1] = 1
            q.append((cur_point - 1, second + 1))
        if (0 <= cur_point + 1 < len(visited)) and visited[cur_point + 1] == 0:
            visited[cur_point + 1] = 1
            q.append((cur_point + 1, second + 1))


solution()