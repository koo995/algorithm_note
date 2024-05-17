# 이 방식은 메모리 초과가 발생하는구나... 메모리초과를 막기위해 제너레이터를 썼지만...
# 이제는 시간초과에 걸린다...
# 구글에 dfs로 푼 코드를 봤는데 중복을 처리하지는 못하네...
import itertools

def solution():
    def get_team_combinations(p_lst):
        # 여기서 팀의 조합을 찾아야한다...
        combinations = list(itertools.combinations(p_lst, len(p_lst) // 2))
        combinations.sort()
        combinations_size = len(combinations)
        for i in range(combinations_size // 2):
            yield combinations[i], combinations[combinations_size - i - 1]  # 여기서 이렇게 짝이 맞춰진다는 것이 신기하네

    def get_power(team: list) -> int:
        power = 0
        combs = itertools.combinations(team, 2)
        for a, b in combs:
            power += S[a-1][b-1]
            power += S[b-1][a-1]
        return power

    def get_balance(a_team, b_team) -> int:
        a_power = get_power(a_team)
        b_power = get_power(b_team)
        return abs(a_power - b_power)

    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    players = [i for i in range(1, N + 1)]
    min_balance = int(1e9)
    for team_a, team_b in get_team_combinations(players):
        min_balance = min(min_balance, get_balance(team_a, team_b))
    print(min_balance)


