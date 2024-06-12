def solution():
    Array = input()
    bomb = list(input())
    bomb_len = len(bomb)
    stack = []
    for ch in Array:
        stack.append(ch)
        while len(stack) >= bomb_len and stack[-bomb_len:] == bomb:
            for _ in range(bomb_len):
                stack.pop()
    if stack:
        print("".join(stack))
    else:
        print("FRULA")


solution()
# 시간초과가 발생하네...?
# 와 String += String 은 시간복잡도가 N^2 이 되겠네