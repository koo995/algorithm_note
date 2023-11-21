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


print(solution(25, [2, 14, 11, 21, 17], 2))
