# index리스트를 소모시키기보단 fatigue을 소모시켜 나가는 방향으로 dfs을 수행하는 것이 좋구나


def solution(k, dungeons):
    global dungeons_dict
    global fatigue
    fatigue = k
    dungeons_dict = {idx: dungeon for idx, dungeon in enumerate(dungeons)}

    def dfs(dungeon_order_permut, ramain_index_lst):
        current_fatigue = fatigue
        max_count = 0

        # 던전 순서의 조합에 따라 몇개에 들어갈 수 있는지 갯수를 센다.
        for dungeon in dungeon_order_permut:
            required_min_fatigue, fatigue_consume = dungeon
            if required_min_fatigue <= current_fatigue:
                current_fatigue -= fatigue_consume
                max_count += 1

        # 재귀함수의 종료조건
        if len(dungeon_order_permut) == len(dungeons_dict):
            return max_count

        for index in ramain_index_lst:
            # 방문하지 않은 던전리스트에서 다음에 방문할 던전의 index을 제외시킨다.
            next_index_lst = ramain_index_lst.copy()
            next_index_lst.remove(index)
            # 던전의 방문 순서에 다음 던전을 추가한다
            next_dungeon_order_lst = dungeon_order_permut.copy()
            next_dungeon_order_lst.append(dungeons_dict[index])
            max_count = max(dfs(next_dungeon_order_lst, next_index_lst), max_count)
        return max_count

    return dfs([], [i for i in range(len(dungeons))])


print(solution(80, [[80, 20], [50, 40], [30, 10]]))

# current_fatigue가 업데이트가 안되니까 무한루프에 빠지는구나
# 그 이유는 던전 index을 계속 같은녀석을 반복하는데...
# dho dungeon_order_lst가 for문 이후의 녀석으로 계속 유지되는 것이지?
# 너무 많은 시행착오가 있었다. dfs에 필요이상으로 변수를 많이 받았고... 다행히 백트래킹에 대해서 조금은 알게된것 같다


from itertools import permutations


# 던전의 순열에 대해서 몇개의 던전을 들어갈 수 있는지 반환한다.
def check_(dungeons, k):
    result = 0
    for dungeon in dungeons:
        required_min_fatigue, fatigue_consume = dungeon
        if required_min_fatigue <= k:
            k -= fatigue_consume
            result += 1
    return result


def solution1(k, dungeons):
    answer = 0
    for dungeons in list(permutations(dungeons)):
        answer = max(check_(dungeons, k), answer)
    return answer


# print(solution1(80, [[80, 20], [50, 40], [30, 10]]))

# `for` 루프를 나왔을 때 `dungeon_order_lst`의 값이 유지되는 것은 Python에서 리스트와 같은 가변 객체(mutable objects)의 동작 방식 때문입니다. 가변 객체는 함수에 전달될 때 참조(reference)로 전달되기 때문에, 함수 내에서 이 객체를 수정하면 원본 객체도 변경됩니다.

# `dungeon_order_lst`는 리스트이며, `dfs` 함수에 인자로 전달될 때, 이 리스트의 참조가 전달됩니다. 따라서, 함수 내에서 `dungeon_order_lst.append(...)` 를 호출하면, 이 변경사항은 함수 외부에 있는 원본 리스트에도 반영됩니다.

# 이러한 문제를 해결하기 위해서는 재귀 호출을 수행할 때마다 리스트의 새로운 복사본을 생성해야 합니다. 이렇게 하면 각 재귀 호출이 독립적인 리스트 인스턴스를 가지게 되어, 한 호출에서의 변경사항이 다른 호출에 영향을 미치지 않습니다.

# `dfs` 함수 내에서 재귀 호출을 할 때 `dungeon_order_lst`의 복사본을 만들고, 그 복사본을 수정하여 다음 재귀 호출에 전달해야 합니다. 예를 들어, 다음과 같이 할 수 있습니다:


# 이 방법을 사용하면 각 재귀 호출마다 `dungeon_order_lst`의 독립적인 복사본을 사용하게 되어, 원본 리스트가 다른 재귀 호출에 의해 변경되지 않습니다.
