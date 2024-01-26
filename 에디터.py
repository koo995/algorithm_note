def solution():
    from collections import deque

    class Node:
        def __init__(self, value, prev, next):
            self.value = value
            self.prev = prev
            self.next = next

        def __str__(self):
            return f"Node : (value: {self.value}, prev: {self.prev}, next: {self.next})"

        def __repr__(self) -> str:
            return self.__str__()

    # 그 다음 이것을 어떻게 초기화를 하지?
    # 해당하는 index에 node객체가 존재한다.
    input_data = list(input())
    N = len(input_data)
    q = deque(
        [
            Node(value, i - 1 if i > 0 else None, i + 1 if i < N - 1 else None)
            for i, value in enumerate(input_data)
        ]
    )

    print("q: ", q)
    M = int(input())
    orders = [(input().split()) for _ in range(M)]
    print("orders: ", orders)
    # 커서는 제일 뒤에 있다고 했으니까
    cursor = N  # 이것과 같이 포인터를 두는 것이 맞는가?
    for order in orders:
        operation = order[0]
        insert_data = order[1] if len(order) > 1 else None
        if operation == "L":
            if q[-1].prev != None:
                q.rotate()
        if operation == "D":
            if q[-1].next != None:
                q.rotate(-1)
        if operation == "B":
            return 0
        if operation == "P":
            return 0


# print(solution())


# 자 이 문제는 stack 2개를 이어주는 방식과
# 연결리스트를 이용하는 방법 이렇게 있다?


def solution2():
    s = input()  # 길이 10만 넘지않음
    M = int(input())
    orders = [input().split() for _ in range(M)]
    stack_1 = list(s)
    stack_2 = []
    for order in orders:
        oper = order[0]
        insert_ch = None
        if len(order) > 1:
            insert_ch = order[1]
        if oper == "L":
            if stack_1:
                ch = stack_1.pop()
                stack_2.append(ch)
        if oper == "D":
            if stack_2:
                ch = stack_2.pop()
                stack_1.append(ch)
        if oper == "B":
            if stack_1:
                stack_1.pop()
        if oper == "P":
            stack_1.append(insert_ch)
    return "".join(stack_1 + stack_2[::-1])


print(solution2())

# 리스트에 원소가 하나인 경우 왜 reverse()을 하면 빈 리스트지?
# list[::-1] 이렇게하면 자동으로 역순이군?
