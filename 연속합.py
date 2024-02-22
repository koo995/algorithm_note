def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    # arr = 10 -4 3 1 5 6 -35 12 21 -1
    sums = [0] * n
    if n == 1:
        print(arr[0])
    else:
        sums[0] = arr[0]
        for i in range(1, n):
            sums[i] = max(sums[i - 1] + arr[i], arr[i - 1] + arr[i], arr[i])
        if arr[n - 1] > sums[n - 1]:
            sums[n - 1] = arr[n - 1]
        print(max(sums))


# 어쨋든 전체에서 최대값만 구하면 되잖아?
# 새로운 녀석이 들어왔을때 그녀석을 포함하는 최대값을 어떻게 구할까?
# 새로운 녀석이 들어 왔을때 그 녀석을 포함하는 최대값이라 생각해보자
# 그 전까지는 그 녀석을 포함하지 않는 최대값이 되겠지?
# n번째를 포함하년 녀석을 고려할 때, n-1 번째 와의 합만 고려하면 될까? n-2 + n-1 + n은?
# 이미 n-1을 고려할 때 n-1와의 합을 고려했고, 그 녀석은 전체 합보다 작다는 것이 확인 됨.
# 위의 식에서 한번 틀렸는데 뭐가 문제지?
# 새롭게 추가된 녀석이 그 하나만으로 매우 크다면 다른 녀석을 포함하는 경우로 할 필요가 없지...
# 그런데... 왜 arr[i-1] + arr[i] 이걸 빼도 가능한 걸까...


def solution2():
    n = int(input())
    seq = list(map(int, input().split()))
    max_sum = [0] * n
    max_sum[0] = seq[0]
    if len(seq) == 1:
        print(seq[0])
    else:
        for idx in range(1, n):
            max_sum[idx] = max(
                max_sum[idx - 1] + seq[idx], seq[idx]
            )  # 여기서 바로 직전까지의 최대썸은...
        print(max(max_sum))


solution2()
