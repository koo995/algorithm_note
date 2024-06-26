def solution():
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())
    array.sort()
    s = 0
    e = 1
    count = 0
    while 0 <= s < e < n:
        if array[s] + array[e] == x:
            s -= 1
            e += 1
            count += 1
        elif array[s] + array[e] < x:
            s += 1
            e += 1
        else:  # array[s] + array[e] > x:
            s -= 1
    print(count)


solution()