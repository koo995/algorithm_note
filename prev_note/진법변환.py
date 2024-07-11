import math


def solution():
    from string import ascii_uppercase

    letters = {}
    for idx, a in enumerate(list(ascii_uppercase)):
        letters[a] = idx + 10

    N, B = (lambda x: (x[0], int(x[1])))(input().split())
    result = 0
    for idx, s in enumerate(N):
        # n이 정수가 가능하다면 어떻게 처리하지?
        if s.isdigit():
            result += int(s) * pow(B, (len(N) - idx - 1))
        else:
            result += letters[s] * pow(B, (len(N) - idx - 1))

    print(result)


def solution2():
    from string import ascii_uppercase
    from collections import defaultdict
    import math

    letters = defaultdict(int)
    for idx, ch in enumerate(ascii_uppercase, start=10):
        letters[ch] = idx

    N, B = input().split()
    B = int(B)  # B 진법이다. 34진법에면 34^1 + 34^0 이런식으로 계산가야 한다.
    N = list(
        N
    )  # N은 ZZB123 이렇게 나올 수 있다. 단 36진법일때만 Z까지 일테고... 아니면 그 전까지
    answer = 0
    for i, num in enumerate(N[::-1]):
        if num.isdigit():
            answer += pow(B, i) * int(num)
        else:
            answer += pow(B, i) * letters[num]

    print("answer: ", answer)

def solution3():
    from string import ascii_uppercase

    letters = {i: i for i in range(10)}
    for idx, ch in enumerate(ascii_uppercase, start=10):
        letters[ch] = idx

    N, B = input().split()  # 숫자 N이 B 진법으로 표현된다.
    B = int(B)
    N_lst = list(N)  # N의 각 자리마다 B^i값을 곱해나간다.
    size = len(N_lst)
    result = 0
    for sub_N in N_lst:
        # sub_N이 십진수로 무슨 값인지 알아야겠는데?
        result += int(letters[sub_N] * math.pow(B, size - 1))
        size -= 1
    print(result)


    pass


solution3()
