import math


def binary_search(start, end, n, times):
    middle_point = (start + end) // 2
    count_n = 0
    for time in times:
        count_n += middle_point // time
    if count_n != n:
        return False
    return True


def solution(n, times):
    middle_point = math.floor((n // len(times)) * (sum(times) // len(times)))

    answer = middle_point
    return answer


print(solution(6, [7, 10]))

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
