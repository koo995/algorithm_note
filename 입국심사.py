import math


def binary_search(start, end, n, times):
    middle_point = (start + end) / 2  # 나중에 이녀석을 반환 해야지?
    # 종료조건이라 하자. 결국에는 소수점 까지 비교해 나가면서 반올림 했을때 완전히 일치하는 지점이 정답이구나
    if round(start) >= round(end):
        return int(middle_point)
    count_n = 0
    for time in times:
        count_n += middle_point // time
    if count_n < n:
        middle_point = binary_search(middle_point, end, n, times)
    else:
        middle_point = binary_search(start, middle_point, n, times)

    return middle_point


def solution(n, times):
    start = 0
    end = int(1e18)  # 최악의 경우 1명의 심사위원 10억분 소요 사람 10억명
    min_time = binary_search(start, end, n, times)
    return min_time


# print(solution(6, [7, 10]))

# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하자
# 사람은 1명이상 10억 이하
# 심사관 항명이 걸리는시간도 1이상 10억 이하
# 심사관은 1명이상 10만 이하
# 끝난 타이밍에 1분더 기다리면... 다른 빠른 심사대원이 빌테니까 그곳으로 간다는 것이군...
# 이걸 문제 그대로 구현해서 풀어봤자 답은 안나올 것 같다.
# 조건에서 10억 이하라는 조건을 보자 이분탐색이 적절할 것 같다. 모든것을 탐색한다는 것은
# n이나 times을 for문 돌린다는것은 미친짓
# 미들 포인트 업데이트 하는 것을 어케 하지? start와 end을 정하고 그 가운데를 middle_point?
# 이분 탐색도 재귀적으로 하는 것이구나...?
# start와 middle_point가 같은경우 무한 재귀가 이루어진다. 어떻게 해결하지?
# 이 마지막 특정 한점을 특정하는 조건을 어케 할까?


def solution2(n, times):
    def binary_search(start, end) -> int:
        mid = (start + end) // 2
        # 재귀적이니까 종료조건이 필요하다. 그렇지만 그 종료조건을... count와 n이 같은 경우라 한다면 굳이 여기서 종료조건을 걸 필요는 없을 것이다.
        if start >= end:
            return mid

        count = 0
        for time in times:
            count += mid // time
        # 내가 원하는 것은 최소의 시간이다.
        # count와 n이 일치하지 않을때는 mid + 1을 해주고... 같을때는 그대로 넣어주네? 이 부분이 너무나 헷갈린다
        # 소수점 이하는 무시되어서 그런 것인가?
        if count < n:
            mid = binary_search(mid + 1, end)
        else:
            mid = binary_search(start, mid)
        # 아하... 여기서 mid을 반환을 해야하구나
        return mid

    # 이진탐색도 결국은 재귀적인 것이 아닌가?

    s = 1
    e = int(1e18)
    return binary_search(s, e)


print(solution2(6, [7, 10]))

# 저번에도 헷갈렸던 것인데... 포인트가 실수와 정수를 왔다갔다 하니까 그 부분 처리하기가 조금 빡세다
# 어짜피 내가 구하는 값이 소수점은 아니잖아? 결국은 정수아냐? 그러면 정수로 다루는게 맞아보이는데?
# 단순히 모두 그냥 했더니 실패가 발생했다...
# 과연 여기서 단순히 정수로 따지는게 맞을까..?
# 하... 이 미묘한 차이를 잘 처리하기가 어렵다....
