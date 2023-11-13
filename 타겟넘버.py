import math


def solution(numbers, target):
    count = 0
    number_pointer = 0
    visited = set()

    def dfs(number_list, target, count, pointer):
        count = 0
        if (tuple(number_list) not in visited) and (sum(number_list) == target):
            count = count + 1
        visited.add(tuple(number_list))
        if pointer == len(number_list):
            return count

        for _ in range(2):
            number_list[pointer] = number_list[pointer] * (-1)
            count += dfs(number_list, target, count, pointer + 1)
        return count

    return dfs(numbers, target, count, number_pointer)


print(solution([4, 1, 2, 1], 4))

# numbers의 원소를 하나하나 다 바꿔볼까? 마지막에 sum 함수 써서 확인해보면 어떨까?
# 그렇다면 어떻게 그 모든케이스의 경우를 체크하지? 20개 이하면... 2^20의 가짓수인데... 104만 정도 된다고 볼수 있다. 그러면 할만한가?
# 재귀적으로 했을때 왜 count을 계속해서 가져가지 못하지?
# dfs의 마지막에 count을 반환하는 것으로써 상위에 호출했던 녀석에게 아래에서 얻은 count값을 전달해줄 수 있다.


# 이 방식은 count을 글로벌하게 설정한다음 업데이트 하는 방식을 사용했다.
def solution1(numbers, target):
    global count
    count = 0
    number_pointer = 0
    visited = set()

    def dfs(number_list, target, pointer):
        global count
        # 우선은 방문처리를 한다.
        if (tuple(number_list) not in visited) and (sum(number_list) == target):
            count += 1
        # 먼저 로직을 처리하고 방문을 했다고 마킹해야지
        visited.add(tuple(number_list))
        # 이 녀석은 종료조건...? 재귀함수에서 더이상 깊게 들어가지 못하도록하는!
        if pointer == len(number_list):
            return 0
        for _ in range(2):
            number_list[pointer] = number_list[pointer] * (-1)
            dfs(number_list, target, pointer + 1)

    dfs(numbers, target, number_pointer)
    return count


# print(solution1([4, 1, 2, 1], 4))

# numbers의 원소를 하나하나 다 바꿔볼까? 마지막에 sum 함수 써서 확인해보면 어떨까?
# 그렇다면 어떻게 그 모든케이스의 경우를 체크하지? 20개 이하면... 2^20의 가짓수인데... 104만 정도 된다고 볼수 있다. 그러면 할만한가?
# 재귀적으로 했을때 왜 count을 계속해서 가져가지 못하지?
# 왜 끝이 아닌 부분에서 None이 리턴되는지 해명하자.


answer = 0


def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if idx == N and target == value:
        answer += 1
        return
    if idx == N:
        return

    DFS(idx + 1, numbers, target, value + numbers[idx])
    DFS(idx + 1, numbers, target, value - numbers[idx])


def solution2(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer


# 이 방법은 처음부터 모든 배열을 보는 것이 아닌... 4 1 2 1 이 있으면 (4) (-4) (4 -1) (4 + 1) 이렇게 모든경우를 탐색하는 구나...


def dfs(nums, idx, n, target):
    # 왜 ret은 0을 해놨을까?
    ret = 0
    if idx == len(nums):
        if n == target:
            return 1
        else:
            return 0
    ret += dfs(nums, idx + 1, n + nums[idx], target)
    ret += dfs(nums, idx + 1, n - nums[idx], target)
    return ret


def solution3(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer
