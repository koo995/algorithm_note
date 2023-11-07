import math

n = int(input())
i = 1
while 1:
    s = 3 * math.pow(i, 2) - 3 * i + 1
    if n <= s:
        print(i)
        break
    i += 1
