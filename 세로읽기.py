def solution():
    words = [input() for _ in range(5)]
    for x in range(15):
        for y in range(5):
            if len(words[y]) <= x:
                continue
            print(words[y][x], end="")


def solution2(my_string: str, m, c):
    answer = [
        (lambda i: my_string[m * i + c - 1])(i) for i in range(len(my_string) // m)
    ]
    return "".join(answer)


print(solution2("ihrhbakrfpndopljhygc", 4, 2))
