from bisect import bisect_left, bisect_right

def solution():
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    sum_A, sum_B = [], []
    for i in range(n):
        s = A[i]
        sum_A.append(s)
        for j in range(i + 1, n):
            s += A[j]
            sum_A.append(s)

    for i in range(m):
        s = B[i]
        sum_B.append(s)
        for j in range(i + 1, m):
            s += B[j]
            sum_B.append(s)

    count = 0
    sum_B.sort()
    for i in range(len(sum_A)):
        value = T - sum_A[i]

        hi = bisect_right(sum_B, value)
        lo = bisect_left(sum_B, value)
        count += (hi - lo)

    print(count)


solution()