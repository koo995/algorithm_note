import math

A, B, V = map(int, input().split())


def sol1():
    cur = 0
    count = 0
    while True:
        count += 1
        if (cur + A) >= V:
            break
        cur = cur + A - B
    print(count)


count = math.ceil((V - A) / (A - B)) + 1
print(count)


# 좋은 것을 배워가는 문제같다. 단순히 반복문으로는 어렵지
# 블로그에 있는 풀이는 허구한날 ㅅㅂ.. 똑같은 풀이밖에 없어
def solutiuon():
    import math

    A, B, V = map(int, input().split())
    c = math.ceil((V - A) / (A - B)) + 1
    return c


print(solutiuon())
