def solution():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    acc_sum = [arr[0]]
    for i in range(1, N):
        acc_sum.append(acc_sum[-1] + arr[i])
    start = 0
    end = 1
    INF = int(1e9)
    min_len = INF
    while 0 <= start < end < N:
        continuous_sub_sum = acc_sum[end] - (acc_sum[start - 1] if start - 1 >= 0 else 0)
        if continuous_sub_sum >= S:
            min_len = min(min_len, end - start + 1)
            start += 1
        else:
            end += 1
    #  혹시나 길이가 1인 녀석이 S보다 더 클 수 있다.
    for a in arr:
        if a >= S:
            min_len = 1
    # 만족하는 녀석이 없다
    print(min_len if min_len != INF else 0)

solution()