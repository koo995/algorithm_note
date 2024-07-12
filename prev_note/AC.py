def solution():
    from collections import deque

    T = int(input())
    cases = [[input() for _ in range(3)] for _ in range(T)]

    for case in cases:
        case = [
            case[0],
            int(case[1]),
            list(map(int, case[2][1:-1].split(","))) if len(case[2]) > 2 else [],
        ]
        functions = case[0]
        n = case[1]
        arr = deque(case[2])
        flag = True
        reverse = False
        R_count = 0

        for func in functions:
            if func == "D":  # 버리기
                if len(arr) != 0:
                    if reverse == False:
                        arr.popleft()  # 인덱스를 지정해서 그렇구나...
                    else:
                        arr.pop()
                else:
                    print("error")
                    flag = False
                    break

            else:  # func == "R" 뒤집기
                R_count += 1
                reverse = True if R_count % 2 != 0 else False
        if flag == False:
            continue

        result = list(arr)
        if R_count % 2 != 0:
            result.reverse()
        print(str(result).replace(" ", ""))


# 시간 초과가 발생하네... 뒤집기에서 문제가 생기는 것 같아.
# 어디서 뭘 어떻게 줄여야 하지? 뒤집기에서 로그연산을 하면 시간복잡도가 딱 알맞는듯
# boolean 변수로 R의 갯수에 따라 앞에서 뒤에서 pop() 하는 방식을 썼는데...
# 어떤 케이스에서 틀린걸까?


def solution2():
    from collections import deque

    def operate(test_case: tuple) -> None:
        orders, _, arr = test_case
        arr = deque(arr)
        reverse = False
        for order in orders:
            if order == "R":
                reverse = not reverse
            if order == "D":
                if arr:
                    arr.popleft() if reverse == False else arr.pop()
                else:
                    print("error")
                    return
        arr = list(arr)
        arr = str(arr if reverse == False else arr[::-1])
        arr.replace(" ", "")
        print(arr)

    T = int(input())  # 테스트케이스의 갯수
    test_cases = []
    for _ in range(T):
        p = input()
        n = int(input())
        arr = input()[1:-1]
        arr = arr.split(",") if len(arr) > 0 else []
        test_cases.append((p, n, arr))
    for test_case in test_cases:
        operate(test_case)
def solution3():
    from collections import deque

    def operate(func_lst, arr_lst):
        print(arr_lst)
        reverse_flag = False
        for func in func_lst:
            if func == "R":
                reverse_flag = not reverse_flag
            else:
                if len(arr_lst) == 0:
                    return "error"
                if reverse_flag:
                    arr_lst.pop()
                else:
                    arr_lst.popleft()
        return list(arr_lst) if reverse_flag == False else list(arr_lst)[::-1]

    T = int(input())
    for _ in range(T):
        func_lst = list(input())
        n = int(input())
        arrays = (input()[1:-1]).split(",")
        print(operate(func_lst, arrays))



solution3()
# 흐음.... 왜 에러가 안들어가는 것일까??
# 헐? arr = "[]" 인 경우... arr[1:-1].split(",") -> [''] 이런 결과가 나온다고....? 왜,,,?
