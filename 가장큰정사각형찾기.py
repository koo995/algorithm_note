n, m = map(int, input().split())
arr = [(lambda str: list(map(int, list(str))))(input()) for _ in range(n)]
print("arr: ", arr)
dp = [[0] * (m + 1) for _ in range(n + 1)]
print("dp: ", dp)
max_value = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            # 3개의 축에대해서 비교를 해본다.
            dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + arr[i][j]
            max_value = max(dp[i + 1][j + 1], max_value)
print(max_value**2)


# 0이 앞에 있는 경우 유의하자. 이거 변환할때 숫자가 아닌 문자로 들어갔군...
# 내가 왼쪽이나 윗부분을 고려 안하고 시작했는데... 그 부분에서 문제가 생긴것 같아
# 역시 탐색을 할 때는 전부다 탐색하자. 대충 그럴꺼 같은데? 하면서 건너뛰니까 문제가 발생한듯
