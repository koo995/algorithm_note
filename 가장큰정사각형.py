# n, m = map(int, input().split())
# arr = [(lambda str: list(map(int, list(str))))(input()) for _ in range(n)]
# print("arr: ", arr)
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# print("dp: ", dp)
# max_value = 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1:
#             # 3개의 축에대해서 비교를 해본다.
#             dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + arr[i][j]
#             max_value = max(dp[i + 1][j + 1], max_value)
# print(max_value**2)


# 0이 앞에 있는 경우 유의하자. 이거 변환할때 숫자가 아닌 문자로 들어갔군...
# 내가 왼쪽이나 윗부분을 고려 안하고 시작했는데... 그 부분에서 문제가 생긴것 같아
# 역시 탐색을 할 때는 전부다 탐색하자. 대충 그럴꺼 같은데? 하면서 건너뛰니까 문제가 발생한듯


import copy

n, m = map(int, input().split())
# 비교를 하기 위해서는 이 값들이 정수일 필요가 있군
array = [(lambda input: list(map(int, list(input))))(input()) for _ in range(n)]
print("array: ", array)
dp = copy.deepcopy(array)
max_value = 0
for i in range(n):
    for j in range(m):
        if array[i][j] != 1:
            continue
        # 어쨋든 해당위치에서 1이 되어있어야 dp을 확인한다.
        if i > 0 and j > 0:
            dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        max_value = max(max_value, dp[i][j])
for row in dp:
    s = "".join(map(str, row))
    print(s)
print(max_value**2)

# 왜 안되는건지 그 이유를 좀 알아야 겠는데?
# 그냥 다른방식으로 했더니 풀리더라가 아닌...
# 찾았다... 111 이런경우... 못잡는 구나...
# 1부터 하면 안되는 이유가... 11111111 과 같은 경우 때문이구나
