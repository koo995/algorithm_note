from itertools import product
from bisect import bisect_left


def solution(infos, queries):  # info는 5만이하, query는 10만이하 점수는 10만이하
    # 모든 정보는 개발언어, 직군, 경력, 소울푸드 순이다.
    # 그리고 모든 값들은 and조건인 것을 명시하자. 이러면 시간복잡도를 줄일 수 있을 것이다.

    # 어떤 점수 이상이다라는 것은 어떻게 구할까? 정렬? 이 부분은 리스트로 써도 되겠는데?
    # 만약 5만명의 데이터에 대해서...

    dev_lang = ["cpp", "java", "python", "-"]
    dev_role = ["backend", "frontend", "-"]
    dev_pos = ["junior", "senior", "-"]
    foods = ["chicken", "pizza", "-"]

    table = {lang: {role: {pos: {food: [] for food in foods} for pos in dev_pos} for role in dev_role} for lang in
             dev_lang}
    # 이제 테이블을 초기화하자.
    for info in infos:
        lang, role, pos, food, score = info.split(" ")
        # 여기서 16가지의 경우의조합을 어떻게 만들지? 솔직히 이걸 해야하나 말아야하나 고민하고... 안하는 방향으로 망설였다. 16이라는 수가 너무 크다 생각들어서 한심하군...
        keys = product([lang, "-"], [role, "-"], [pos, "-"], [food, "-"])
        for l, r, p, f in keys:
            table[l][r][p][f].append(int(score))

    result = []
    # 이제 쿼리문을 수행하자.
    for query in queries:
        lang, role, pos, food_and_score = query.split(" and ")
        food, score = food_and_score.split(" ")
        temp = table[lang][role][pos][food]
        # 여기서 score 이상인 녀석의 수를 세어야한다.
        temp.sort()
        idx = bisect_left(temp, int(score))
        result.append(len(temp) - idx)
    return result


from itertools import product
from bisect import bisect_left
from collections import defaultdict

# 하... 효율성 2개를 통과못하고 있다.
def solution2(infos, queries):  # info는 5만이하, query는 10만이하 점수는 10만이하
    table = defaultdict(list)
    # 이제 테이블을 초기화하자.
    for info in infos:
        lang, role, pos, food, score = info.split(" ")
        score = int(score)
        keys = map("".join, product([lang, "-"], [role, "-"], [pos, "-"], [food, "-"]))
        for key in keys:
            table[key].append(score)

    result = []
    # 이제 쿼리문을 수행하자.
    for query in queries:
        lang, role, pos, food_and_score = query.split(" and ")
        food, score = food_and_score.split(" ")
        temp = table[lang + role + pos + food]
        # 여기서 score 이상인 녀석의 수를 세어야한다.
        temp.sort()
        idx = bisect_left(temp, int(score))
        result.append(len(temp) - idx)
    return result