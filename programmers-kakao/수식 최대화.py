def solution(expression):
    from itertools import permutations
    def calculate(num_lst, oper_lst, priority):
        for op in priority:
            while op in oper_lst:
                # 이 안에 있는 연산자는 모두 계산해야지?
                idx = oper_lst.index(op)
                oper_lst.pop(idx)
                if op == "*":
                    result = num_lst[idx] * num_lst[idx + 1]
                    num_lst[idx] = result
                    num_lst.pop(idx + 1)
                elif op == "+":
                    result = num_lst[idx] + num_lst[idx + 1]
                    num_lst[idx] = result
                    num_lst.pop(idx + 1)
                else:  # 여기서는 "-" 이겠다.
                    result = num_lst[idx] - num_lst[idx + 1]
                    num_lst[idx] = result
                    num_lst.pop(idx + 1)
        return abs(sum(num_lst))

    operands = []
    operations = []
    priorites = permutations(("*", "-", "+"), 3)
    operand = ""
    for c in expression:
        if not c.isdigit():
            operands.append(int(operand))
            operations.append(c)
            operand = ""
            continue
        operand += c
    operands.append(int(operand))
    max_value = 0
    for priority in priorites:
        max_value = max(max_value, calculate(operands.copy(), operations.copy(), priority))

    answer = max_value
    return answer