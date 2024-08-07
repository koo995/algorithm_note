def solution(stones, k):
    def check(person_num, k):
        stack = []
        for stone in stones:
            diff = stone - person_num + 1
            if diff > 0:
                if len(stack) + 1 > k:
                    return False
                stack = []
            else:
                stack.append(0)
        if len(stack) + 1 > k:
            return False
        return True

    start = 0
    end = max(stones) + 2
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid, k):
            start = mid
        else:
            end = mid
    return start

# 위의 풀이는 계속 8, 10, 12 에서 시간초과가 발생한다.
def solution2(stones, k):
    def check(person_num, k):
        jump = 0
        for stone in stones:
            diff = stone - person_num + 1
            if diff > 0:
                if jump + 1 > k:
                    return False
                jump = 0
            else:
                jump += 1
        return False if jump + 1 > k else True

    start = 2
    end = max(stones) + 2
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid, k):
            start = mid
        else:
            end = mid
    return start