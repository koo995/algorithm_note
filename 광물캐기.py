import math


def solution(picks, minerals):
    sub_minerals = [
        minerals[i * 5 : i * 5 + 5] for i in range(math.ceil(len(minerals) / 5))
    ]  # 미네랄을 우선 잘게 쪼갯군
    for idx, sub_mineral in enumerate(sub_minerals):
        prio = count_prio(sub_mineral)  # 각 더미마다의 우선순위를 계산하고
        sub_minerals[idx].append(prio)  # 더미의 마지막에다가 집어넣었군
    if sum(picks) >= len(sub_minerals):
        sub_minerals.sort(key=lambda x: x[-1], reverse=True)
    else:
        dif = len(sub_minerals) - sum(picks)
        sub_minerals = sub_minerals[:-dif]
        sub_minerals.sort(key=lambda x: x[-1], reverse=True)
    result = 0
    for sub_mineral in sub_minerals:
        if picks[0] != 0:  # 다이아 도끼를 쓰는 경우 항상 5?
            result += count_fatigue(sub_mineral, 0)
            picks[0] -= 1
        elif picks[1] != 0:  # 철을 쓰는 경우
            result += count_fatigue(sub_mineral, 1)
            picks[1] -= 1
        elif picks[2] != 0:  # 돌을 쓰는 경우
            result += count_fatigue(sub_mineral, 2)
            picks[2] -= 1
        else:
            break  # 모두 다 0 이란 것이니까... 곡괭이를 다 쓴 경우
    return result


def count_fatigue(bunch, p):
    result = 0
    bunch.pop()
    table = [
        {"diamond": 1, "iron": 1, "stone": 1},
        {"diamond": 5, "iron": 1, "stone": 1},
        {"diamond": 25, "iron": 5, "stone": 1},
    ]
    pick = table[p]
    for b in bunch:
        result += pick[b]
    return result


def count_prio(bunch):
    result = 0
    table = {"diamond": 25, "iron": 5, "stone": 1}
    for i in bunch:
        result += table[i]
    return result


# 곡괭이가 먼저 소모되는 경우 마지막 녀석은 어짜피 못쓰니까 아니지... 마지막 앞 앞 녀석도 못 캘 수도? 곡괭이가 캘 수 있는데까지 우선순위 고려하면 되겠네
# 여기 이 부분 반드시 알아가자 minerals[a:b]이렇게 할때 b가 전체 길이보다 크더라도 index 에러는 발생하지 않고 마지막까지 가준다.


def solution2(picks: list, minerals: list):
    import copy

    fatigue_table = [
        {"diamond": 1, "iron": 1, "stone": 1},
        {"diamond": 5, "iron": 1, "stone": 1},
        {"diamond": 25, "iron": 5, "stone": 1},
    ]
    results = []

    def dfs(picks: list, minerals: list, fatigue):
        if sum(picks) == 0 or not minerals:
            results.append(fatigue)
            return

        for i in range(3):
            if picks[i] != 0:
                tmp_picks = picks.copy()
                tmp_fatigue = fatigue
                tmp_picks[i] -= 1
                for mineral in minerals[:5]:
                    tmp_fatigue += fatigue_table[i][mineral]
                dfs(tmp_picks, minerals[5:], tmp_fatigue)
                # 여기에서 일일이 tmp을 만들어줘야 하냐....? 다른 방법 없냐
                # 슬라이싱은 새로운 객체를 만들어 내는 구나
        return 0

    dfs(picks, minerals, 0)  # 이 두 녀석들은 계속해서 업데이트 될 것이다.
    return min(results)


# print(
#     solution2(
#         [1, 3, 2],
#         ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
#     )
# )
print(
    solution2(
        [1, 0, 1],
        [
            "diamond",
            "diamond",
        ],
    )
)


# 음... 왜 틀린거지? 완전탐색을 똑바로 한 것 같은디
# 속도는 위에서 그리디로 푸는 것이 더 빠르구나...
