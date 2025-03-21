import math
import time


def binary_search(start, end, dis_btw_rocks, n):
    time.sleep(2)
    print("-------이진탐색 시작-------------")
    # 종료조건
    mid = (start + end) / 2
    print(f"start: {start} end: {end}")
    print("mid: ", mid)
    if round(start) >= round(end):
        return round(mid)
    # search 과정 이부분에서 논리적 구조를 올바르게 새워야 하는데... 뭐가 계속 틀린거 같다.
    n_count = 0  # 이녀석은 가만히 있는 녀석들의 갯수다.
    for dis in dis_btw_rocks:
        if dis >= mid:
            n_count += 1
    # 중간값보다 작은게 n_count개 니까 총 n_count-1개를 건드려야 하고 그녀석을 n과 비교해야지

    print("n_count: ", n_count)
    # 재귀 적으로 탐색
    if n_count > len(dis_btw_rocks) - n:
        mid = binary_search(mid, end, dis_btw_rocks, n)
    else:
        mid = binary_search(start, math.ceil(mid), dis_btw_rocks, n)
    return mid


def solution(distance, rocks, n):
    rocks.sort()
    dis_btw_rocks = [
        (lambda rock, idx: rock - rocks[idx - 1] if idx != 0 else rock)(rock, idx)
        for idx, rock in enumerate(rocks)
    ]
    print("dis_btw_rocks: ", dis_btw_rocks)
    answer = binary_search(0, distance, dis_btw_rocks, n)
    bigger_than_answer = [dist for dist in dis_btw_rocks if dist >= answer]
    bigger_than_answer.sort()
    return bigger_than_answer[0]


def solution1(distance, rocks, n):
    answer = 0
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance)  # 마지막 도착지점을 위해서 넣었나 보군.
    # 역시나 길이로 이분탐색을 적용해 나간다.
    left = 0
    right = distance
    while left <= right:
        mid = int(
            (left + right) / 2
        )  # mid 이 녀석을 어쨋든 최소로 잡고싶어 하는 것이지?
        cnt = 0
        rock_point = 0
        # 어쨋든 간에 모든 거리에 대해서 하나하나 확인해 나간다?
        for i in range(len(sorted_rocks)):
            if sorted_rocks[i] - rock_point < mid:
                cnt += 1
            else:  # 여기 이 부분이 내가 생각하지 못한 부분이구나?
                rock_point = sorted_rocks[i]
        if (
            cnt > n
        ):  # 여기서 1로 두는 것도 음... 등호를 안쓰고 종료조건을 저렇게 만들어나가나?
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer


# print(solution1(25, [2, 14, 11, 21, 17], 2))
# print(solution1(28, [2, 9, 14, 11, 21, 17, 20], 4))

"""
만약에 돌멩이 사이의 거리를 최소한 x 이상만큼 만들기 위해서 최소한으로 제거해야하는 돌멩이의 개수는 몇개인가?"
( 또는 "점프력이 x 미만인 사람은 못건너게 할 때 최소한으로 제거해야하는 돌멩이의 개수는 몇개인가? " 라고 생각해도 좋습니다)
"""


def solution2(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    def binary_search(start, end) -> int:
        mid = (start + end) // 2
        if start >= end:
            return mid
        cnt = 0
        rock_point = 0
        for i in range(len(rocks)):
            if rocks[i] - rock_point < mid:
                cnt += 1
            else:
                rock_point = rocks[i]
        if cnt < n:
            mid = binary_search(mid + 1, end)
        else:
            mid = binary_search(start, mid)

        return mid

    start = 0
    end = distance
    while start + 1 < end:
        mid = (start + end) // 2
        cnt = 0
        rock_point = 0
        for i in range(len(rocks)):
            if rocks[i] - rock_point < mid:
                cnt += 1
            else:
                rock_point = rocks[i]
        if cnt < n:
            start = mid
        else:
            end = mid
    return start


def solution3(distance, rocks, n):
    if n >= len(rocks):
        return distance
    
    rocks.sort()
    rocks.append(distance)

    start = 1
    end = distance
    while start + 1 < end:
        mid = (start + end) // 2
        cnt = 0
        rock_point = 0
        for r in rocks:
            if r - rock_point < mid:
                cnt += 1
            else:
                rock_point = r
        if cnt <= n: # 여기서 mid 일때와 start 일때 결과가 같나? start 일때 매우 작을 것이다. mid 일때 도 n 보다 작다면?
            start = mid
        else:
            end = mid
    return start
    
    
    # mid = binary_search(start, end)
    # print("mid: ", mid)


def solution4(distance, rocks, n):
    def get_remove_rock_count(m):
        # 거리의 최소가 m이 되고자한다.
        prev = 0
        count = 0
        for i in range(len(rocks)):
            if rocks[i] - prev < m:
                count += 1
                continue
            prev = rocks[i]
        return count

    rocks = sorted(rocks) + [distance]
    dist_btw_rocks = []

    prev = 0
    for i in range(len(rocks)):
        dist_btw_rocks.append(rocks[i] - prev)
        prev = rocks[i]

    # 가장 특이한 점은 최소중에서 최대를 구하는 것이다.
    start = min(dist_btw_rocks)  # 이것보다 작은 경우는 나타나지 않는다. 무지성으로 0으로 하지 말자.
    end = int(1e9)  # 단순히 max(dist_btw_rocks)로 하면 거리가 더 큰 녀석이 나타날 수 있다.
    while start + 1 < end:
        mid = (start + end) // 2
        if get_remove_rock_count(mid) <= n:
            start = mid
        else:
            end = mid
    return start


print(solution2(25, [2, 14, 11, 21, 17], 2))
