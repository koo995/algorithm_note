def solution2():
    n = int(input())
    words = [input() for _ in range(n)]
    print(words)
    count = n
    for word in words:
        list = []
        for idx, letter in enumerate(word):
            if idx + 1 < len(word) and word[idx + 1] == letter:
                continue
            if letter not in list:
                list.append(letter)
            else:
                count -= 1
                break
    print(count)


# 솔직히 continue 라는 것을 쓸 생각을 못했어...
# 뒤에 있는 녀석이 같으면 건너뛴다라...


def solution():
    def checker(word):
        prev_set = set()
        prev_p = word[0]
        for c in word:
            if c in prev_set:
                return 0
            if c == prev_p:
                continue
            prev_set.add(prev_p)
            prev_p = c
        return 1

    n = int(input())
    words = [input() for _ in range(n)]
    count = 0
    for word in words:
        count += checker(word)
    return count


print(solution())
