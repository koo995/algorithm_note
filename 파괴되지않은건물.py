def solution(board, skills):
    # 그렇다면 스킬들의 공격을 다 합할 테이블이 필요하군
    MAX_X = len(board)
    MAX_Y = len(board[0])

    total_affect = [[0] * (MAX_Y + 1) for _ in range(MAX_X + 1)]
    print("board: ", board)
    print("total_affect: ", total_affect)

    # 모든 공격에 대한 계산?
    for type, x1, y1, x2, y2, degree in skills:  # 모든 스킬들을 다 합한다음 보드에 적용한다!
        # 이제부터 스킬하나하나에 대한 영향을 보드에 적용할 것이다.
        # 1일 경우는 적의 공격을 의미합니다. 건물의 내구도를 낮춥니다.
        total_affect[x1][y1] += degree if type != 1 else -degree
        total_affect[x1][y2 + 1] -= degree if type != 1 else -degree
        total_affect[x2 + 1][y1] -= degree if type != 1 else -degree
        total_affect[x2 + 1][y2 + 1] += degree if type != 1 else -degree

    # 모든 공격에 대한 누적합을 적용하자
    # 한번은 밑에서 아래로 한번은 왼쪽에서 오른쪽으로
    for i in range(len(total_affect)):
        for j in range(1, len(total_affect[0])):
            total_affect[i][j] += total_affect[i][j - 1]

    for i in range(len(total_affect[0])):
        for j in range(1, len(total_affect)):
            total_affect[j][i] += total_affect[j - 1][i]
    print("total_affect: ", total_affect)
    count = 0
    for i in range(MAX_X):
        for j in range(MAX_Y):
            if board[i][j] + total_affect[i][j] >= 1:
                count += 1
    return count


# print(
#     solution(
#         [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
#         [
#             [1, 0, 0, 3, 4, 4],
#             [1, 2, 0, 2, 3, 2],
#             [2, 1, 0, 3, 1, 2],
#             [1, 0, 1, 3, 3, 1],
#         ],
#     )
# )
print(
    solution(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
    )
)


# 미쳤다는 말밖에 안나온다 이런 방법이 있다니 너무 신기하다
