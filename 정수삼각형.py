def solution0():
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (i + 1) for i in range(n)]
    dp[0] = costs[0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + costs[i][0]
    for i in range(1, n):
        l = len(costs[i])
        for j in range(1, l):
            dp[i][j] = (
                max(dp[i - 1][j - 1], dp[i - 1][j])
                if j != (l - 1)
                else dp[i - 1][j - 1]
            ) + costs[i][j]
    print(max(dp[-1]))


# 제일 끝 부분에 있는 녀석은 max비교로 넣을 것이 아니군


def solution(triangle):
    dp_triangle = [[0] + i + [0] for i in triangle]
    print("dp+triangle", dp_triangle)
    for idx, triangle_line in enumerate(
        dp_triangle
    ):  # 아하... 이렇게 되었을 때도 idx가 0부터 나오는 구나...
        if idx == 0:
            continue
        for j in range(1, len(triangle_line) - 1):
            print("idx, j: ", idx, j)
            dp_triangle[idx][j] += max(
                dp_triangle[idx - 1][j - 1], dp_triangle[idx - 1][j]
            )
    return max(dp_triangle[-1])


# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


def solution2():
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    print("triangle: ", triangle)
    for i, row in enumerate(triangle[1:], start=1):
        for j in range(len(row)):
            triangle[i][j] += max(
                triangle[i - 1][j - 1] if j - 1 >= 0 else 0,
                triangle[i - 1][j] if j < len(row) - 1 else 0,
            )
    print("trai: ", triangle)
    print(max(triangle[-1]))


solution2()
