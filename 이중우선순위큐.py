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


print(
    solution(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)


# 한가지 알아가는 것은
# q라는 리스트안에서는 우선순위큐가 정렬이 되어 있지 않다는 것이아.
