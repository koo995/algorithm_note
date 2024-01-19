from itertools import product
import time


def solution(word):
    start = time.time()
    chars = ["A", "E", "I", "O", "U", " "]
    table = product(chars, chars, chars, chars, chars)
    table = list(map("".join, table))
    table = list(map(st, table))
    end = time.time()
    print(list(table))
    print("total_time: ", end - start)
    return 0


def solution2(word):
    table = []
    chars = ["A", "E", "I", "O", "U"]
    for blank_num in range(len(chars)):
        # 빈칸이 하나라면 5개중에 중복을 선택해서 4개의 순열을 구해야지.
        result = list(map("".join, product(chars, repeat=len(chars) - blank_num)))
        table += result
    print("table: ", table)
    table.sort()  # 이걸보면... 모든 조합을 다 구하고 결국에 정렬을 하는 것이구나? 한가지 알아가야할것은... sort함수가 어떤식으로 정렬을 하는가야. 사전식? 으로 한다는 것인데 사전식이 어떤건지 알아둘 필요가 있어.
    for word in table:
        print(word)
    return table.index(word)


print(solution2("AAAAE"))

# " "이것을 넣어서 모든 조합을 구하는 것은 아닌것 같다.
# 경우의수를 세어보니 정말 무식한 방법으로 하나하나 다 찾는것이 나을 것 같더라
