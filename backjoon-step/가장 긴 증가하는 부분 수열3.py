import bisect

def solution():
    def get_index(num):
        idx = bisect.bisect_left(lis, num)
        return idx
    
    N = int(input())
    arrays = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = 1
    lis = [arrays[0]]
    for i in range(1, N):
        if lis[-1] < arrays[i]:
            lis.append(arrays[i])
        else:
            idx = get_index(arrays[i])
            lis[idx] = arrays[i]
    print(len(lis))

solution()