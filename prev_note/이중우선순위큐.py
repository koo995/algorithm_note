import heapq


def solution(operations):
    def execute(operation: str, q):
        print("-----------------------")
        print("q: ", q)
        oper, num = operation.split(" ")
        if oper == "I":
            heapq.heappush(q[0], int(num))  # 최소우선순위큐
            heapq.heappush(q[1], -int(num))  # 최대우선순위큐
            return
        if num == "1" and q[1]:  # 최대값에서 가져온다
            max_num = -1 * heapq.heappop(q[1])
            # 최소 큐에서도 제거해 줘야지
            q[0].remove(max_num)
            return max_num
        if num == "-1" and q[0]:
            min_num = heapq.heappop(q[0])
            q[1].remove(-min_num)
            return min_num

    q = [[], []]  # 한녀석은 최소, 한녀석은 최대
    for operation in operations:
        result = execute(operation, q)
        if result:
            print(result)
    print("연산 후 q: ", q)
    if q[0]:
        max_value = -1 * heapq.heappop(q[1])
        min_value = heapq.heappop(q[0])
        return [max_value, min_value]
    return [0, 0]


# 한가지 알아가는 것은
# q라는 리스트안에서는 우선순위큐가 정렬이 되어 있지 않다는 것이아.


def solution2(operations):
    from collections import deque
    import heapq

    # 우선순위 큐는... 제일 작은 것이 앞에 오는 구나...
    # 다만 그 뒷부분이 정렬이 된다는 것은 아니다.
    h_min = []
    h_max = []
    for s in operations:
        operation, digit = (lambda l: (l[0], int(l[1])))(s.split(" "))
        if operation == "I":
            heapq.heappush(h_min, digit)
            heapq.heappush(h_max, -digit)
            pass
        if h_min and operation == "D":
            # 최대값을 제거해야 한다.
            if digit == 1:
                pop_item = -heapq.heappop(h_max)
                h_min.remove(pop_item)
                # 그렇다면... 최소힙에서 어떻게 원소를 제거하지?
            else:
                # 최소값 삭제
                pop_item = -heapq.heappop(h_min)
                h_max.remove(pop_item)
    if h_max or h_min:
        return [-heapq.heappop(h_max), heapq.heappop(h_min)]
    return [0, 0]


print(
    solution2(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)
