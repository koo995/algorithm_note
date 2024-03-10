def solution(arr):
    nums = []
    opers = []
    for idx, ch in enumerate(arr):
        if idx % 2 != 0:
            opers.append(ch)
        else:
            nums.append(int(ch))
    print(nums)
    print(opers)
    n = len(nums)
    INF = int(1e8)
    """
    [5, 3, 1, 2, 4]
    ['-', '+', '+', '-']
    """
    max_dp = [[-INF] * n for _ in range(n)]
    min_dp = [[INF] * n for _ in range(n)]
    for step in range(len(nums)):
        for start in range(n - step):
            end = start + step
            # 작은것부터 먼저 구해나간다.
            if start == end:
                max_dp[start][end] = min_dp[start][end] = nums[start]
                continue
            for mid in range(start, end):
                if opers[mid] == "+":
                    max_dp[start][end] = max(
                        max_dp[start][end], max_dp[start][mid] + max_dp[mid + 1][end]
                    )
                    min_dp[start][end] = min(
                        min_dp[start][end], min_dp[start][mid] + min_dp[mid + 1][end]
                    )
                else:
                    max_dp[start][end] = max(
                        max_dp[start][end], max_dp[start][mid] - min_dp[mid + 1][end]
                    )
                    min_dp[start][end] = min(
                        min_dp[start][end], min_dp[start][mid] - max_dp[mid + 1][end]
                    )
    print("max_dp: ", max_dp)
    print("min_dp: ", min_dp)
    return max_dp[0][-1]


solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])


def solution2(arr):
    INF = 987654321
    n = len(arr)  # 숫자 갯수임.
    MIN_DP = [[INF for _ in range(n)] for _ in range(n)]
    MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]

    for step in range(n):  # i와 j의 간격.

        for i in range(n - step):  # i부터 j까지의 연산을 수행함.

            j = i + step

            if step == 0:
                MAX_DP[i][i] = MIN_DP[i][i] = 0
            else:
                for k in range(
                    i, j
                ):  # i 부터 j까지 돌면서, 괄호를 하나는 늘리고, 하나는 줄여서 각각의 범위 연산을 수행함.
                    if 1 == "+":  # k번째에 해당되는 연산이 + 일 경우:
                        MAX_DP[i][j] = max(
                            MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k + 1][j]
                        )  # + 일 경우 최댓값은 최댓값 + 최댓값임.
                        MIN_DP[i][j] = min(
                            MIN_DP[i][j], MIN_DP[i][k] + MIN_DP[k + 1][j]
                        )  # + 일 경우 최솟값은 최솟값 + 최솟값임.
                    else:  # k번째에 해당되는 연산이 - 일 경우.
                        MAX_DP[i][j] = max(
                            MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k + 1][j]
                        )  # - 일 경우 최댓값은 최댓값 - 최솟값임.
                        MIN_DP[i][j] = min(
                            MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k + 1][j]
                        )  # - 일 경우 최솟값은 최솟값 - 최댓값임.

    return MAX_DP[0][n - 1]


def solution3(arr):
    NEG_INF = float("-inf")
    POS_INF = float("inf")
    nums, ops = [], []  # 여기서 숫자와 연산을 불리했군
    for idx, element in enumerate(arr):
        nums.append(element) if not idx % 2 else ops.append(element)

    N = len(nums)
    dp_max = [[NEG_INF] * N for _ in range(N)]
    dp_min = [[POS_INF] * N for _ in range(N)]

    for scope in range(N):
        print(f"사이 거리가 {scope} 일때: ")
        for start in range(N - scope):
            end = start + scope
            print(f"  start: {start}, end: {end}")
            if start == end:
                dp_max[start][start] = dp_min[start][start] = int(nums[start])
                continue

            # 어쨋든 여기서는 dp[start][end]의 최댓값을 구하기 위한 코드이다. 가운데 mid을 둬서 나누고 모든 연산을 파악해 본다.
            for mid in range(start, end):
                print(f"    mid가 {mid}일때")
                if ops[mid] == "+":
                    dp_max[start][end] = max(
                        dp_max[start][mid] + dp_max[mid + 1][end], dp_max[start][end]
                    )
                    dp_min[start][end] = min(
                        dp_min[start][mid] + dp_min[mid + 1][end], dp_min[start][end]
                    )
                elif ops[mid] == "-":
                    dp_max[start][end] = max(
                        dp_max[start][mid] - dp_min[mid + 1][end], dp_max[start][end]
                    )
                    dp_min[start][end] = min(
                        dp_min[start][mid] - dp_max[mid + 1][end], dp_min[start][end]
                    )

    return dp_max[0][-1]


# solution3(["5", "-", "3", "+", "1", "+", "2", "-", "4"])
# [5, -3, 1, 2, -4]
# 대충 점화식은 안다고 해도.. dp을 구성하는 이유는 연산량을 줄이기 위함인데, for문을 어떻게 배치하냐도 엄청나게 중요하잖아?
# 제일 큰 틀은 사잇거리가 0일때부터 4일따 까지인 경우다. 이거는 0~4까지의 함에서 각각 거리가 0인경우에서의 최소...
# 그런데 지금 제일 이해가 안가는 부분은.. for문의 최상단이 사이거리가 되는 것이다.
# 우리는 기본적으로 0~4까지의 최대값을 구하는 것이다. 그 경우는 연산자 기준으로 괄호를 한다했을때 양쪽의 최대값의 연산이 된다.
# 그렇다면 괄호안의 연산들도 최대를 이루어야 하는데... 우리는 연산에서 중복되는 계산이 있다는 것을 알수있다.
# 그렇다면... 그 중복되는 연산들을 본인자신... 바로옆의 하나 바로옆옆의 연산까지 점점 크게 키워나가면 최종계산할때 연산의 중복이 안나타나지 않을까? 로 접근하는게 맞지않을까 싶다.
# 최종 계산까지는 총 4개합의 연산까지 고려가 되야하니까.. 서서히 0개(자신) 부터 최대까지 고려되야 할 것이다.
# 어쨋든 dp라는 것은 중복된 연산을 줄이기 위함이다. 그리고 start와 end사이의 최대를 구할때 그 사이에는 반드시 그 갯수보다 작은 수의 묶음을 가진 피연산자들이 들어간다
# 가장 작은 합을 구해놓으면 더 큰 범위는 작은범위를 이용하여 구할 수 있다.
