def solution():
    from collections import deque

    N = int(input())  # 100만이 최대. 이 사이의 임의의 정수가 비번
    M = int(input())  # 로그인에 시도에 사용될 비밀번호의 갯수... 최대 10만개
    passwords = [*map(int, input().split())]

    # 안전도의 초기값을 무엇으로 처리하지? 알지 못하는 것들은 -1로 하자
    safty = [-1 for _ in range(N + 1)]

    q = deque()
    for password in passwords:
        q.append(password)
        safty[password] = 0
    max_safty = 0
    while q:
        cur_password = q.popleft()
        # 이 녀석으로부터 안전도가 1인 녀석들을 다 구해보자
        # 아하 2^20이 되어야 100만까지 표현가능하지... 2^19는 최대 50만 정도라구
        for i in range(20):
            n_password = cur_password ^ (1 << i)
            # 근데 혹시나 중복되는 녀석들이 생길 수 있잖아?
            if n_password > N or safty[n_password] != -1:
                continue
            # n_password의 안전도를 갱신하고, 그 녀석이 최대라면 max_safty을 바꿔준다. 그리고 q에 삽입
            safty[n_password] = safty[cur_password] + 1
            max_safty = max(max_safty, safty[n_password])
            q.append(n_password)
    print(max_safty)


solution()


# 여기서 구해야 할것은 N 사이의 임의의 수 중에서 안전도가 제일 높은 수를 구하는 것이다.
# 비트 연산을 할려면 특히 xor 연산은 ^을 이용한다 그러면 그 결과값이 10진수로 표현된다.
# 비트연산과 dp을 이용하는 것일줄 알았으나... bfs라는 용어가 나왔다. 그래프...  완전 첫 단추부터 잘못되었다. 어떻게 해결할지?
# 아니 애초에 이 문제를 그래프로 나타낼수가 있나..? 다른 방법은 없을까? 그래프라니 그건 비약이 심해 나에게는...


def solution2():
    import sys
    from collections import deque

    input = sys.stdin.readline

    N = int(input())
    M = int(input())
    try_passwords = list(map(int, input().split()))
    # 최대 N인데 이 모든 값들에 대해서 디폴트 안전거리는 21로 설정을 해두었네
    safety = [21 for _ in range(N + 1)]
    dq = deque()

    # 시도하는 비밀번호들은 본인 자신에 대해서는 안전거리의 최소가 0인 안전도를 가진다. 하긴 시도하는 녀석중에 있으면 전혀 안전하지 않은 것이군
    for try_password in try_passwords:
        safety[try_password] = 0
        dq.append(try_password)

    ans = 0

    while dq:
        cur_try_password = dq.popleft()

        for i in range(20):
            password_candidate = (1 << i) ^ cur_try_password
            # password_candidate이 녀석은 후보가 아니니까 안전도가 아마 21로 기본 설정되어 있겠지? 그러니까 업데이트 되지 않앗다고 봐도 되겠다.
            if (
                password_candidate <= N
                and safety[cur_try_password] + 1 < safety[password_candidate]
            ):
                safety[password_candidate] = safety[cur_try_password] + 1
                ans = max(safety[password_candidate], ans)
                dq.append(password_candidate)
    print(ans)
