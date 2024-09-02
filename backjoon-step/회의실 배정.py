def solution():
    N = int(input())  # 최대 10만까지 가능하다
    meetings =[tuple(map(int, input().split())) for _ in range(N)]
    meetings.sort(key=lambda meeting:(meeting[1], meeting[1] - meeting[0])) # 이것은 틀리고... 시작시간이 더 짧은 녀석이어야 하네...?
    end = meetings[0][1]
    count = 1
    if N == 1:
        print(count)
    else:
        for n_s, n_e in meetings[1:]:
            if end <= n_s:
                count += 1
                end = n_e
        print(count)


def solution2():
    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]
    meetings.sort(key=lambda meeting: (meeting[1], meeting[0]))
    start = meetings[0][0]
    end = meetings[0][1]
    count = 1
    if N == 1:
        print(count)
    else:
        for meeting in meetings[1:]:
            next_start = meeting[0]
            next_end = meeting[1]
            if end <= next_start:
                count += 1
                end = next_end
        print(count)
    pass

solution2()