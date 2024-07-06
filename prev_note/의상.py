from itertools import combinations


def solution(clothes):
    dic = {}
    for clothe in clothes:
        if clothe[1] in dic:
            dic[clothe[1]].append(clothe[0])
            continue
        dic[clothe[1]] = [clothe[0]]

    result = 0
    for c in range(1, len(dic) + 1):
        # 지금부터 c개의 의상의 조합을 찾아나갈 것이다.
        clothe_combi_list = list(map(list, combinations(dic.keys(), c)))
        for clothe_combi in clothe_combi_list:
            # clothe_combi = ['headgear', 'eyewear']
            mul = 1
            for clothe in clothe_combi:
                mul = mul * len(dic[clothe])
            result += mul
    return result


def solution2(clothes):
    dic = {}
    for clothe in clothes:
        if clothe[1] in dic:
            dic[clothe[1]].append(clothe[0])
            continue
        dic[clothe[1]] = [clothe[0]]

    result = 1
    for key in dic.keys():
        result = result * (len(dic[key]) + 1)
    return result - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ]
    )
)

# 이제 모든 조합에 대한 수를 세어나갸야 한다.
# for문을 3번이나 도는데... 이게 맞나
# 역시 아닌것 같아. 이 방법 단 한케이스에 대해서 시간초과가 발생해.
# 와 지렸다. 조합을 찾는 새로운 방법이를까? 역시 단순한 갯수반환이니까 이게 맞는거 같다.
# 내가 한 방법은 진짜 하나하나 조합을 다 찾는 경우지
