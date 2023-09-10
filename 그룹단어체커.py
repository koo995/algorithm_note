n = int(input())
words = [input() for _ in range(n)]
print(words)
count = n
for word in words:
    list = []
    for idx, letter in enumerate(word):
        if idx+1 < len(word) and word[idx+1] == letter:
            continue
        if letter not in list:
            list.append(letter)
        else:
            count -= 1
            break
print(count)

# 솔직히 continue 라는 것을 쓸 생각을 못했어...
# 뒤에 있는 녀석이 같으면 건너뛴다라... 