def solution():
    from string import ascii_uppercase

    N, B = map(int, input().split())
    # 10진법 N을 B진법으로...
    result = ""
    letters = {}
    for idx, e in enumerate(list(ascii_uppercase)):
        letters[idx + 10] = e

    while True:
        if N < B:
            if N >= 10:
                N = letters[N]
            result = str(N) + result
            break
        if (N % B) >= 10:
            s = letters[N % B]
            result = s + result
        else:
            result = str((N % B)) + result
        N = N // B
    print(result)

    # 이 방법이 더 낫네...
    N, B = map(int, input().split())
    s = ""
    arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while N:
        s += str(arr[N % B])
        N //= B

    print(s[::-1])


def solution2():
    from string import ascii_uppercase

    letters = {idx: ch for idx, ch in enumerate(ascii_uppercase, start=10)}

    # 10진수 N을 B진법으로 변환
    N, B = map(int, input().split())
    # 정녕 나누기를 해나가며 더해야 하나...?
    answer = []
    while 1:
        if N < B:
            answer.append(str(N) if N < 10 else letters[N])
            break
        remain = N % B
        answer.append(str(remain) if remain < 10 else letters[remain])
        N = N // B
    print("".join(answer[::-1]))
    pass


solution2()
# 이걸 굳이 리스트로 변경할 필요는 없었구나... 그냥 str더하기 연산만 해도 충분...
