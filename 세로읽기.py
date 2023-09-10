words = [input() for _ in range(5)]
for x in range(15):
    for y in range(5):
        if len(words[y]) <= x:
            continue
        print(words[y][x], end="")