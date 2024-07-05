def solution():
    def check(m: int) -> int:
        # m이라는 숫자보다 작거나 같은 숫자들의 갯수를 세어보자
        # i 번째 행에서 m 보다 작거나 같은 녀석들의 갯수를 구하고 더해보자
        count = 0
        for i in range(1, N + 1):
            count += min(N, m//i)
        return count

    N = int(input())  # 10^5 이하
    K = int(input())  # K는 최대 10^9 최소 1
    # 이분탐색을 할 필요가 있을 듯 하다.배열의 값을 미리 정의하는 것은 힘들 것 같다.
    s = 0  # check(s) != check(e)을 만족하기 위함
    e = N * N  # 이렇게 잡아도 될까
    while s + 1 < e:
        mid = (s + e) // 2
        if check(mid) < K:
            s = mid
        else:
            e = mid
    print(e)


def solution2():
    def check(m):
        count = 0
        for i in range(1, n + 1):
            count += min(n, m // i)
        return count

    n = int(input())
    k = int(input())
    start = 0
    end = n ** 2
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid) <= k:  # 이런식으로 하면 mid 값에 해당하는 녀석이 여러개 있을 수 있어서. 단순히 mid 가 k 번째 수인지 구하기 어렵다.
            start = mid
        else:
            end = mid
    print(start)



solution()
