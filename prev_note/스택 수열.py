import heapq


def solution():
    n = int(input())
    goal = [int(input()) for _ in range(n)]  # 4 3 6 8 7 5 2 1
    goal_pointer = 0
    stack = [
        int(i) for i in range(n + 1)
    ]  # 반드시 오름차순으로 대입 될 것 [0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, ... n ]
    stack_pointer = 1
    result = []
    result.append("+")
    while 0 < stack_pointer < len(stack):
        if stack[stack_pointer] < goal[goal_pointer]:  # 1~4이 4보다 같거나 작다면
            stack_pointer += 1
            result.append("+")
        elif stack[stack_pointer] == goal[goal_pointer]:
            stack.pop(stack_pointer)
            stack_pointer -= 1
            goal_pointer += 1
            result.append("-")
        else:
            print("NO")
            break
    if goal_pointer != n:
        print("No")
    else:
        print(result)


# goal_pointer가 수열끝에 다다르지 않았는데 반복문이 빠져나왔다면 역시 에러


def solution2():
    from collections import deque

    def n_generator(n):
        lst = [i for i in range(1, n + 1)]
        yield from lst

    n = int(input())
    gen = n_generator(n)
    array = deque([int(input()) for _ in range(n)])
    stack = []
    result = []
    while array:
        if len(stack) == 0 or array[0] > stack[-1]:
            stack.append(next(gen))
            result.append("+")
            continue
        elif array[0] == stack[-1]:
            v = stack.pop()
            result.append("-")
            array.popleft()
        else:
            result.clear()
            result.append("NO")
            break
    for i in range(len(result)):
        print(result[i])


solution2()

# 모든 결과를 다 모은 다음에 NO을 반환하는 방법 밖에 없는가??
