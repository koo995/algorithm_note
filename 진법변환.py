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


solution2()
