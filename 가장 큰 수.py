from itertools import permutations


def solution(numbers: list):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x[0], reverse=True)
    # numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    two_array_numbers = [[] for _ in range(10)]
    for n in numbers:
        two_array_numbers[int(n[0])].append(n)
    for idx, two_array_number in enumerate(two_array_numbers):
        if two_array_number is []:
            two_array_numbers.pop(idx)

    print("two_array_numbers: ", two_array_numbers)

    answer = ""
    return numbers


print(solution([23, 45, 6, 67, 89, 99, 76, 45, 23, 67, 9, 6, 4, 999, 3, 91, 92, 929]))

# two_array_numbers:  [[], [], [23, 23], [3], [45, 45, 4], [], [6, 67, 67, 6], [76], [89], [99, 9, 999, 91, 92, 929]]
# 막히는 부분은?
