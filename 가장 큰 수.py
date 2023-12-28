def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)

    return "".join(numbers) if numbers[0] != "0" else "0"


print(solution([23, 45, 6, 67, 89, 99, 76, 45, 23, 67, 9, 6, 4, 999, 3, 91, 92, 929]))

# two_array_numbers:  [[], [], [23, 23], [3], [45, 45, 4], [], [6, 67, 67, 6], [76], [89], [99, 9, 999, 91, 92, 929]]
# 막히는 부분은?

import functools


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (
        int(t1) < int(t2)
    )  #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0


def solution2(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int("".join(n)))
    return answer


from functools import cmp_to_key


def solution3(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers = sorted(numbers, key=cmp_to_key(lambda a, b: -1 if a + b >= b + a else 1))
    answer = "".join(numbers)

    return str(int(answer))


# 이 문제 존나 좋은것 같다.
# sort을 할때 어떻게 정렬을 하는지 근본부터 정하게 되는것 같아.


def solution4(numbers):
    # 우선 그냥 드는 방법이 있는데 그거 먼저 해보자
    # 예전에 봤던건데 각 자릿수마다 영향력?  1000자리니까 그것을 적용하자
    dom_list = []
    for number in numbers:
        l = len(str(number))
        d = (str(number) * 4)[:4]
        dom_list.append((d, l))
    dom_list.sort(reverse=True)
    answer = ""
    for info in dom_list:
        d, l = info
        answer += d[:l]
    return answer if answer[0] != "0" else "0"


def solution5(numbers):
    from functools import cmp_to_key

    def my_comp(a, b):
        print("호출")
        s1 = int(a + b)
        s2 = int(b + a)
        return 1 if s1 >= s2 else -1

    numbers = list(map(str, numbers))
    new_list = sorted(numbers, key=cmp_to_key(my_comp), reverse=True)
    print("new_list: ", new_list)


print(solution5([3, 30, 34, 5, 9, 44, 77]))
# print(solution([0, 0, 0]))
# 0이 있을수도있다. [0,0,0]을 고려하지 않은 케이스 이 경우는 0이 나와야 한다.
